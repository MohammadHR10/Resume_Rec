import streamlit as st
from recommender import rank_resumes
import os

st.set_page_config(page_title="Resume Recommender", layout="centered")

st.title("🔍 Resume Recommendation System")

# Sidebar for settings
st.sidebar.header("⚙️ Settings")
max_resumes = st.sidebar.slider("Max resumes to process", 1, 20, 5)

# Step 1: Upload resumes
st.header("📄 Upload Resumes (PDF)")
uploaded_files = st.file_uploader("Upload multiple resumes", type=["pdf"], accept_multiple_files=True)

# Save uploaded files
resume_dir = "data/resumes"
if uploaded_files:
    os.makedirs(resume_dir, exist_ok=True)
    st.success(f"Uploaded {len(uploaded_files)} file(s). Processing up to {max_resumes}.")
    for file in uploaded_files[:max_resumes]:  # Limit by slider
        with open(os.path.join(resume_dir, file.name), "wb") as f:
            f.write(file.getbuffer())

# Step 2: Input job description
st.header("📌 Job Description / Requirements")
job_description = st.text_area("Paste job requirements here")

# Step 3: Department filter (for future logic, customizable scoring)
department = st.selectbox("Select Department", ["Engineering", "Sales", "Marketing", "Design", "HR"])

# Step 4: Match resumes
if st.button("Match Resumes"):
    if not uploaded_files:
        st.warning("Please upload at least one resume.")
    elif not job_description.strip():
        st.warning("Please paste the job description.")
    else:
        st.subheader("🎯 Ranked Candidates")
        with st.spinner("Scoring resumes... please wait"):
            results = rank_resumes(resume_dir, job_description)
        for filename, score, reason in results:
            st.markdown(f"**{filename}** — Score: `{score}`")
            with st.expander("Reasoning"):
                st.text(reason)
