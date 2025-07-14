# app/__init__.py
from flask import Flask
from flask_cors import CORS
from .config import Config
from .extensions import db, migrate, mail  

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)

    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    # Import blueprints after extensions are initialized
    from .routes.auth import bp as auth_bp
    from .routes.tasks import bp as tasks_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)

    return app  
