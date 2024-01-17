from app import db
from datetime import datetime, timedelta

class Message(db.Model):
  """
  Message Model: represents a table for messages in the database.
  """
  __tablename__ = "messages"
  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  sender_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
  receiver_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
  timestamp = db.Column(db.Integer, nullable = False)
  text = db.Column(db.String, nullable = True)
  status = db.Column(db.String, nullable = False)
  
  def __init__(self, sender, receiver, **kwargs):
    """
    Initialize a message object. 
    """
    self.sender_id = sender
    self.receiver_id = receiver
    self.timestamp = datetime.utcnow() - timedelta(hours = 5)
    self.text = kwargs.get("text")
    self.status = "sent"
    
  def serialize(self):
    """
    Serialize a message object.
    """
    return {
      "sender": self.sender_id,
      "receiver": self.receiver_id,
      "timestamp": self.timestamp,
      "text": self.text,
      "status": self.status
    }
    
  def simple_serialize(self):
    """
    Serialize a message object without receiver and text.
    """
    return {
      "sender": self.sender_id,
      "timestamp": self.timestamp,
      "status": self.status
    }  
  
  def update_message_status(self, new_status):
    """Update the status of message. Possible status include sent and viewed.
    """
    self.transaction_status = new_status
    db.session.commit() 