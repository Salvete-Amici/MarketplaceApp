from . import db # from __init__.py
from werkzeug.security import generate_password_hash
import datetime
import secrets

# User Class 
class User(db.Model):
  """
  User Model: represents a table for users in the database.
  """
  __tablename__ = "users"
  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  username = db.Column(db.String, unique = True, nullable = False)
  contact_info = db.Column(db.String)
  email = db.Column(db.String, unique = True, nullable = False)
  hashed_password = db.Column(db.String, nullable = False)
  sessions = db.relationship("Session", back_populates = "user" )
  
  def create_password(self, password):
    """
    Generate hashed password.
    """
    self.hashed_password = generate_password_hash(password)
  
  def __init__(self, **kwargs):
    """
    Initialize a user object. 
    """
    self.username = kwargs.get("username")
    self.contact_info = kwargs.get("contact_info")
    self.email = kwargs.get("email")
    
  def serialize(self):
    """
    Serialize a user object, not including sensitive data like password.
    """
    return {
      "id": self.id,
      "username": self.username,
      "contact_info": self.contact_info,
      "email": self.email,
      "sessions": [session.serialize() for session in self.sessions]
    }
    
  def simple_serialize(self):
    """
    Serialize a user object without assignments, students, or instructors fields
    """
    return {
      "id": self.id,
      "code": self.code,
      "contact_info": self.contact_info,
      "email": self.email
    }  
  
# Session Class  
class Session(db.Model):
  """
  Session Model: represents a table for sessions in the database.
  """
  __tablename__ = "sessions"
  id = db.Column(db.Integer, primary_key = True)
  session_token = db.Column(db.String, nullable = False)
  created_at = db.Column(db.DateTime, nullable = False)
  expires_at = db.Column(db.DateTime, nullable = False)
  refresh_token = db.Column(db.String, nullable = False)
  session_status = db.Column(db.String, nullable = False)
  user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
  user = db.relationship("User", back_populates = "sessions")
  
  def __init__(self, user_id):
    """
    Initialize a session object. 
    """
    self.session_token = self.token_generate()
    self.created_at = datetime.utcnow()
    self.expires_at = self.created_at + datetime.timedelta(minutes = 30)
    self.refresh_token = self.token_generate()
    self.session_status = "active"
    self.user_id = user_id
  
  @staticmethod
  def token_generate():
    """
    Generate session token.
    """
    return secrets.token_urlsafe()
  
  def session_validation(self):
    """
    Check whether session is valid.
    """
    return self.session_status == "active" and datetime.utcnow() < self.expires_at
  
  def serialize(self):
    """
    Serialize a session object (convert session object into dict format).
    """
    return {
      "id": self.id,
      "session_token": self.session_token,
      "created_at": self.created_at.isoformat(),
      "expires_at": self.expires_at.isoformat(),
      "session_status": self.session_status,
      "user_id": self.user_id
    } 
    