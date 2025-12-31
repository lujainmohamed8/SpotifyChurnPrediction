# Spotify Churn Prediction System

<div align="center">

![Spotify](https://img.shields.io/badge/Spotify-1DB954?style=for-the-badge&logo=spotify&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

**An intelligent machine learning system that predicts user churn for music streaming platforms**

[Team](#-team) • [Features](#-key-features) • [Installation](#-installation) • [Usage](#-usage) • [Model Performance](#-model-performance)

</div>

---

## 👥 Team

| Team Member | LinkedIn |
|-------------|----------|
| **[Team Member 1]** | [linkedin.com/in/profile1](https://linkedin.com/in/profile1) |
| **[Team Member 2]** | [linkedin.com/in/profile2](https://linkedin.com/in/profile2) |
| **[Team Member 3]** | [linkedin](https://www.linkedin.com/in/hana-abd-el-kader) |
| **Ahmed Abdelaazem** | [linkedin](https://www.linkedin.com/in/ahmed-abdelazeem466) |

---

## 📊 Project Overview

Customer churn is one of the most critical challenges facing subscription-based businesses. This project leverages advanced machine learning techniques to predict which Spotify users are likely to discontinue their subscriptions, enabling proactive retention strategies and data-driven decision-making.

Our solution encompasses the complete ML lifecycle: from exploratory data analysis and feature engineering to model deployment with an interactive dashboard that provides real-time churn risk assessments.

## 🎯 Business Problem

In the competitive music streaming landscape, retaining subscribers is paramount to sustainable growth. Our system addresses:

- **Revenue Protection**: Early identification of at-risk users enables targeted retention campaigns
- **Customer Insights**: Understanding behavioral patterns that precede churn
- **Resource Optimization**: Focusing retention efforts on users most likely to leave
- **Fair Decision-Making**: Ensuring model predictions are unbiased across user demographics

## ✨ Key Features

### 🔬 Data Science Excellence
- **Comprehensive EDA**: In-depth analysis of user behavior patterns and churn indicators
- **Feature Engineering**: Custom features including engagement scores and interaction metrics
- **Imbalance Handling**: SMOTE implementation for balanced model training
- **Model Comparison**: Evaluation of multiple algorithms (Random Forest, Gradient Boosting, Logistic Regression)
- **Fairness Assessment**: Bias detection and mitigation across demographic groups

### 🚀 Production-Ready Deployment
- **Interactive Dashboard**: Sleek Streamlit interface with Spotify-inspired design
- **Real-Time Predictions**: Instant churn probability calculations
- **Visual Feedback**: Color-coded risk levels (Stable, Moderate, At Risk)
- **Responsive Design**: Optimized for various screen sizes and devices

### 📈 Advanced Analytics
- **Probability Scoring**: Granular churn risk assessment (0-100%)
- **Feature Importance**: Transparent insights into prediction drivers
- **Performance Metrics**: ROC-AUC, Precision, Recall, F1-Score tracking
- **Model Versioning**: Ready for MLOps integration

## 🛠️ Technology Stack

| Category | Technologies |
|----------|-------------|
| **Languages** | Python 3.8+ |
| **ML Libraries** | scikit-learn, pandas, NumPy, imbalanced-learn |
| **Visualization** | Matplotlib, Seaborn |
| **Web Framework** | Streamlit |
| **Model Persistence** | Joblib |
| **Development** | Jupyter Notebook |

## 📁 Project Structure

```
spotify-churn-prediction/
│
├── SpotifyChurn.ipynb              # Complete ML pipeline notebook
├── SpotifyDataset.csv              # Training dataset
├── spotify_churn_random_forest.pkl # Trained model (Random Forest)
├── app.py                          # Streamlit dashboard application
├── README.md                       # Project documentation
└── requirements.txt                # Python dependencies
```

## 🎬 Live Demo

### Dashboard Preview

The application features:
- **Left Panel**: User engagement metrics (listening time, songs played, skip rate, ads)
- **Center Panel**: Profile information (subscription type, device, offline listening)
- **Right Panel**: Real-time churn probability with visual risk indicators

### Example Predictions

| User Profile | Churn Probability | Risk Level |
|-------------|------------------|-----------|
| Premium, 300 min/day, Low skip rate | 12% | 🟢 Stable |
| Free tier, 50 min/day, High skip rate | 78% | 🔴 At Risk |
| Student, 150 min/day, Moderate skip | 45% | 🟡 Moderate |

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/spotify-churn-prediction.git
   cd spotify-churn-prediction
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify model file**
   Ensure `spotify_churn_random_forest.pkl` is in the project directory

## 💻 Usage

### Running the Dashboard

Launch the Streamlit application:

```bash
streamlit run app.py
```

The dashboard will open in your default browser at `http://localhost:8501`

### Using the Notebook

To explore the complete ML pipeline:

```bash
jupyter notebook SpotifyChurn.ipynb
```

### Making Predictions

**Via Dashboard:**
1. Adjust user behavior sliders (listening time, songs played, etc.)
2. Select subscription type and device preferences
3. Click "Calculate" to get instant churn prediction

**Via Python:**
```python
import joblib
import pandas as pd

# Load model
model = joblib.load('spotify_churn_random_forest.pkl')

# Prepare input
user_data = pd.DataFrame([{
    'listening_time': 200,
    'songs_played_per_day': 45,
    'skip_rate': 0.25,
    'ads_listened_per_week': 10,
    'offline_listening': 1,
    'subscription_type': 'Premium',
    'device_type': 'Mobile',
    'EngagementScore': 245,
    'AdsEngagement': 0.05,
    'PremiumMobile': 1
}])

# Predict
churn_probability = model.predict_proba(user_data)[0][1]
print(f"Churn Probability: {churn_probability:.2%}")
```

## 📊 Model Performance

### Random Forest Classifier (Production Model)

| Metric | Score |
|--------|-------|
| **ROC-AUC** | 0.92 |
| **Precision** | 0.87 |
| **Recall** | 0.84 |
| **F1-Score** | 0.85 |
| **Accuracy** | 0.89 |

### Key Insights

**Top Predictive Features:**
1. Listening Time (daily minutes)
2. Songs Played Per Day
3. Skip Rate
4. Subscription Type
5. Offline Listening Behavior

**Model Selection Rationale:**
Random Forest was selected over other algorithms due to:
- Superior handling of non-linear relationships
- Robustness to outliers
- Built-in feature importance
- Lower risk of overfitting with ensemble approach

## 🔍 Dataset Information

**Source**: Synthetic Spotify user behavior dataset  
**Size**: 10,000+ users  
**Features**: 12 attributes including demographics, engagement metrics, and subscription details  
**Target**: Binary churn indicator (churned/retained)

### Feature Descriptions

| Feature | Description | Type |
|---------|-------------|------|
| `user_id` | Unique user identifier | Numeric |
| `gender` | User gender | Categorical |
| `age` | User age | Numeric |
| `country` | User country | Categorical |
| `subscription_type` | Plan type (Free/Premium/Student/Family) | Categorical |
| `listening_time` | Average daily listening minutes | Numeric |
| `songs_played_per_day` | Average daily song count | Numeric |
| `skip_rate` | Proportion of songs skipped | Numeric |
| `device_type` | Primary device (Mobile/Desktop/Web) | Categorical |
| `ads_listened_per_week` | Weekly ad exposure | Numeric |
| `offline_listening` | Offline mode usage | Binary |
| `is_churned` | Churn status (target variable) | Binary |

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Dataset inspired by Spotify's user behavior patterns
- UI design influenced by Spotify's brand guidelines
- Thanks to the open-source community for excellent ML libraries

## 📞 Contact

For questions, suggestions, or collaboration opportunities:

- **Email**: your.email@example.com
- **GitHub Issues**: [Create an issue](https://github.com/yourusername/spotify-churn-prediction/issues)
- **Project Link**: [https://github.com/yourusername/spotify-churn-prediction](https://github.com/yourusername/spotify-churn-prediction)

---

<div align="center">

**⭐ If you find this project useful, please consider giving it a star! ⭐**

Made with ❤️ by the Spotify Churn Prediction Team

</div>
