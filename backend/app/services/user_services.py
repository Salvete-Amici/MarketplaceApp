from ..models.user import User, Session, Wishlist
from .. import db 
from werkzeug.security import check_password_hash
from datetime import datetime, timedelta
import logging
logging.basicConfig(level=logging.INFO)

class UserService:
  
  @staticmethod
  def create_user(username, contact_info, email, password):
    """
    Register a new user.
    
    Parameters: 
    username: a string of username for application user.
    contact_info: string of contact information (details yet to be figured out).
    email: string of user email address.
    password: string to be hashed.
    
    Returns: a new user object. 
    """
    existing_user = User.query.filter_by(email = email).first()
    if existing_user:
      return None
    user = User(username = username, contact_info = contact_info, email = email)
    user.create_password(password)
    db.session.add(user)
    db.session.commit()
    wishlist = Wishlist(user_id = user.id)
    db.session.add(wishlist)
    db.session.commit()
    return user
  
  @staticmethod
  def authenticate_user(login_method, password):
    """
    Authenticate a user.
    
    Parameters: 
    login_method: the login identifier of user's choice.
    password: string of password for authentication.
    
    Returns:if successful then user and success message otherwise why error occured.
    """
    if "@" in login_method:
      user = User.query.filter_by(email = login_method).first()
    else: 
      user = User.query.filter_by(username = login_method).first()
    if user:
      if check_password_hash(user.hashed_password, password):
        return user, "success"
      else:
        return None, "password incorrect" 
    else:
      return None, "user does not exist"
  
  @staticmethod   
  def get_user_by_id(user_id):
    """
    Get the user object associated with input id.
    
    parameters:
    user_id: integer identifier for user.
    
    Returns: corresponding user object if exists, otherwise None.
    """
    user = User.query.filter_by(id=user_id).first() 
    return user 
  
  @staticmethod
  def update_user_info(user_id, new_info):
    """
    Update the profile information for associated user.
    
    parameters:
    user_id: integer identifier for user.
    new_info: a dictionary where the key is the field to be updated and val is the new info.
    
    Returns: user object with updated information, if failed to update then None.
    """
    logging.info(f"Updating user {user_id} with info {new_info}")
    user = User.query.get(user_id)
    if user:
      try:
        for key, val in new_info.items():
          if hasattr(user, key):
            logging.info(f"Setting {key} to {val}")
            setattr(user, key, val) 
        db.session.commit()
        logging.info(f"User {user_id} updated")
        return user
      except Exception as e:
        return None
    else:
      return None
  
  def delete_user(user_id):
    """
    Delete a user from database.
    
    Parameters:
    uer_id: integer identifier for user.
    
    Returns: true if user is deleted successfully, otherwise return false.
    """
    user = User.query.get(user_id)
    if user:
      db.session.delete(user)
      db.session.commit()
      return user
    else:
      return None
    
class SessionService:
  
  @staticmethod
  def create_session(user_id):
    """
    Create a new session.
    
    Parameters:
    user_id: string identifier of user.
    
    Returns: serialized new session.
    """
    session = Session(user_id = user_id)
    db.session.add(session)
    db.session.commit()
    return session.serialize()
  
  @staticmethod
  def validate_session(session_token):
    """
    Validate a session.
    
    Parameters:
    session_token: token string.
    
    Returns: true if the session status is active and has not expired, otherwise false.
    """
    session = Session.query.filter_by(session_token = session_token).first()
    return session.session_validation()
  
  @staticmethod
  def refresh_session(refresh_token):
    """
    Refresh a session.
    
    Parameters:
    refresh_token: refresh token used to obtain a new session token.
    
    Returns: serialized session after refreshing. 
    """
    session = Session.query.filter_by(refresh_token = refresh_token).first()
    if session.session_validation():
      session.session_token = Session.token_generate()
      session.refresh_token = Session.token_generate()
      session.expires_at = datetime.utcnow() - timedelta(hours = 5) + timedelta(minutes = 30)
      db.session.commit()
      return session.serialize()
    else: 
      return None 
      
  @staticmethod
  def terminate_session(session_token):
    """
    Terminate a session.
    
    Parameters:
    session_token: string of session token.
    
    Procedure no return.
    """
    session = Session.query.filter_by(session_token = session_token).first()
    db.session.delete(session)
    db.session.commit()