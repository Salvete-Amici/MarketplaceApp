from . import db
import datetime

class Message(db.Model):
  """
  Message Model: represents a table for messages in the database.
  """
  __tablename__ = "messages"
  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  sender = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
  receiver = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
  timestamp = db.Column(db.Integer, nullable = False)
  text = db.Column(db.String, nullable = True)
  status = db.Column(db.String, nullable = False)
  
  def __init__(self, sender, receiver, **kwargs):
    """
    Initialize a message object. 
    """
    self.sender = sender
    self.receiver = receiver
    self.timestamp = datetime.utcnow()
    self.text = kwargs.get("text")
    self.status = "sent"
    
  def serialize(self):
    """
    Serialize a message object.
    """
    return {
      "sender": self.sender,
      "receiver": self.receiver,
      "timestamp": self.timestamp,
      "text": self.text,
      "status": self.status
    }
    
  def simple_serialize(self):
    """
    Serialize a message object without receiver and text.
    """
    return {
      "sender": self.sender,
      "timestamp": self.timestamp,
      "status": self.status
    }  
  
  def update_message_status(self, new_status):
    """Update the status of message. Possible status include sent and viewed.
    """
    self.transaction_status = new_status
    db.session.commit() 