from flask_mail import Message
from app.extensions import mail

def send_task_notification(recipient_email, task_title):
    msg = Message(
        subject="New Task Assigned",
        recipients=[recipient_email],
        body=f"A new task titled '{task_title}' has been assigned to you."
    )
    msg.sender = "bryiumonyancha@gmail.com"  

    mail.send(msg)
