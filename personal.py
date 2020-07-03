# from flask import Flask, request, abort, render_template
# import os
# from flask_bootstrap import Bootstrap
# from flask_sqlalchemy import SQLAlchemy
#
# app = Flask(__name__)
# app.config['SECRET_KEY'] = '85sR2qcp[e]xa9KIXvNDc7gdTd7bfW{4nb{hHb<RnBy3rF{2T3R(h6QnVmypBCo3u(shF45PCXsBnxpmE}4T}D[WMo'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)),
#                                                                     'data.sqlite')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)
#
# bootstarp = Bootstrap(app)
#

# @app.route('/')
# def index():
#     return render_template('index.html')
#
#
# @app.route('/cats')
# def cats():
#     return render_template('cats.html')
#
#
# @app.route('/cats/new')
# def add_cats():
#     return render_template('cats_new.html')
#
#
# @app.route('/power')
# def power():
#     return render_template('power.html')
#
#
# @app.route('/water')
# def water():
#     return render_template('water.html')
#
#
# @app.route('/coal')
# def coal():
#     return render_template('coal.html')
#
#
# @app.route('/summary')
# def summary():
#     return render_template('summary.html')

from app import create_app, db

app = create_app('default')

@app.shell_context_processor
def make_shell_context():
    return dict(db=db)

if __name__ == '__main__':
    app.run()
