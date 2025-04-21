import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import os

def generate_model():
    # Create model directory if it doesn't exist
    if not os.path.exists('model'):
        os.makedirs('model')
    
    # Load the resume dataset
    df = pd.read_excel('UpdatedResumeDataSet.xlsx')
    
    # Preprocess the resumes
    df['cleaned_resume'] = df['Resume'].str.lower()
    df['cleaned_resume'] = df['cleaned_resume'].str.replace(r'[^a-zA-Z\s]', '')
    
    # Create and fit the vectorizer
    vectorizer = TfidfVectorizer(max_features=5000)
    vectorizer.fit(df['cleaned_resume'])
    
    # Save the vectorizer
    with open('model/vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)
    
    # Save the resume data
    with open('model/resume_data.pkl', 'wb') as f:
        pickle.dump(df, f)
    
    print("✅ Model files generated successfully!")

if __name__ == '__main__':
    generate_model() 