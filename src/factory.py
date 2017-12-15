from flask import Flask

from src.config import DevelopmentConfig


def create_app():
    app = Flask(__name__, static_folder="static")
    app.config.from_object(DevelopmentConfig)
    
    from src.views import photo_blueprint
    app.register_blueprint(photo_blueprint)
    
    return app
