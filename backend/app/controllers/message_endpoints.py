from flask import Blueprint, request, jsonify
from ..services.message_services import MessageService
from . import success_helper, failure_helper

message_endpoints_blueprint = Blueprint("message_endpoints", __name__)

@message_endpoints_blueprint.route("/api/messages/", methods = ["POST"])
def send_message():
  data = request.json
  sender = data.get("sender")
  receiver = data.get("receiver")
  text = data.get("text")
  if sender is None or receiver is None or text is None:
    return failure_helper("Missing Information", 400)
  serialized_message = MessageService.send_message(sender, receiver, text)
  return success_helper(serialized_message, 201)

@message_endpoints_blueprint.route("/api/messages/<int:message_id>/")
def check_message(message_id):
  message = MessageService.check_message(message_id)
  if message is None:
    return failure_helper("Message Not Found", 404)
  return success_helper(message, 200)

@message_endpoints_blueprint.route("/api/messages/<int:receiver_id>/")
def view_all_messages():
  data = request.json
  receiver = data.get("receiver")
  if not receiver:
    return failure_helper("Receiver ID Not Supplied", 400)
  messages = MessageService.get_all_messages(receiver)
  return success_helper(jsonify(messages), 200)