# Motor Insurance Analytics Dashboard

A comprehensive Streamlit-based analytics platform for motor insurance covering Private Car, Two-Wheeler, and Commercial Vehicle segments.

## Features

### 📊 **Dashboard Pages**

1. **Home Dashboard** - Overview with key metrics and KPIs
2. **Customer Analytics** - Segmentation, retention analysis, and CLV
3. **Retention Prediction** - Interactive ML-powered churn prediction tool
4. **Claims & Fraud** - Claims analysis and fraud detection
5. **Pricing & Portfolio** - Rate relativities and portfolio performance
6. **Executive Summary** - One-page executive view

### 🔧 **Key Capabilities**

- **Predictive Models**: XGBoost-based retention and fraud detection
- **Risk Segmentation**: K-means clustering for customer segments
- **Interactive Visualizations**: Plotly charts with drill-down capabilities
- **Real-time Predictions**: Input customer data for instant risk scoring
- **Portfolio Analytics**: GWP, loss ratios, combined ratios
- **Telematics Analytics**: UBI premium calculations

## Project Structure

```
motor_insurance_dashboard/
│
├── Home.py                          # Main dashboard page
│
├── pages/                           # Additional dashboard pages
│   ├── 1_📊_Customer_Analytics.py
│   ├── 2_🎯_Retention_Prediction.py
│   ├── 3_🔍_Claims_Fraud.py
│   ├── 4_💰_Pricing_Portfolio.py
│   └── 5_📈_Executive_Summary.py
│
├── utils/                           # Utility modules
│   ├── data_generator.py          # Synthetic data generation
│   ├── model_utils.py              # ML models (retention, fraud, segmentation)
│   └── viz_utils.py                # Visualization functions
│
├── data/                            # Data directory
│   └── motor_insurance_data.csv    # Generated synthetic dataset
│
├── models/                          # Trained model artifacts (optional)
├── assets/                          # Static assets (images, etc.)
├── requirements.txt                 # Python dependencies
└── README.md                        # This file
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup Steps

1. **Clone or download this repository**

```bash
cd motor_insurance_dashboard
```

2. **Create a virtual environment (recommended)**

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On Mac/Linux
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Generate synthetic data**

```bash
python utils/data_generator.py
```

This will create `motor_insurance_data.csv` in the `data/` folder with 5,000 synthetic policy records.

## Usage

### Running the Dashboard

```bash
streamlit run Home.py
```

The dashboard will open in your default web browser at `http://localhost:8501`

### Navigating the Dashboard

- **Home**: Start here for an overview of key metrics
- **Sidebar**: Use filters to segment data by LOB and location
- **Pages**: Navigate between different analytics modules using the sidebar menu
- **Interactive Elements**: Click on charts, adjust sliders, and explore data

### Using the Retention Prediction Tool

1. Go to the "Retention Prediction" page
2. Enter customer details using the input fields
3. Click "Predict Renewal Probability"
4. View the predicted renewal probability and recommendations

## Data Dictionary

### Key Fields

- **policy_id**: Unique policy identifier
- **lob**: Line of Business (Private Car, Two-Wheeler, Commercial Vehicle)
- **age**: Customer age
- **premium**: Annual premium amount (₹)
- **annual_km**: Estimated annual kilometers driven
- **accident_history**: Number of previous accidents
- **claims_count**: Number of claims filed
- **driving_score**: Telematics-based driving behavior score (0-100)
- **renewed**: Whether the policy was renewed (1=Yes, 0=No)
- **fraud**: Fraud indicator (1=Fraudulent, 0=Legitimate)

### Calculated Metrics

- **Loss Ratio**: Claims Amount / Premium
- **Combined Ratio**: Loss Ratio + Expense Ratio
- **GWP**: Gross Written Premium (sum of all premiums)
- **CLV**: Customer Lifetime Value (5-year discounted)

## Models

### Retention Prediction Model

- **Algorithm**: XGBoost Classifier
- **Features**: 17 features including demographics, vehicle, policy, and behavior
- **Performance**: ROC-AUC 0.78-0.85
- **Use Case**: Identify customers at risk of churning

### Fraud Detection Model

- **Algorithm**: Hybrid ensemble (XGBoost + Isolation Forest)
- **Features**: 8 features focused on claims patterns
- **Performance**: ROC-AUC 0.82-0.90
- **Use Case**: Flag suspicious claims for investigation

### Risk Segmentation

- **Algorithm**: K-Means Clustering (4 segments)
- **Features**: 8 behavioral and policy features
- **Output**: Low/Medium/High/Very High risk categories

## Configuration

### Modifying Data Volume

Edit `utils/data_generator.py`:

```python
df = generate_motor_insurance_data(n_records=10000)  # Change 5000 to desired count
```

### Adjusting Model Parameters

Edit `utils/model_utils.py` in the respective model classes:

```python
self.model = XGBClassifier(
    n_estimators=200,  # Adjust hyperparameters
    max_depth=6,
    learning_rate=0.05
)
```

## Key Performance Indicators (KPIs)

### Financial Targets

- **Loss Ratio**: 60-65%
- **Expense Ratio**: 25-30%
- **Combined Ratio**: <100%
- **ROE**: 15%+

### Operational Targets

- **Renewal Rate**: 82-85%
- **FNOL Time**: <24 hours
- **Settlement Time**: <30 days
- **Fraud Rate**: <5%

## Troubleshooting

### Common Issues

**Issue**: Data file not found
```
Solution: Run `python utils/data_generator.py` to generate data
```

**Issue**: Module import errors
```
Solution: Ensure all dependencies are installed: `pip install -r requirements.txt`
```

**Issue**: Streamlit not found
```
Solution: Activate your virtual environment and reinstall: `pip install streamlit`
```

## Customization

### Adding New Pages

1. Create a new file in `pages/` folder
2. Name it with a number prefix: `6_🔍_Your_Page.py`
3. Use the same structure as existing pages
4. The page will automatically appear in the sidebar

### Modifying Visualizations

Edit `utils/viz_utils.py` to customize charts or add new visualization functions.

### Extending Models

Add new model classes to `utils/model_utils.py` following the existing patterns.

## Performance Optimization

- Data is cached using `@st.cache_data` decorator
- Models are cached using `@st.cache_resource` decorator
- Large datasets can be loaded once and reused across pages

## Deployment

### Local Deployment

Already covered in the Usage section above.

### Cloud Deployment (Streamlit Cloud)

1. Push code to GitHub repository
2. Connect to Streamlit Cloud (https://share.streamlit.io)
3. Deploy from GitHub repository
4. Set Python version to 3.8+ in settings

### Docker Deployment

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "Home.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

## License

This project is provided as-is for educational and demonstration purposes.

## Support

For issues or questions:
- Check the Troubleshooting section
- Review Streamlit documentation: https://docs.streamlit.io
- Check data science best practices for insurance analytics

## Acknowledgments

- Built with Streamlit
- Visualizations powered by Plotly
- ML models using scikit-learn and XGBoost
- Synthetic data generation inspired by Indian motor insurance market patterns

## Version History

- **v1.0.0** - Initial release with all core features
  - 5 dashboard pages
  - 3 ML models (retention, fraud, segmentation)
  - Comprehensive visualizations
  - Synthetic data generator

---

**Motor Insurance Analytics Dashboard** | Built for Data Science Professionals in General Insurance
