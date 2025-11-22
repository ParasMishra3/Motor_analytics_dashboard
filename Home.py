import streamlit as st
import pandas as pd
import sys
import os

# Add utils to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

from viz_utils import *
from model_utils import calculate_kpis

# Page config
st.set_page_config(
    page_title="Motor Insurance Analytics",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
    }
    .metric-value {
        font-size: 2rem;
        font-weight: bold;
        color: #1f77b4;
    }
    .metric-label {
        font-size: 1rem;
        color: #666;
    }
</style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    try:
        df = pd.read_csv('data/motor_insurance_data.csv')
        return df
    except FileNotFoundError:
        st.error("Data file not found. Please run data generation first.")
        st.stop()

df = load_data()

# Sidebar
st.sidebar.title("🚗 Motor Insurance Analytics")
st.sidebar.markdown("---")
st.sidebar.markdown("### Navigation")
st.sidebar.info(
    """
    **Main Dashboard** - Overview and key metrics

    Use the pages menu above to access:
    - 📊 Customer Analytics
    - 🎯 Retention Prediction
    - ⚠️ Risk Analysis
    - 🔍 Claims & Fraud
    - 💰 Pricing & Portfolio
    - 📈 Executive Summary
    """
)

# Filters
st.sidebar.markdown("---")
st.sidebar.markdown("### Filters")

lob_filter = st.sidebar.multiselect(
    "Line of Business",
    options=df['lob'].unique(),
    default=df['lob'].unique()
)

location_filter = st.sidebar.multiselect(
    "Location Type",
    options=df['location_type'].unique(),
    default=df['location_type'].unique()
)

# Apply filters
if lob_filter:
    df = df[df['lob'].isin(lob_filter)]
if location_filter:
    df = df[df['location_type'].isin(location_filter)]

# Main content
st.markdown('<h1 class="main-header">🚗 Motor Insurance Analytics Dashboard</h1>', unsafe_allow_html=True)

# Calculate KPIs
kpis = calculate_kpis(df)

# Display key metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="📋 Total Policies",
        value=f"{kpis['total_policies']:,}",
        delta=None
    )

with col2:
    st.metric(
        label="💰 GWP (Gross Written Premium)",
        value=f"₹{kpis['gwp']/10000000:.2f} Cr",
        delta=None
    )

with col3:
    st.metric(
        label="📊 Loss Ratio",
        value=f"{kpis['loss_ratio']*100:.1f}%",
        delta=f"{(kpis['loss_ratio']*100 - 65):.1f}% vs target",
        delta_color="inverse"
    )

with col4:
    st.metric(
        label="🔄 Renewal Rate",
        value=f"{kpis['renewal_rate']*100:.1f}%",
        delta=f"{(kpis['renewal_rate']*100 - 82):.1f}% vs target",
        delta_color="normal"
    )

st.markdown("---")

# Charts
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(plot_lob_distribution(df), use_container_width=True)
    st.plotly_chart(plot_premium_distribution(df), use_container_width=True)

with col2:
    st.plotly_chart(plot_renewal_rate_by_lob(df), use_container_width=True)
    st.plotly_chart(plot_loss_ratio_by_lob(df), use_container_width=True)

# Additional metrics
st.markdown("---")
st.markdown("### 📈 Additional Metrics")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📋 Total Claims", f"₹{kpis['total_claims']/10000000:.2f} Cr")
    st.metric("📊 Avg Premium", f"₹{kpis['avg_premium']:,.0f}")

with col2:
    st.metric("⚠️ Fraud Rate", f"{kpis['fraud_rate']*100:.2f}%")
    st.metric("🔄 Churn Rate", f"{kpis['churn_rate']*100:.1f}%")

with col3:
    st.metric("📉 Claims Frequency", f"{kpis['claims_frequency']:.3f}")
    st.metric("💵 Avg Claims Amount", f"₹{kpis['avg_claims_amount']:,.0f}")

# LOB-wise breakdown
st.markdown("---")
st.markdown("### 📊 LOB-wise Performance")

lob_stats = df.groupby('lob').agg({
    'policy_id': 'count',
    'premium': ['sum', 'mean'],
    'claims_amount': 'sum',
    'renewed': 'mean',
    'fraud': 'mean'
}).round(2)

lob_stats.columns = ['Policies', 'Total Premium (₹)', 'Avg Premium (₹)', 
                     'Total Claims (₹)', 'Renewal Rate', 'Fraud Rate']
lob_stats['Loss Ratio'] = (lob_stats['Total Claims (₹)'] / lob_stats['Total Premium (₹)']).round(4)
lob_stats['Renewal Rate'] = (lob_stats['Renewal Rate'] * 100).round(1)
lob_stats['Fraud Rate'] = (lob_stats['Fraud Rate'] * 100).round(2)

st.dataframe(lob_stats, use_container_width=True)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666; padding: 1rem;'>
        <p>Motor Insurance Analytics Platform | Data Science Dashboard</p>
        <p>Built with Streamlit | Private Car • Two-Wheeler • Commercial Vehicle</p>
    </div>
    """,
    unsafe_allow_html=True
)
