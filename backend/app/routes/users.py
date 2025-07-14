from flask import Blueprint, request, jsonify
from ..extensions import db
from ..models.user import User
from ..models.task import Task 
from app.extensions import db, mail
from flask_mail import Message

users_bp = Blueprint("users", __name__, url_prefix="/api/users")

# GET all users
@users_bp.route("", methods=["GET"])
@users_bp.route("/", methods=["GET"])
def get_users():
    try:
        users = User.query.all()
        return jsonify([
            {"id": u.id, "name": u.name, "email": u.email}
            for u in users
        ]), 200
    except Exception as e:
        print("GET USERS ERROR:", e)
        return jsonify({"error": "Failed to fetch users", "details": str(e)}), 500

# POST new user
@users_bp.route("", methods=["POST"])
@users_bp.route("/", methods=["POST"])
def create_user():
    try:
        data = request.get_json()

        # Validate required fields
        if not data or "id" not in data or "name" not in data or "email" not in data:
            return jsonify({"error": "Missing user id, name, or email"}), 400

        user = User(
            id=data["id"],
            name=data["name"],
            email=data["email"],
            is_admin=data.get("is_admin", False)
        )

        db.session.add(user)
        db.session.commit()

        return jsonify({
            "message": "User created",
            "user": {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "is_admin": user.is_admin
            }
        }), 201

    except Exception as e:
        print("CREATE USER ERROR:", e)
        return jsonify({"error": "Failed to create user", "details": str(e)}), 500
# PUT update user
@users_bp.route("/<string:user_id>", methods=["PUT"])
def update_user(user_id):
    try:
        data = request.get_json()
        user = User.query.get(user_id)

        if not user:
            return jsonify({"error": "User not found"}), 404

        if "name" not in data or "email" not in data:
            return jsonify({"error": "Missing name or email"}), 400

        user.name = data["name"]
        user.email = data["email"]
        db.session.commit()
        return jsonify({
            "message": "User updated",
            "user": {"id": user.id, "name": user.name, "email": user.email}
        }), 200
    except Exception as e:
        print("UPDATE USER ERROR:", e)
        return jsonify({"error": "Failed to update user", "details": str(e)}), 500

# DELETE user
@users_bp.route("/<string:user_id>", methods=["DELETE"])
def delete_user(user_id):
    try:
        user = User.query.get(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404

        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "User deleted", "user_id": user_id}), 200
    except Exception as e:
        print("DELETE USER ERROR:", e)
        return jsonify({"error": "Failed to delete user", "details": str(e)}), 500
    

# Login User
@users_bp.route("/login", methods=["POST"])
def login_user():
    try:
        data = request.get_json()
        email = data.get("email")
        user_id = data.get("user_id")

        if not email or not user_id:
            return jsonify({"error": "Email and User ID are required"}), 400

        user = User.query.filter_by(id=user_id, email=email).first()
        if not user:
            return jsonify({"error": "Invalid credentials"}), 401

        return jsonify({
            "message": "Login successful",
            "user": {
                "id": user.id,
                "name": user.name,
                "email": user.email
            }
        }), 200

    except Exception as e:
        print("LOGIN ERROR:", e)
        return jsonify({"error": "Login failed", "details": str(e)}), 500





@users_bp.route("/api/tasks/", methods=["POST"])
def create_task():
    try:
        data = request.get_json()
        title = data.get("title")
        description = data.get("description")
        deadline = data.get("deadline")
        user_id = data.get("user_id")

        if not all([title, deadline, user_id]):
            return jsonify({"error": "Missing title, deadline, or user_id"}), 400

        user = User.query.get(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404

        # Create task with default status
        task = Task(
            title=title,
            description=description,
            deadline=deadline,
            user_id=user_id,
            status="incomplete"  # Default status
        )

        db.session.add(task)
        db.session.commit()

        # Send email notification
        msg = Message(
            subject="New Task Assigned",
            recipients=[user.email],
            body=f"Hello {user.name},\n\nYou have been assigned a new task:\n\nTitle: {title}\nDescription: {description}\nDeadline: {deadline}\n\nPlease log in to update your progress.\n\nRegards,\nTask Manager"
        )
        mail.send(msg)

        return jsonify({"message": "Task assigned and email sent"}), 201

    except Exception as e:
        print("CREATE TASK ERROR:", e)
        return jsonify({"error": "Failed to assign task", "details": str(e)}), 500
