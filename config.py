
#  """App configuration."""
from os import environ,getcwd,path
from dotenv import load_dotenv


# Configuration .env
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

# Esto ya ni me acuerdo pa que sirve
file_path = path.abspath(getcwd())+"/test2.db"

class Config:
    """Setting confg"""

    # General Config
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_APP = environ.get('FLASK_APP')
    FLASK_ENV = environ.get('FLASK_ENV')
    TESTING = True
    DEBUG = True

    # Static Assets
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"

    # Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+file_path
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    