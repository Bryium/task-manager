# manage.py
from flask.cli import FlaskGroup
from app import create_app
import os
from app.extensions import db, migrate

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    
