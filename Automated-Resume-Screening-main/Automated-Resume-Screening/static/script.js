document.addEventListener("DOMContentLoaded", () => {
    const fileInput = document.getElementById("fileUpload");
    const label = document.querySelector(".upload-label");

    fileInput.addEventListener("change", () => {
        const fileName = fileInput.files.length > 0 ? fileInput.files[0].name : "Choose your resume dataset";
        label.textContent = fileName;
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const roleSelect = document.getElementById('role');
    const jobDescription = document.getElementById('jobDescription');
    
    const jobDescriptions = {
        'data_scientist': 'We are looking for a Data Scientist with strong experience in Python, Machine Learning, Statistical Analysis, and Data Visualization. The ideal candidate should have expertise in implementing machine learning models, conducting statistical analysis, and communicating insights effectively.',
        'software_engineer': 'We are seeking a Software Engineer with strong programming skills in multiple languages (Java, Python, C++). Experience with web development frameworks, database design, and API development is required. Knowledge of software design patterns and agile methodologies is essential.',
        'data_analyst': 'Looking for a Data Analyst with strong SQL skills, experience with data visualization tools, and proficiency in Python or R. The ideal candidate should be able to analyze complex datasets, create insightful visualizations, and communicate findings effectively.',
        'web_developer': 'We need a Web Developer with expertise in HTML, CSS, JavaScript, and modern frontend frameworks (React, Angular, or Vue.js). Experience with backend development, RESTful APIs, and database management is required.',
        'machine_learning': 'Seeking a Machine Learning Engineer with strong Python programming skills and deep understanding of ML algorithms, deep learning frameworks (TensorFlow/PyTorch), and deployment of ML models. Experience with MLOps and model optimization is a plus.',
        'custom': ''
    };

    roleSelect.addEventListener('change', function() {
        const selectedRole = this.value;
        jobDescription.value = jobDescriptions[selectedRole] || '';
        if (selectedRole === 'custom') {
            jobDescription.placeholder = 'Enter custom job description...';
            jobDescription.focus();
        }
    });
}); 