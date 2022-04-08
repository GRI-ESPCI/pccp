import os


class BaseConfig(object):

    PROJECT = "PCCP"

    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    DEBUG = False
    TESTING = True

    ADMINS = ['louisld@bloomenetwork.fr']

    SECRET_KEY = "rejhbvF?zreghéç_htYGF7FG58hzf"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    LANGUAGES = {
        'fr': 'Français'
    }

    UPLOAD_PATH = os.path.join(PROJECT_ROOT, "pccp/static/upload/")


class DefaultConfig(BaseConfig):

    DEBUG = True

    SQLALCHEMY_ECHO = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://pccp:carotte@localhost/pccp'


class TestConfig(BaseConfig):
    TESTING = True
    CSRF_ENABLED = False
