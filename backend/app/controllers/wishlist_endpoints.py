from flask import Blueprint, request
from ..services.wishlist_services import WishlistService
from . import success_helper, failure_helper

wishlist_endpoints_blueprint = Blueprint("wishlist_endpoints", __name__)

@wishlist_endpoints_blueprint.route("/api/users/<int:user_id>/wishlist/")
def get_wishlist(user_id):
  try : 
    items = WishlistService.get_all_items(user_id)["items"]
    return success_helper(items, 200)
  except Exception as e:
    print(f"Error: {e}")
    return failure_helper("Something Went Wrong", 500)

@wishlist_endpoints_blueprint.route("/api/users/<int:user_id>/wishlist/", methods = ["POST"])  
def add_to_wishlist(user_id):
  data = request.json
  item_id = data.get("item_id")
  if item_id is None:
    return failure_helper("Missing Listing ID", 400)
  res_tup = WishlistService.add_to_wishlist(user_id, item_id)
  if res_tup[0]: 
    return success_helper(([item.serialize() for item in res_tup[1].items]), 200)
  else:
    return failure_helper(res_tup[1], 400)
  
@wishlist_endpoints_blueprint.route("/api/users/<int:user_id>/wishlist/", methods = ["DELETE"])
def remove_from_wishlist(user_id):
  data = request.json
  item_id = data.get("item_id")
  if item_id is None:
    return failure_helper("Missing Information", 400)
  try: 
    result = WishlistService.delete_from_wishlist(user_id, item_id)
    if result[0]:
      return success_helper({"Message": "Item Removed"}, 200)
    else: 
      return failure_helper(result[1], 500)
  except Exception as e:
    return failure_helper("Failed To Remove Item", 500)
  
@wishlist_endpoints_blueprint.route("/api/users/<int:user_id>/wishlist/clear/", methods = ["DELETE"])
def clear_wishlist(user_id):
  result = WishlistService.clear_wishlist(user_id)
  if result:
    return success_helper({"Message": "Wishlist Cleared"}, 200)
  return failure_helper("Failed To Clear Wishlist", 500)