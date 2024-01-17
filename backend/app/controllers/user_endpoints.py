from flask import Blueprint, request
from ..services.user_services import UserService
from ..services.user_services import SessionService
from . import success_helper, failure_helper

user_endpoints_blueprint = Blueprint("user_endpoints", __name__)

@user_endpoints_blueprint.route("/api/users/", methods = ["POST"])
def register_user():
  data = request.json
  username = data.get("username") 
  contact_info = data.get("contact_info")
  email = data.get("email")
  password = data.get("password")
  if username is None or contact_info is None or email is None or password is None:
    return failure_helper("Missing Information", 400)
  user = UserService.create_user(username, contact_info, email, password)
  if user is None:
    return failure_helper("User cannot be created.", 400)
  return success_helper(user.serialize(), 201)

@user_endpoints_blueprint.route("/api/users/login/", methods = ["POST"])
def login_user():
  """User login and session creation.

  Returns:
      serialized json data.
  """
  data = request.json
  print("Received data:", data)
  login_method = data.get("login_method")
  password = data.get("password")
  if login_method is None or password is None:
    return failure_helper("Missing Information", 400)
  user, message = UserService.authenticate_user(login_method, password)
  if message == "password incorrect":
    return failure_helper("Incorrect Password", 401)
  elif message == "user does not exist":
    return failure_helper("User Does Not Exist", 401)
  session_info = SessionService.create_session(user.id)
  return success_helper({"User": user.serialize(), "Session": session_info}, 200)

@user_endpoints_blueprint.route("/api/users/<int:user_id>/")
def retrieve_user(user_id):
  user = UserService.get_user_by_id(user_id)
  if user is None: 
    return failure_helper("User Not Found",404)
  return success_helper(user.serialize(), 200)

@user_endpoints_blueprint.route("/api/users/<int:user_id>/", methods = ["PUT"])
def update_user(user_id):
  new_info = request.json.get("new_info")
  updated_user = UserService.update_user_info(user_id, new_info)
  if updated_user is None:
    return failure_helper("Updated User Not Found", 404)
  return success_helper(updated_user.serialize(), 200)

@user_endpoints_blueprint.route("/api/users/<int:user_id>/", methods = ["DELETE"])
def delete_user(user_id):
  result = UserService.delete_user(user_id)
  if result is None:
    return failure_helper("User Deletion Failed", 500)
  return success_helper(result.serialize(), 200)

@user_endpoints_blueprint.route("/api/sessions/refresh/", methods = ["POST"])
def refresh_session():
  data = request.json
  refresh_token = data.get("refresh_token")
  if refresh_token is None:
    return failure_helper("Refresh Token Missing", 400)
  new_session = SessionService.refresh_session(refresh_token)
  if new_session is None:
    return failure_helper("Invalid Refresh Token", 401)
  return success_helper(new_session, 200)
    
@user_endpoints_blueprint.route("/api/users/logout/", methods = ["POST"])
def terminate_session():
  data = request.json
  session_token = data.get("session_token")
  if session_token is None:
    return failure_helper("Missing Session Token", 400)
  SessionService.terminate_session(session_token)
  return success_helper({"Message": "Logged Out"}, 200)
  
  