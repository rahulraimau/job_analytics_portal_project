import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from transformers import pipeline
from datetime import datetime
import pytz
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder

# Get current time in IST (India Standard Time)
def is_between_3pm_to_5pm_ist():
    ist = pytz.timezone("Asia/Kolkata")
    now = datetime.now(ist)
    return now.hour >= 15 and now.hour < 17

# Load dataset
df = pd.read_csv("job_dataset_cleaned.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Parse numeric fields
df["salary_cleaned"] = df["salary_range"].astype(str).str.extract(r"(\d+)").astype(float)
df["experience_cleaned"] = df["experience"].astype(str).str.extract(r"(\d+)").astype(float)

# Title
st.set_page_config(page_title="Job Analytics Dashboard", layout="wide")
st.title("📊 Job Analytics Dashboard")

# Sidebar Filters
st.sidebar.header("🔎 Filter Jobs")
country_filter = st.sidebar.multiselect("Country", options=df["country"].dropna().unique())
role_filter = st.sidebar.multiselect("Role", options=df["role"].dropna().unique())
exp_filter = st.sidebar.slider("Min Experience", 0, 20, 0)

# Apply Filters
filtered_df = df.copy()
if country_filter:
    filtered_df = filtered_df[filtered_df["country"].isin(country_filter)]
if role_filter:
    filtered_df = filtered_df[filtered_df["role"].isin(role_filter)]
filtered_df = filtered_df[filtered_df["experience_cleaned"] >= exp_filter]

# Summary Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Max Salary", f"${filtered_df['salary_cleaned'].max():,.0f}")
col2.metric("Min Experience", f"{filtered_df['experience_cleaned'].min():.0f} years")
col3.metric("Total Jobs", len(filtered_df))

# Show Data
st.subheader("📁 Filtered Jobs Data")
st.dataframe(filtered_df.head(20), use_container_width=True)

# ================================
# Static Charts
# ================================
st.subheader("📈 Static Visualizations")

st.image("static_graphs/salary_distribution.png", caption="Salary Distribution", use_column_width=True)
st.image("static_graphs/experience_boxplot.png", caption="Experience Boxplot", use_column_width=True)
st.image("static_graphs/top_companies.png", caption="Top Hiring Companies", use_column_width=True)
st.image("static_graphs/top_roles.png", caption="Most Frequent Roles", use_column_width=True)
st.image("static_graphs/work_type_distribution.png", caption="Work Type Distribution", use_column_width=True)

# ================================
# Problem 1: Top 5 Roles in 2023
# ================================
st.subheader("📊 Problem 1: Top 5 Roles in 2023 (Intern, Account Director)")

chart1_df = df.copy()
chart1_df['job_posting_date'] = pd.to_datetime(chart1_df['job_posting_date'], errors='coerce')
chart1_df = chart1_df[
    (chart1_df['job_posting_date'].dt.year == 2023) &
    (chart1_df['work_type'].str.lower() == 'intern') &
    (chart1_df['job_title'].str.lower() == 'account director') &
    (chart1_df['company_size'].fillna(0) < 2_000_000)
]

top_roles = chart1_df['role'].value_counts().head(5)
if not top_roles.empty:
    st.bar_chart(top_roles)
else:
    st.warning("No data available for the specified criteria.")

# ================================
# Problem 2: Top 10 Companies (3-5PM IST only)
# ================================
if is_between_3pm_to_5pm_ist():
    st.subheader("🏢 Problem 2: Top 10 Companies with Data Engineers (Non-Asian, Female Preference)")

    chart2_df = df.copy()
    chart2_df['job_posting_date'] = pd.to_datetime(chart2_df['job_posting_date'], errors='coerce')
    asian_countries = ['India', 'China', 'Japan', 'Indonesia', 'Pakistan', 'Bangladesh', 'Vietnam', 'Thailand', 'Philippines', 'Malaysia']

    if 'gender_preference' not in chart2_df.columns:
        chart2_df['gender_preference'] = ''

    if 'company' in chart2_df.columns:
        chart2_df['company_name'] = chart2_df['company']
    elif 'company_name' not in chart2_df.columns:
        chart2_df['company_name'] = "Unknown"

    chart2_df = chart2_df[
        (chart2_df['role'].str.lower() == 'data engineer') &
        (chart2_df['job_title'].str.lower() == 'data scientist') &
        (~chart2_df['country'].isin(asian_countries)) &
        (~chart2_df['country'].str.startswith('C')) &
        (chart2_df['latitude'].fillna(999) > 10) &
        (chart2_df['gender_preference'].str.lower() == 'female') &
        (chart2_df['qualification'].str.lower() == 'b.tech') &
        (chart2_df['job_posting_date'] >= '2023-01-01') &
        (chart2_df['job_posting_date'] <= '2023-06-01')
    ]

    top_companies = chart2_df['company_name'].value_counts().head(10)
    if not top_companies.empty:
        st.bar_chart(top_companies)
    else:
        st.warning("No data available for the specified criteria.")
else:
    st.subheader("🏢 Problem 2: Hidden (only visible from 3PM to 5PM IST)")
    st.info("⏰ This chart is visible only between 3 PM and 5 PM IST.")

# ================================
# Problem 3: Company Size vs Company (3-5PM IST only)
# ================================
if is_between_3pm_to_5pm_ist():
    st.subheader("🏗️ Problem 3: Company Size for Mechanical Engineer (Asian, Male)")

    chart3_df = df.copy()
    if 'gender_preference' not in chart3_df.columns:
        chart3_df['gender_preference'] = ''
    if 'applied_platform' not in chart3_df.columns:
        chart3_df['applied_platform'] = ''

    asian = ['India', 'China', 'Japan', 'Indonesia', 'Pakistan', 'Bangladesh', 'Vietnam', 'Thailand', 'Philippines', 'Malaysia']
    chart3_df = chart3_df[
        (chart3_df['company_size'].fillna(999999999) < 50000) &
        (chart3_df['job_title'].str.lower() == 'mechanical engineer') &
        (chart3_df['experience_cleaned'] > 5) &
        (chart3_df['country'].isin(asian)) &
        (chart3_df['salary_cleaned'] > 50000) &
        (chart3_df['work_type'].str.lower().isin(['part time', 'full time'])) &
        (chart3_df['gender_preference'].str.lower() == 'male') &
        (chart3_df['applied_platform'].str.lower() == 'idealist')
    ]

    chart3_grouped = chart3_df.groupby('company')['company_size'].mean().sort_values(ascending=False).head(10)
    if not chart3_grouped.empty:
        st.bar_chart(chart3_grouped)
    else:
        st.warning("No data available for the specified criteria.")
else:
    st.subheader("🏗️ Problem 3: Hidden (only visible from 3PM to 5PM IST)")
    st.info("⏰ This chart is visible only between 3 PM and 5 PM IST.")

# ================================
# Hugging Face Sentiment Analysis
# ================================
st.subheader("🤗 Job Description Sentiment (Hugging Face)")
sample = filtered_df["job_description"].dropna().sample(1).values[0]
st.markdown(f"**Sample Job Description:** {sample[:500]}...")

if st.button("Run Sentiment Analysis"):
    sentiment_pipeline = pipeline("sentiment-analysis")
    result = sentiment_pipeline(sample[:512])[0]
    st.info(f"**Label:** {result['label']}, **Score:** {result['score']:.2f}")

# ================================
# Job Role Prediction (TF-IDF + LR)
# ================================
st.subheader("🧠 Predict Job Role from Skills & Description")

# Load ML model components
tfidf_vectorizer = joblib.load("tfidf_vectorizer.pkl")
logistic_model = joblib.load("logistic_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

user_input_skills = st.text_area("Enter your Skills (comma separated):", "")
user_input_description = st.text_area("Paste Job Description or Summary:", "")

if st.button("Predict Role"):
    if user_input_skills.strip() == "" or user_input_description.strip() == "":
        st.warning("Please fill in both skills and job description.")
    else:
        combined_text = user_input_skills + " " + user_input_description
        vectorized = tfidf_vectorizer.transform([combined_text])
        prediction = logistic_model.predict(vectorized)
        predicted_role = label_encoder.inverse_transform(prediction)[0]
        st.success(f"🔮 Predicted Role: **{predicted_role}**")
