## Resume Analyzer

This project analyzes a resume and returns an ATS (Applicant Tracking System) score
based on the provided job description.

## Installation

1. Create and activate a virtual environment (recommended):

Windows PowerShell:

```
python -m venv .venv
.venv\Scripts\Activate.ps1
```

2. Install the project dependencies from the requirements file:

```
pip install -r requirment.txt
```

> Note: The requirements file is named `requirment.txt` (intentionally kept as-is).

## Run the App

This project uses Streamlit. From the `Resume_Analyzer` folder run:

```
streamlit run app.py
```

Or, if you prefer to run directly with Python for debugging, execute:

```
python app.py
```

## Usage

- Upload a resume PDF using the file uploader.
- Paste the Job Description into the text area.
- The app shows an ATS score and lists up to 20 missing keywords.

## Files of Interest

- `app.py` — Streamlit front-end (upload resume, paste JD, display results).
- `parser.py` — Extracts text from uploaded PDF resumes.
- `ats_score.py` — Calculates similarity-based ATS score.
- `analyzer.py` — Finds missing keywords from the job description.

If you'd like, I can also: fix the `requirment.txt` filename, add example screenshots, or expand the README with troubleshooting tips.

