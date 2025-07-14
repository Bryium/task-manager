from flask import Blueprint, request, jsonify
from ..models.user import User
from .. import db

bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    print("Received data:", data)

    # Validate input
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    is_admin = data.get("is_admin", False)

    if not name or not email or not password:
        return jsonify({"error": "Name, email, and password are required"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "User already exists"}), 400

    user = User(name=name, email=email, is_admin=is_admin)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201


@bp.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([
        {
            "id": u.id,
            "name": u.name,
            "email": u.email,
            "is_admin": u.is_admin
        } for u in users
    ])
