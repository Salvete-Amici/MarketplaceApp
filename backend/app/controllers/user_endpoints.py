from flask import Blueprint

user_endpoints_blueprint = Blueprint("user_endpoints", __name__)

@user_endpoints_blueprint.route("/api/users/")
def users():
  return ""