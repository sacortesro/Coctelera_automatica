"""Initialize app."""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mqtt import Mqtt

# Global variables
db = SQLAlchemy()
login_manager=LoginManager()
mqtt = Mqtt()

def create_app():
    """Initialize the core aplication."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    
    #inicializar plugins
    db.init_app(app)
    login_manager.init_app(app)
    
    #config mqtt
    app.config['MQTT_BROKER_URL'] = '192.168.0.19'
    app.config['MQTT_BROKER_PORT'] = 1883
    app.config['MQTT_USERNAME'] = ''
    app.config['MQTT_PASSWORD'] = ''
    app.config['MQTT_REFRESH_TIME'] = 1.0  # refresh time in seconds
    mqtt = Mqtt(app)
    mqtt.publish('server', 'Servidor Iniciado')

    with app.app_context():
        # Import parts of our flask_wtforms_tutorial
        from . import routes
        from .home import home
        from .coctail import coctail
        
        # Create sql tables
        db.create_all()

        #resgister blueprints
        app.register_blueprint(home.home_coctail)
        app.register_blueprint(coctail.coctail_bp)

        
        return app
