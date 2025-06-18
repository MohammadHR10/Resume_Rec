from llama_cpp import Llama

#llm = Llama(model_path="/Users/mohammad/Downloads/Resume_Rec/models/mistral-7b-instruct.Q4_K_M.gguf")
llm = Llama(
    model_path="/Users/mohammad/Downloads/Resume_Rec/models/mistral-7b-instruct.Q4_K_M.gguf",
    n_ctx=2048  # or 4096 if your machine handles it
)

def score_resume_against_jd(resume_text, job_description):
    resume_text = resume_text[:1500]  # Trim only resume
    prompt = f"Rate this resume for the following job:\n\n{job_description}\n\nResume:\n{resume_text}\n\nScore (0-10) and reason:"
    return llm(prompt, max_tokens=256)['choices'][0]['text']

