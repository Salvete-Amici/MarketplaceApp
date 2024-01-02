from . import db
import datetime
from .assoc_tables import wishlist_items_association_table

class Listing(db.Model):
  """
  Listing Model: represents a table for product listings in the database.
  """
  __tablename__ = "listings"
  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  title = db.Column(db.String, nullable = False)
  description = db.Column(db.String, nullable = False)
  price = db.Column(db.Numeric(precision = 8, scale = 2), nullable = False)
  category = db.Column(db.String, nullable = False)
  image_url = db.Column(db.String, nullable = True)
  listed_time = db.Column(db.DateTime, nullable = False)
  seller_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
  wishlists = db.relationship("Wishlist", secondary = wishlist_items_association_table, back_populates = "items")
  
  def __init__(self, seller_id, **kwargs):
    """
    Initialize a listing object. 
    """
    self.title = kwargs.get("title")
    self.description = kwargs.get("description")
    self.price = kwargs.get("price")
    self.category = kwargs.get("category")
    self.image_url = kwargs.get("image_url")
    self.listed_time = datetime.utcnow()
    self.seller_id = seller_id
    
  def serialize(self):
    """
    Serialize a listing object.
    """
    return {
      "title": self.title,
      "description": self.description,
      "price": self.price,
      "category": self.category,
      "image_url": self.image_url,
      "listed_time": self.listed_time,
      "seller_id": self.seller_id
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
  