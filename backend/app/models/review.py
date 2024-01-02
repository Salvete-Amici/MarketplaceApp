from . import db
import datetime

class Review(db.Model):
  """
  Review Model: represents a table for reviews in the database.
  """
  __tablename__ = "reviews"
  id = db.Column(db.Integer, primary_key = True, autoincrement = True)
  reviewer = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
  reviewee = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
  item = db.Column(db.Integer, db.ForeignKey("listings.id"), nullable = False)
  rating = db.Column(db.Integer, nullable = False)
  text = db.Column(db.String, nullable = True)
  review_time = db.Column(db.DateTime, nullable = False)
  
  def __init__(self, reviewer, reviewee, item, **kwargs):
    """
    Initialize a review object. 
    """
    self.reviewer = reviewer
    self.reviewee = reviewee
    self.item = item
    self.rating = kwargs.get("rating")
    self.text = kwargs.get("text")
    self.review_time = datetime.utcnow()
    
  def serialize(self):
    """
    Serialize a review object.
    """
    return {
      "reviewer": self.reviewer,
      "reviewee": self.reviewee,
      "item": self.item,
      "rating": self.rating,
      "text": self.text,
      "review_time": self.review_time
    }
    
  def simple_serialize(self):
    """
    Serialize a review object without reviewer and reviewee.
    """
    return {
      "item": self.item,
      "rating": self.rating,
      "text": self.text,
      "review_time": self.review_time
    } 
    

  
