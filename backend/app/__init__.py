from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_mail import Mail
from .config import Config

db = SQLAlchemy()
mail = Mail()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)

    db.init_app(app)
    mail.init_app(app)

    from .routes import auth, tasks
    app.register_blueprint(auth.bp)
    app.register_blueprint(tasks.bp)

    with app.app_context():
        db.create_all()

    return app
