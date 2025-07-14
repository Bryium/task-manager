# manage.py
from flask.cli import FlaskGroup
from app import create_app
from app.extensions import db, migrate

app = create_app()

if __name__ == "__main__":
    app.run()
