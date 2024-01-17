from .. import db
from ..models.message import Message

class MessageService:
  
  @staticmethod
  def send_message(sender, receiver, text):
    """
    Send a message.
    
    Parameters:
    sender: integer user identifier for sender.
    receiver: integer user identifier for receiver.
    text: string of text message content.
    
    Returns: serialized new message.
    """
    message = Message(sender = sender, receiver = receiver, text = text)
    db.session.add(message)
    db.session.commit()
    return message.serialize()
  
  @staticmethod
  def check_message(message_id):
    """
    Check a message.
    
    Parameters:
    message_id: integer message identifier.
    
    Returns: serialized message data.
    """
    message = Message.query.get(message_id)
    if message is None:
      return None
    message.update_message_status("viewed")
    db.session.commit()
    return message.serialize()
  
  @staticmethod
  def get_all_messages(receiver):
    """
    Get all messages of a user (receiver).
    
    Parameters:
    receiver: integer identifier of a user.
    
    Returns: a list of serialized messages.
    """
    messages = Message.query.filter_by(receiver_id = receiver).all()
    message_lst = [message.serialize() for message in messages]
    return message_lst
    