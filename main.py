import os
from flask import Blueprint, render_template

from flask import Flask

# This is the file of middleware

app = Flask(__name__)
app.secret_key = "hello"

# Define a Blueprint for your views
views = Blueprint("views", __name__)


@views.route('/')
def index():
    # Replace 'place_api.html' with the actual template file for the Place API
    return render_template('index.html')


@views.route('/place-api')
def place_api():
    # Replace 'place_api.html' with the actual template file for the Place API
    return render_template('place-api.html')


@views.route('/calendar-api')
def calendar_api():
    # Replace 'calendar_api.html' with the actual template file for the Calendar API
    return render_template('calendar-api.html')


@views.route('/youtube-data-api')
def youtube_data_api():
    # Replace 'youtube_data_api.html' with the actual template file for the YouTube Data API
    return render_template('youtube-data-api.html')


@views.route('/openweather-api')
def openweather_api():
    # Replace 'openweather_api.html' with the actual template file for the OpenWeather API
    return render_template('openweather-api.html')


@views.route('/aleps-api')
def aleps_api():
    # Replace 'aleps_api.html' with the actual template file for Alep's API
    return render_template('aleps-api.html')


app.register_blueprint(views)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# Register the Blueprint
app.register_blueprint(views, name='my_views')

app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 8000)), debug=True)
