# cloud-computing-assignment
using FLASK (python) as the middleware

# Simple website to demonstrate the usage of Google app engines APIs library. Cloud Computing Assignment

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


<link rel="stylesheet" type="text/css" href="/css/styles.css">

##**Flask App HTML (with Jinja Template Engine):**

In a Flask app with the Jinja template engine, you must use `url_for` to generate URLs dynamically. This is useful, for example, when you want to handle static files through Flask's routing:

```html
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/style.css') }}">


