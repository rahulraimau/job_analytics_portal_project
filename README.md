# 🔍 Job Analytics & Role Prediction Portal

A complete data science project that analyzes job market trends and predicts job roles based on skills and descriptions.

![Streamlit](https://img.shields.io/badge/Deployed%20on-Streamlit-0099ff?logo=streamlit)

---
Dataset-https://www.kaggle.com/datasets/ravindrasinghrana/job-description-dataset
## 📊 Features

- Job role prediction from skills using ML
- TF-IDF vectorization of text data
- Role-based filtering & visualization (Time-filtered charts)
- Company clustering and salary insights
- Streamlit dashboard with upload + filtering
- Resume parsing + matching (optional)

---

## 🚀 Live Demo

https://jobanalyticsappproject-3g6jw7wpfjsch4d8d5hjup.streamlit.app/


https://jobanalytics1.netlify.app/





🔗 [Streamlit App](https://job-analytics.streamlit.app) *(Update link if different)*

---

## 🛠️ Tech Stack

- Python (Pandas, Scikit-learn, Matplotlib, Seaborn)
- Streamlit for UI
- GitHub for version control
- Netlify (optional frontend)
- Tableau (.twbx for dashboard visuals)

---

## 📁 Project Structure

├── app.py # Streamlit App
├── model.pkl # Trained ML model
├── requirements.txt # Python dependencies
├── data/ # Input datasets
├── charts/ # Exported graphs
├── Book1.twbx # Tableau Workbook (visuals)
└── README.md # Project README

yaml
Copy
Edit

---

## 💡 Sample Usage

```bash
streamlit run app.py
📦 Requirements
bash
Copy
Edit
pip install -r requirements.txt
📜 License
MIT © [Your Name]

sql
Copy
Edit

Then commit and push:

```bash
git add README.md
git commit -m "Added README.md"
git push origin main
🟢 2. Add Streamlit Deploy Badge
Add this line inside the README under the title or “Live Demo” section:

markdown
Copy
Edit
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://job-analytics.streamlit.app)
Replace https://job-analytics.streamlit.app with your real deployed app link.

🚀 3. Deploy on Streamlit Cloud
Step-by-step:
Go to: https://streamlit.io/cloud

Click “New app”

Connect your GitHub → choose job_analytics_portal_project

Set:

Branch: main

Main file path: app.py

Click Deploy

It will automatically install from requirements.txt.

🌐 4. (Optional) Connect Frontend to Netlify
If you have a React frontend (or visualization dashboard) hosted on Netlify, connect it by:

Putting the static site files (build/, index.html) in a subfolder

Deploying using Netlify CLI

Use your dashboard as a frontend, and app.py as backend (on Render or Streamlit Cloud)

