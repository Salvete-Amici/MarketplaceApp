from . import db
import datetime

class Transaction(db.Model):
  """
  Transaction Model: represents a table for transactions in the database.
  """
  __tablename__ = "transactions"
  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  buyer = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
  seller = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
  item = db.Column(db.Integer, db.ForeignKey("listings.id"), nullable = False)
  transaction_time = db.Column(db.DateTime, nullable = False)
  transaction_amount = db.Column(db.Numeric(precision = 8, scale = 2), nullable = False)
  transaction_status = db.Column(db.String, nullable = False)
  
  def __init__(self, buyer, seller, item, **kwargs):
    """
    Initialize a transaciton object. 
    """
    self.buyer = buyer
    self.seller = seller
    self.item = item
    self.transaction_time = datetime.utcnow()
    self.transaction_amount = kwargs.get("transaction_amount")
    self.transaction_status = "pending"
    
  def serialize(self):
    """
    Serialize a transaction object.
    """
    return {
      "buyer": self.buyer,
      "seller": self.seller,
      "item": self.item,
      "transaction_time": self.transaction_time,
      "transaction_amount": self.transaction_amount,
      "transaction_status": self.transaction_status
    }
    
  def simple_serialize(self):
    """
    Serialize a transaction object without buyer, seller, and transaction time.
    """
    return {
      "item": self.item,
      "transaction_amount": self.transaction_amount,
      "transaction_status": self.transaction_status
    }  
  
  def update_transaction_status(self, new_status):
    """Update the status of transaction. Possible status include pending, 
    processing, completed, and cancelled.
    """
    self.transaction_status = new_status
    db.session.commit()
