# MagicResumeBuilder

**MagicResumeBuilder** is a simple resume builder in Python using Flask. The program allows users to create and customize resumes by selecting and filling in different sections through a web interface.

## Description

MagicResumeBuilder allows users to create professional resumes with an intuitive graphical interface. This tool provides the ability to:
- Choose from various resume sections (work experience, education, skills, projects, etc.)
- Easily input and edit data in each section
- Export resumes in popular formats (e.g., PDF or DOCX)

## Features
- Color selection
- Add new sections
- Support for different resume types
- Easy export options

## To-Do
- Implement color selection
- Add more sections
- Add support for different resume types
- And more...

---

# Resume Builder - Step-by-Step Guide

This guide will help you download, install, and run the Resume Builder web application.

## Step 1: Install Required Software

Before you begin, make sure you have installed the following:
- **Git** – to download the code from GitHub
- **Python** (version 3.8 or later) – to run the application

### Install Git

1. Go to the [official Git website](https://git-scm.com/)
2. Download and install the latest version (default settings are fine).
3. Verify the installation by running:

    ```bash
    git --version
    ```

   If it displays a version number, Git is installed.

### Install Python

1. Go to the [official Python website](https://www.python.org/downloads/)
2. Download and install Python 3.8 or later.
3. **Important**: Check the box "Add Python to PATH" during installation!
4. Verify the installation by running:

    ```bash
    python --version
    ```

   or

    ```bash
    python3 --version
    ```

   If a Python version appears, the installation is successful.

---

## Step 2: Download the Code from GitHub

1. Open **Command Prompt** (Windows) or **Terminal** (Mac/Linux).
2. Navigate to the folder where you want to download the project (e.g., Documents):

    ```bash
    cd ~/Documents
    ```

3. Clone the repository from GitHub (replace `your_repo_url` with the actual repository URL):

    ```bash
    git clone your_repo_url
    ```

   Example:

    ```bash
    git clone https://github.com/yourusername/resume-builder.git
    ```

4. Move into the project folder:

    ```bash
    cd resume-builder
    ```

---

## Step 3: Install Dependencies

(Optional but recommended) Create a virtual environment:

  ```
    python -m venv venv
  ```

or (if using Python 3):

python3 -m venv venv
Activate the virtual environment:

Windows:
  ```
    venv\Scripts\activate
  ```

Mac/Linux:
  ```
    source venv/bin/activate
  ```

Install required libraries:
  ```
  pip install -r requirements.txt
  ```

If the installation is successful, everything is ready 

## Step 4: Start the Application

Run the server:
  ```
  python app.py
  ```
or (if using Python 3):
  ```
  python3 app.py
  ```

You should see a message like this in the terminal:
Running on http://127.0.0.1:5000/
Open your browser and go to:
  ```
  http://127.0.0.1:5000/
  ```

The application is now running! 

## Step 5: Using the Resume Builder

* Fill out the resume form (Step 1)
* Review and edit the data (Step 2)
* If everything looks good, click "Finalize"
* If you need to make changes, click "Edit"
* Finalized resume (Step 3)
* You can now print or save it as a PDF

## Step 6: Stop the Application

To stop the server, go to the terminal where it is running.
Press Ctrl + C to terminate the process.
The application will stop running.

If you encounter dependency issues:

  ```
  pip install --upgrade pip
  pip install -r requirements.txt
  ```
Troubleshooting

"python not found" error – Check if Python is installed and added to PATH 
"Flask not found" error – Ensure dependencies are installed (pip install -r requirements.txt) 
"Permission denied" error (Mac/Linux) – Try running with sudo:
sudo python3 app.py

