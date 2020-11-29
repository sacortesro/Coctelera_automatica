
#  """App configuration."""
import os

file_path = os.path.abspath(os.getcwd())+"/test.db"

class Config:
    """Setting confg"""

    # General Config
    SECRET_KEY = "asdi89uda89sdua9sda97syd7"
    FLASK_APP = "app.py"
    FLASK_ENV = "development"
    TESTING = True
    DEBUG = True

    # Static Assets
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"

    # Database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+file_path
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
