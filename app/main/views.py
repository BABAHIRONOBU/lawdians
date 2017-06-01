from flask import render_template

from . import main


@main.route('/test')
def test_index():
    return render_template('index.html')
