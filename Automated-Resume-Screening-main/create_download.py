import os
import shutil
import zipfile

def create_downloadable_zip():
    # Create a temporary directory
    temp_dir = 'Resume_Screening_App'
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)
    
    # List of files and directories to include
    items_to_copy = [
        'app.py',
        'requirements.txt',
        'README.md',
        'UpdatedResumeDataSet.xlsx',
        'static',
        'templates',
        'model'
    ]
    
    # Copy files and directories
    for item in items_to_copy:
        if os.path.isfile(item):
            shutil.copy2(item, os.path.join(temp_dir, item))
        elif os.path.isdir(item):
            shutil.copytree(item, os.path.join(temp_dir, item))
    
    # Create zip file
    zip_filename = 'Resume_Screening_App.zip'
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, temp_dir)
                zipf.write(file_path, arcname)
    
    # Clean up
    shutil.rmtree(temp_dir)
    
    print(f"✅ Downloadable zip file created: {zip_filename}")
    print(f"Location: {os.path.abspath(zip_filename)}")

if __name__ == '__main__':
    create_downloadable_zip() 