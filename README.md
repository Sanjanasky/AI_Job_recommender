🚀 AI Job Recommender System

The AI Job Recommender System is a Python-based project that fetches and aggregates job listings from Indeed and Naukri based on user-defined keywords.
It is designed with a modular backend architecture, making it easy to extend into analytics, AI-based recommendations, or a full web application.

📌 Key Features

🔍 Job search using keywords (e.g., Data Analyst, Python Developer)

🌍 Supports Indian job market (Indeed & Naukri)

🧩 Modular and reusable Python codebase

🔐 Secure API key handling using environment variables

⚡ Easy to extend with AI/ML or UI (Streamlit / FastAPI)

🏗️ Project Architecture
User Input (Keywords)
        ↓
Job Fetching Layer
(Indeed API | Naukri API)
        ↓
Job Data Processing
        ↓
Unified Job Results

📂 Project Structure
Job_Recommendation/
│
├── src/
│   ├── job_api.py        # Functions to fetch jobs from Indeed & Naukri
│   └── __init__.py
│
├── .env.example          # Sample environment variables
├── .gitignore
├── requirements.txt
├── main.py               # Entry point / testing script
└── README.md

🛠️ Tech Stack

Language: Python 3.10+

APIs: Indeed, Naukri

HTTP Requests: requests / httpx

Environment Management: python-dotenv

Version Control: Git & GitHub

🔑 Environment Setup

Create a .env file in the root directory:

APIFY_API_TOKEN=your_apify_token_here
OPENAI_API_KEY=your_openai_key_optional


⚠️ .env is intentionally ignored by Git for security reasons.

📦 Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/Sanjanasky/AI_Job_recommender.git
cd AI_Job_recommender

2️⃣ Create Virtual Environment
python -m venv .venv
source .venv/Scripts/activate   # Windows Git Bash

3️⃣ Install Dependencies
pip install -r requirements.txt

▶️ Usage Example
from src.job_api import fetch_indeed_jobs, fetch_naukri_jobs

indeed_jobs = fetch_indeed_jobs(
    search_query="Data Analyst",
    location="India",
    rows=30
)

naukri_jobs = fetch_naukri_jobs(
    search_query="Python Developer",
    rows=30
)


Each function returns structured job data including:

Job Title

Company Name

Location

Job URL

📈 Future Enhancements

Resume-based job recommendations

Skill gap analysis

AI-powered job ranking

Streamlit or FastAPI frontend

Database integration (PostgreSQL / MongoDB)

💡 Why This Project Matters

Solves a real-world job search problem

Demonstrates API integration & backend skills

Shows clean, scalable Python design

Can be extended into AI / Data Analytics projects

👩‍💻 Author

Sanjana Kumari Yadav
Aspiring Data Analyst | Python Developer
