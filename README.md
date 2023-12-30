# Cloud Computing Assignment: Simple website to demonstrate the usage of Google app engines APIs library. 

## Languages and Tools:
<p align="left"> 
<a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a><a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a><a href="https://flask.palletsprojects.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="flask" width="40" height="40"/> </a> </a> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a>   </p>

## Overview
This Flask app is a group assignment project for the Cloud Computing course. 

## Prerequisites
Make sure you have the following installed:
- Python 3.x
- Pip (Python package installer)

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/msyaafiq/cloud-computing-assignment.git
2. **Navigate to the project directory:**
   ```bash
   cd cloud-computing-assignment
2. **Open New Window:**
   ```bash
   code .   
3. **Install Flask:**
   ```bash
   pip install Flask
4. **Run the Flask App:**
   ```bash
   python main.py
4. **Open the browser**
   Click the link with address:
   http://127.0.0.1:8000/

## Things to Take Note:

### Normal HTML:
In normal HTML, if you want to reference a static file like a CSS file, you might use a relative path:

```html
<link rel="stylesheet" type="text/css" href="/css/styles.css">
/```

**Flask App HTML (with Jinja Template Engine):**

In a Flask app with the Jinja template engine, you must use `url_for` to generate URLs dynamically. 
This is useful, for example, when you want to handle static files through Flask's routing:

```html
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/style.css') }}">


