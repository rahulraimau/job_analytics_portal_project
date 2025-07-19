Job Analytics and Role Prediction Portal – Project Report
📌 Project Overview
The Job Analytics and Role Prediction Portal is an intelligent dashboard and predictive system designed to help users gain meaningful insights from job market data and forecast suitable roles based on text input such as skills and job descriptions.

It combines interactive visualizations with machine learning models to power both exploratory analysis and job role prediction, tailored for students, job seekers, and HR analysts.

📊 Key Functionalities
1. Interactive Dashboard (via Streamlit)
Filters: Role, Job Title, Country, Gender, Work Type, Salary Range, Company Size, Date

Charts:

Top 5 Roles for Interns (Account Director, Company < 2M, Year 2023)

Top 10 Companies Hiring Data Engineers (non-Asian countries, female-preferred, time-filtered)

Company Size vs. Company (Mechanical Engineers, Salary > $50K, Male, Asia, 3–5 PM IST)

2. Text-Based Role Prediction (ML Model)
Uses TfidfVectorizer to extract features from combined Skills and Job Description fields.

Logistic Regression classifier trained to predict the most probable job role.

Achieved 100% Accuracy on a test set with 15,983 entries:

java
Copy
Edit
Wedding Consultant: F1 Score = 1.00
Wireless Network Engineer: F1 Score = 1.00
...
3. Resume Upload and Role Matching
Users can upload a resume (text extracted using PyMuPDF or pdfminer).

Role prediction based on extracted text is displayed alongside top matching companies.

🔎 Insights Discovered
Wedding-related roles (Planner, Consultant, Coordinator) had consistently high match and clarity in skill-job alignment.

Internships for Account Directors in companies with size < 2M were concentrated in a few sectors in 2023.

Data Engineering roles with job title Data Scientist skewed towards female-preferred postings in European and American companies.

Mechanical Engineering jobs with salary > $50K and >5 years of experience were majorly full-time/part-time in Asia.

🤖 Machine Learning Summary
Model Used: Logistic Regression

Vectorization: TF-IDF with 1000 features

Target: Role (LabelEncoded)

Accuracy: 100%

Files Saved: logistic_model.pkl, tfidf_vectorizer.pkl, label_encoder.pkl

Prediction Endpoint: Integrated into app.py via Streamlit

📁 Files & Technologies
Frontend: jobanalytics1.netlify.app

Backend: Streamlit + Joblib + Hugging Face (for optional LLM role summaries)

Data Source: Cleaned .xlsx with job descriptions, roles, skills, salary, company info

Charts: Altair, Matplotlib, Plotly

Modeling: Scikit-learn

📝 Conclusion
This project demonstrates how natural language processing, machine learning, and interactive dashboards can work together to help users explore the job landscape and receive intelligent career guidance in real-time.

The architecture is scalable and can integrate resume parsing, job matching engines, LLM-powered profile summaries, and feedback-based recommendation loops in the future.

