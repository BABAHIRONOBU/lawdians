from flask import render_template

from . import main


@main.route('/test')
def index():
    return render_template('index.html')
