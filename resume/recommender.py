from resume_parser import extract_text_from_pdf
from mistral_model import score_resume_against_jd
import os

def rank_resumes(resume_folder, job_description):
    ranked = []
    for filename in os.listdir(resume_folder):
        if filename.endswith(".pdf"):
            path = os.path.join(resume_folder, filename)
            text = extract_text_from_pdf(path)
            output = score_resume_against_jd(text, job_description)
            score_line = [line for line in output.split("\n") if "Score" in line]
            score = float(score_line[0].split(":")[-1].strip()) if score_line else 0
            ranked.append((filename, score, output))
    return sorted(ranked, key=lambda x: x[1], reverse=True)
