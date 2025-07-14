from flask_mail import Message
from .. import mail
from flask import current_app

def send_task_notification(email, task_title):
    msg = Message("New Task Assigned",
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[email])
    msg.body = f"You have been assigned a new task: {task_title}"
    mail.send(msg)
