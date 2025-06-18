# Resume Recommendation System

This project is a resume recommendation system built with Python and Streamlit. It parses resumes, uses a local language model for recommendations, and provides a web interface for interaction.

---

## 📁 Project Structure

```
Resume_Rec/
│
├── resume/
│   ├── app.py                # Main Streamlit app
│   ├── recommender.py        # Recommendation logic
│   ├── resume_parser.py      # Resume parsing utilities
│   ├── mistral_model.py      # Model loading/inference code
│   └── data/                 # (Optional) Data files for testing/training
│
├── models/
│   └── mistral-7b-instruct.Q4_K_M.gguf  # (Not included in repo, see below)
│
├── requirements.txt          # Python dependencies
├── .gitignore                # Files/folders not tracked by git
└── README.md                 # Project documentation (this file)
```

---

## 🚀 Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone <your-repo-url>
   cd Resume_Rec
   ```

2. **Install dependencies:**
   It's recommended to use a virtual environment.

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. **Download the Model File:**

   - The `models/` directory is **not** included in the repository (see `.gitignore`).
   - You must manually download the required model file (e.g., `mistral-7b-instruct.Q4_K_M.gguf`) and place it in the `models/` directory.
   - **Model download instructions:**
     - Obtain the model from the official source or your organization's storage.
     - Place it at:
       ```
       Resume_Rec/models/mistral-7b-instruct.Q4_K_M.gguf
       ```
   - **Note:** The model file is large (~4GB) and is not tracked by git.

4. **Run the application:**
   ```bash
   cd resume
   streamlit run app.py
   ```

---

## 📝 Notes

- The `.gitignore` file ensures that large files (like models), virtual environments, and other unnecessary files are not tracked by git.
- Do **not** upload the `models/` directory or any large model files to GitHub.
- If you add new dependencies, update `requirements.txt` accordingly.

---

## 🤝 Contributing

1. Fork the repo and create your branch: `git checkout -b feature/your-feature`
2. Commit your changes: `git commit -am 'Add some feature'`
3. Push to the branch: `git push origin feature/your-feature`
4. Open a pull request

---

## 📬 Questions?

If you have any questions or need help setting up the project, please open an issue or contact the maintainer.
