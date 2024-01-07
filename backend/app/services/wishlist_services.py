from .. import db
from ..models.wishlist import Wishlist
from ..models.listing import Listing

class WishlistService:
  
  @staticmethod
  def add_to_wishlist(user_id, item_id):
    """
    Add an item to wishlist.
    
    Parameters:
    user_id: integer identifier for user.
    item_id: integer identifier for listed item.
    
    Returns: true if item added successfully, otherwise false.
    """
    user_wishlist = Wishlist.query.filter_by(user_id = user_id).first()
    item = Listing.query.get(item_id)
    if item not in user_wishlist.items:
      try:
        user_wishlist.items.append(item)
        return True
      except Exception as e: 
        return False
    
  @staticmethod
  def get_all_items(user_id):
    """
    Get all items on the wishlist.
    
    Parameters:
    user_id: integer identifier of user.
    
    Returns: a list of all items on the wishlist.
    """
    user_wishlist = Wishlist.query.filter_by(user_id = user_id).first()
    items = user_wishlist.items
    return items 
  
  @staticmethod
  def delete_from_wishlist(user_id, item_id):
    """
    Remove an item from user's wishlist.
    
    Parameters:
    user_id: integer identifier of user.
    item_id: integer identifier of item.
    
    Returns: true if item successfully removed from wishlist, otherwise false.
    """
    user_wishlist = Wishlist.query.filter_by(user_id = user_id).first()
    for item in user_wishlist.items:
      if item.id == item_id:
        user_wishlist.items.remove(item)
        db.session.commit()
        return True
    return False 
    
  @staticmethod
  def clear_wishlist(user_id):
    """
    Remove all items from a user's wishlist.
    
    Parameters:
    user_id: integer identifier of a user.
    
    Returns: true if operation was successful otherwise false.
    """
    try: 
      user_wishlist = Wishlist.query.filter_by(user_id = user_id)
      user_wishlist.items.clear()
      db.session.commit()
      return True
    except Exception as e:
      return False
      
      
    