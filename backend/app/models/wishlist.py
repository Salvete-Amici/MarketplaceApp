from . import db
from .assoc_tables import wishlist_items_association_table

class Wishlist(db.Model):
  """
  Wishlist Model: represents a table for wishlists in the database.
  """
  __tablename__ = "wishlists"
  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  items = db.relationship("Listing", secondary = wishlist_items_association_table, back_populates = "wishlists")  
  user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
  
  def __init__(self, item_id, user_id, **kwargs):
    """
    Initialize a wishlist object. 
    """
    self.title = kwargs.get("title")
    self.item_id = item_id
    self.user_id = user_id
    
  def serialize(self):
    """
    Serialize a wishlist object.
    """
    return {
      "title": self.title,
      "item_id": self.item_id,
      "user_id": self.user_id
    }
    
  def simple_serialize(self):
    """
    Serialize a listing object without listed time and seller id.
    """
    return {
      "title": self.title,
      "description": self.description,
      "price": self.price,
      "category": self.category,
      "image_url": self.image_url
    }  
  