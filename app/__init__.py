from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import os

bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config[
        'SECRET_KEY'] = '85sR2qcp[e]xa9KIXvNDc7gdTd7bfW{4nb{hHb<RnBy3rF{2T3R(h6QnVmypBCo3u(shF45PCXsBnxpmE}4T}D[WMo'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                                                        'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # app.config.from_object(config[config_name])
    # config[config_name].init_app(app)

    bootstrap.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
