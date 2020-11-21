
#  """App configuration."""
# from os import 
# tenv import load_dotenv

# # Load variables from .env
# basedir = path.abspath(path.dirname(__file__))
# load_dotenv(path.join(basedir, ".env"))


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