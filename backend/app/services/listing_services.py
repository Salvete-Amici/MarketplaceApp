from .. import db
from ..models.listing import Listing

class ListingService:
  
  @staticmethod
  def create_listing(seller_id, title, description, price, category, image_url):
    """
    Create a listing.
    
    Parameters:
    seller_id: integer user id.
    title : string title of the listing.
    description: string description of the listing.
    price: float price of the item.
    category: string category of the item.
    image_url: string url of the listing.
    
    Returns: serialized listing.
    """
    listing = Listing(seller_id = seller_id, title = title, description = description,
                      price = price, category = category, image_url = image_url)
    db.session.add(listing)
    db.session.commit()
    return listing.serialize()
  
  @staticmethod
  def get_all_listings():
    """
    Get all listings.
    
    Parameters:
    /
    
    Returns: all serialized listings in a list.
    """
    listings = Listing.query.all()
    listing_lst = [listing.serialize() for listing in listings]
    return listing_lst
  
  @staticmethod
  def get_listing_by_id(listing_id):
    """
    Get listing by id.
    
    Parameters:
    listing_id: integer listing id.
    
    Returns: serialized listing.
    """
    listing = Listing.query.get(listing_id)
    return listing.serialize()
  
  @staticmethod
  def update_listing(listing_id, **kwargs):
    """
    Update listing information.
    
    Parameters: 
    listing_id: integer identifier of listing.
    **kwargs: a dictionary for passing in relevant values
    
    Returns: updated listing.
    """
    listing = Listing.query.get(listing_id)
    try:
      for key, val in kwargs.items():
        if hasattr(listing, key):
          setattr(listing, key, val)
      db.session.commit()
      return listing.serialize()
    except Exception as e:
      return None
  
  @staticmethod
  def delete_listing(listing_id):
    """
    Delete a listing by id.
    
    Parameters: 
    listing_id: integer identifier for listing.
    
    Returns: True if listing was deleted successfully, otherwise false.
    """
    listing = Listing.query.get(listing_id)
    try: 
      db.session.delete(listing)
      db.session.commit()
      return True
    except Exception as e:
      db.session.rollback()
      return False
    