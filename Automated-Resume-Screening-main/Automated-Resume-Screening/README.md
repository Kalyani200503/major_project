# Automated Resume Screening

A Flask-based web application for automated resume screening using machine learning.

## Features

- Upload resume datasets (CSV/XLSX format)
- Select predefined job roles or enter custom job descriptions
- Automatic job description suggestions based on role
- ATS (Applicant Tracking System) score calculation
- Candidate ranking based on resume-job description match
- Modern, responsive UI

## Installation

1. Clone this repository
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:
   ```bash
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

3. Upload your resume dataset (CSV or XLSX format)
4. Select a role or enter a custom job description
5. Click "Analyze" to process the resumes
6. View the results showing candidate rankings and ATS scores

## Requirements

- Python 3.6+
- Flask
- scikit-learn
- pandas
- openpyxl

## File Structure

```
Automated-Resume-Screening/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── static/
│   ├── style.css         # CSS styles
│   └── script.js         # JavaScript functionality
├── templates/
│   └── index.html        # HTML template
└── model/                # Model files
    ├── vectorizer.pkl    # Trained vectorizer
    └── resume_data.pkl   # Resume data
```

## Notes

- The application processes up to 10 resumes at a time
- Make sure your resume dataset has a column named "Resume"
- ATS scores are calculated using cosine similarity
- Results are sorted by ATS score in descending order 