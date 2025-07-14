from flask import Flask
from flask_cors import CORS
from .config import Config
from .routes.users import users_bp
from .extensions import db, migrate, mail

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app, resources={r"/api/*": {"origins": "*"}})

    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    
    from .routes.tasks import bp as tasks_bp
    from .routes.users import users_bp
    from .routes.auth import auth_bp

    # ✅ Use URL prefixes
    app.register_blueprint(tasks_bp, url_prefix="/api/tasks")
    app.register_blueprint(users_bp, url_prefix="/api/users")
    app.register_blueprint(auth_bp, url_prefix="/api/auth") 

    return app
