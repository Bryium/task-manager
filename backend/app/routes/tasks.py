from flask import Blueprint, request, jsonify
from ..models.task import Task
from ..models.user import User
from app.extensions import db

from ..utils.email import send_task_notification
from datetime import datetime

bp = Blueprint("tasks", __name__, url_prefix="/api/tasks")

@bp.route("/", methods=["POST"])
def assign_task():
    data = request.get_json()
    title = data["title"]
    description = data.get("description", "")
    deadline = datetime.strptime(data["deadline"], "%Y-%m-%d")
    user_id = data["user_id"]

    task = Task(title=title, description=description, deadline=deadline, user_id=user_id)
    db.session.add(task)
    db.session.commit()

    user = User.query.get(user_id)
    if user:
        send_task_notification(user.email, title)

    return jsonify({"message": "Task assigned successfully"}), 201

@bp.route("/user/<int:user_id>", methods=["GET"])
def get_user_tasks(user_id):
    tasks = Task.query.filter_by(user_id=user_id).all()
    return jsonify([
        {
            "id": t.id,
            "title": t.title,
            "description": t.description,
            "status": t.status,
            "deadline": t.deadline.strftime("%Y-%m-%d"),
            "created_at": t.created_at.strftime("%Y-%m-%d")
        } for t in tasks
    ])

@bp.route("/<int:task_id>", methods=["PATCH", "PUT"])
def update_status(task_id):
    data = request.get_json()
    status = data.get("status")

    task = Task.query.get(task_id)
    if not task:
        return jsonify({"error": "Task not found"}), 404

    if status not in ["Pending", "In Progress", "Completed"]:
        return jsonify({"error": "Invalid status"}), 400

    task.status = status
    db.session.commit()
    return jsonify({"message": "Task status updated"})


@bp.route("/", methods=["GET"])
def get_all_tasks():
    tasks = Task.query.join(User).add_columns(
        Task.id,
        Task.title,
        Task.description,
        Task.status,
        Task.deadline,
        User.name,
        User.email
    ).all()

    result = []
    for task, id_, title, description, status, deadline, name, email in tasks:
        result.append({
            "id": id_,
            "title": title,
            "description": description,
            "status": status,
            "deadline": deadline.strftime("%Y-%m-%d") if deadline else None,
            "user": {
                "name": name,
                "email": email
            }
        })

    return jsonify(result)




