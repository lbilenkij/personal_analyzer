from . import main
from flask import render_template


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/cats')
def cats():
    return render_template('cats.html')


@main.route('/cats/new')
def add_cats():
    return render_template('cats_new.html')


@main.route('/power')
def power():
    return render_template('power.html')


@main.route('/water')
def water():
    return render_template('water.html')


@main.route('/coal')
def coal():
    return render_template('coal.html')


@main.route('/summary')
def summary():
    return render_template('summary.html')
