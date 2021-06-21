import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = True
    HOST = "0.0.0.0"
    PORT = 8588
    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(64)
    CELERY_RESULT_BACKEND = "rpc://"
    CELERY_BROKER_URL = "redis://localhost:6379/0"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class DevelopmentConfig(Config):
    ENV = "development"
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + basedir + "/db.sqlite3"


config = {
    "production": ProductionConfig(), 
    "development": DevelopmentConfig()
}