import os


class Config:
    SECRET_KEY = '85sR2qcp[e]xa9KIXvNDc7gdTd7bfW{4nb{hHb<RnBy3rF{2T3R(h6QnVmypBCo3u(shF45PCXsBnxpmE}4T}D[WMo'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)),
                                                          'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


config = {'development': DevelopmentConfig,
          'default': DevelopmentConfig}
