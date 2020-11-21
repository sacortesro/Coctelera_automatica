"""Initialize app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Global variables
db = SQLAlchemy()

def create_app():
    """Initialize the core aplication."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    
    #inicializa la base de datos
    # db.init_app(app)

    with app.app_context():
        # Import parts of our flask_wtforms_tutorial
        from . import routes
        from .home import home
        from .coctail import coctail

        #resgister blueprints
        app.register_blueprint(home.home_coctail)
        app.register_blueprint(coctail.coctail_bp)


        return app