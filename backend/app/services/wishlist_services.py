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
    if item is None:
      return False, "Item Not Found"
    if item not in user_wishlist.items:
      try:
        user_wishlist.items.append(item)
        db.session.commit()
        return True, user_wishlist
      except Exception as e: 
        return False, f"Error: {e}"
    elif item in user_wishlist.items:
      return False, "Item Already In Wishlist"
    
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
    return {"wishlist_id": user_wishlist.id, "items": [item.serialize() for item in items]}
  
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
    if user_wishlist is None:
      return False, "Wishlist Does Not Exist"
    int_id = int(item_id) 
    for item in user_wishlist.items:
      if item.id == int_id:
        user_wishlist.items.remove(item)
        db.session.commit()
        return True, user_wishlist
    return False, "Item Not Found"
    
  @staticmethod
  def clear_wishlist(user_id):
    """
    Remove all items from a user's wishlist.
    
    Parameters:
    user_id: integer identifier of a user.
    
    Returns: true if operation was successful otherwise false.
    """
    try: 
      user_wishlist = Wishlist.query.filter_by(user_id = user_id).first()
      user_wishlist.items.clear()
      db.session.commit()
      return True
    except Exception as e:
      print(e)
      return False
      
      
    