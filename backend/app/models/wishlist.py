from app import db
from .assoc_tables import wishlist_items_association_table

class Wishlist(db.Model):
  """
  Wishlist Model: represents a table for wishlists in the database.
  """
  __tablename__ = "wishlists"
  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  items = db.relationship("Listing", secondary = wishlist_items_association_table, back_populates = "wishlists")  
  user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
  
  def __init__(self, user_id):
    """
    Initialize a wishlist object. 
    """
    self.user_id = user_id
    
  def serialize(self):
    """
    Serialize a wishlist object.
    """
    return {
      "items": [item.serialize() for item in self.items],
      "user_id": self.user_id
    }
    
