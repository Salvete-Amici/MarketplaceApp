from .. import db
from ..models.review import Review

class ReviewService:
  
  @staticmethod
  def post_review(reviewer, reviewee, item, rating, text):
    """
    Post a new review.

    Parameters:
    reviewer: integer identifier of the user wrting the review.
    reviewee: integer identifier of the user whom the review is for.
    item: integer identifier of the listed item being reviewed.
    rating: integer rating of item provided in the review.
    text: text content of the review.
    
    Returns: serialized new review.
    """
    review = Review(reviewer = reviewer, reviewee = reviewee, item = item, rating = rating, text = text)
    return review.serialize()
  
  @staticmethod
  def edit_review(review_id, **kwargs):
    """
    Edit an existing review.
    
    Parameters: 
    review_id: integer id of the review.
    kwargs: dictionary containing new review content.
    
    Returns: updated review.
    """
    review = Review.query.get(review_id)
    try:
      for key, val in kwargs.item():
        if hasattr(review, key):
          setattr(review, key, val)
      db.session.commit()
      return review.serialize()
    except Exception as e:
      db.session.rollback()
      
  @staticmethod
  def read_review(review_id):
    """
    Get a review by id.
    
    Parameters:
    review_id: integer review identifier.
    
    Returns: serialized review data. 
    """
    review = Review.query.get(review_id)
    return review.serialize()