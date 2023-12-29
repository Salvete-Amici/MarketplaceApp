from flask import Blueprint

message_endpoints_blueprint = Blueprint("message_endpoints", __name__)

@message_endpoints_blueprint.route("/api/messages/")
def message():
  return ""