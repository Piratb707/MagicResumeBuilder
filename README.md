# MagicResumeBuilder

**MagicResumeBuilder** — is a simple resume builder in Python using Flask. The program allows users to create and customize resumes by selecting and filling in different sections through a web interface..

## Description

MagicResumeBuilder allows users to create professional resumes with an intuitive graphical interface. This tool provides the ability to:
- Choose from various resume sections (work experience, education, skills, projects, etc.).
- Easily input and edit data in each section.
- Export resumes in popular formats (e.g., PDF or DOCX).
  
## ToDo
- Сolor selection
- Adding sections
- Different resume types
- etc...


🚀 Resume Builder - Step-by-Step Guide

This guide will help you download, install, and run the Resume Builder web application.

📌 Step 1: Install Required Software

Before you begin, make sure you have installed:
✅ Git – to download the code from GitHub✅ Python (version 3.8 or later) – to run the application

🔹 Install Git

Go to the official Git website

Download and install the latest version (default settings are fine)

Check if Git is installed:

git --version

If it displays a version number, Git is installed ✅

🔹 Install Python

Go to the official Python website

Download and install Python 3.8 or later

Important: Check the box "Add Python to PATH" during installation!

Verify the installation by running:

python --version

or

python3 --version

If a Python version appears, the installation is successful ✅

📌 Step 2: Download the Code from GitHub

Open Command Prompt (Windows) or Terminal (Mac/Linux)

Navigate to the folder where you want to download the project (e.g., Documents):

cd ~/Documents

Clone the repository from GitHub (replace your_repo_url with the actual repository URL):

git clone your_repo_url

Example:

git clone https://github.com/yourusername/resume-builder.git

Move into the project folder:

cd resume-builder

📌 Step 3: Install Dependencies

(Optional but recommended) Create a virtual environment:

python -m venv venv

or (if using Python 3):

python3 -m venv venv

Activate the virtual environment:

Windows:

venv\Scripts\activate

Mac/Linux:

source venv/bin/activate

Install required libraries:

pip install -r requirements.txt

If the installation is successful, everything is ready ✅

📌 Step 4: Start the Application

Run the server:

python app.py

or (if using Python 3):

python3 app.py

You should see a message like this in the terminal:

Running on http://127.0.0.1:5000/

Open your browser and go to:

http://127.0.0.1:5000/

The application is now running! 🎉

📌 Step 5: Using the Resume Builder

Fill out the resume form (Step 1)

Review and edit the data (Step 2)

If everything looks good, click "Finalize"

If you need to make changes, click "Edit"

Finalized resume (Step 3)

You can now print or save it as a PDF

📌 Step 6: Stop the Application

To stop the server, go to the terminal where it is running.

Press Ctrl + C to terminate the process.

The application will stop running.

📌 Additional Commands

📌 To update the code from GitHub:

git pull origin main

📌 To install new libraries:

pip install library_name

📌 If you encounter dependency issues:

pip install --upgrade pip
pip install -r requirements.txt

📌 Troubleshooting

❌ "python not found" error – Check if Python is installed and added to PATH❌ "Flask not found" error – Ensure dependencies are installed (pip install -r requirements.txt)❌ "Permission denied" error (Mac/Linux) – Try running with sudo:

sudo python3 app.py

🎉 You're All Set! 🚀

Launch the application and create your resume in just a few clicks! 😊If you have any questions, feel free to ask!

