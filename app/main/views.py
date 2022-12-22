import jinja2
from flask import render_template

from . import main


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/services')
def services():
    return render_template('services.html')


