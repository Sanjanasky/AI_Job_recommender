import streamlit as st
from src.helper import extract_text_from_pdf, ask_openai
from src.job_api import fetch_indeed_jobs, fetch_naukri_jobs

st.set_page_config(page_title="AI Job Recommender", layout="wide")
st.title("📄 AI Job Recommender")
st.markdown(
    "Upload your resume and get job recommendations based on your skills and experience from **Indeed & Naukri**."
)

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file:
    with st.spinner("📄 Extracting text from your resume..."):
        resume_text = extract_text_from_pdf(uploaded_file)

    with st.spinner("🧠 Summarizing your resume..."):
        summary = ask_openai(
            f"Summarize this resume highlighting skills, education, and experience:\n\n{resume_text}",
            max_tokens=400
        )

    with st.spinner("🛠️ Finding skill gaps..."):
        gaps = ask_openai(
            f"Analyze this resume and highlight missing skills, certifications, and experiences:\n\n{resume_text}",
            max_tokens=300
        )

    with st.spinner("🚀 Creating future roadmap..."):
        roadmap = ask_openai(
            f"Based on this resume, suggest a future roadmap (skills, certifications, exposure):\n\n{resume_text}",
            max_tokens=300
        )

    # -------- DISPLAY AI RESULTS --------
    st.markdown("---")
    st.header("📑 Resume Summary")
    st.markdown(
        f"<div style='background:#000;padding:15px;border-radius:10px;color:white'>{summary}</div>",
        unsafe_allow_html=True,
    )

    st.header("🛠️ Skill Gaps")
    st.markdown(
        f"<div style='background:#000;padding:15px;border-radius:10px;color:white'>{gaps}</div>",
        unsafe_allow_html=True,
    )

    st.header("🚀 Future Roadmap")
    st.markdown(
        f"<div style='background:#000;padding:15px;border-radius:10px;color:white'>{roadmap}</div>",
        unsafe_allow_html=True,
    )

    st.success("✅ Resume analysis completed")

    # -------- JOB RECOMMENDATIONS --------
    if st.button("🔎 Get Job Recommendations"):
        with st.spinner("🔍 Generating job search keywords..."):
            keywords = ask_openai(
                f"Based on this resume summary, suggest best job titles for job search. "
                f"Return comma-separated keywords only.\n\nSummary:\n{summary}",
                max_tokens=80
            )

            search_keywords = keywords.replace("\n", "").strip()

        st.info(f"**Job Search Keywords:** {search_keywords}")

        with st.spinner("💼 Fetching jobs from Indeed & Naukri..."):
            indeed_jobs = fetch_indeed_jobs(search_keywords, rows=40)
            naukri_jobs = fetch_naukri_jobs(search_keywords, rows=40)

        # -------- INDEED JOBS --------
        st.markdown("---")
        st.header("💼 Indeed Jobs")

        if indeed_jobs:
            for job in indeed_jobs[:10]:
                st.markdown(f"**{job.get('position')}**")
                st.markdown(f"🏢 {job.get('company')}")
                st.markdown(f"📍 {job.get('location')}")
                st.markdown(f"🔗 [View Job]({job.get('url')})")
                st.markdown("---")
        else:
            st.warning("No Indeed jobs found.")

        # -------- NAUKRI JOBS --------
        st.markdown("---")
        st.header("💼 Naukri Jobs (India)")

        if naukri_jobs:
            for job in naukri_jobs[:10]:
                st.markdown(f"**{job.get('title')}**")
                st.markdown(f"🏢 {job.get('companyName')}")
                st.markdown(f"📍 {job.get('location')}")
                st.markdown(f"🔗 [View Job]({job.get('url')})")
                st.markdown("---")
        else:
            st.warning("No Naukri jobs found.")
