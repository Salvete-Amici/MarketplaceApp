from flask import Blueprint, request
from ..services.listing_services import ListingService
from . import success_helper, failure_helper

listing_endpoints_blueprint = Blueprint("listing_endpoints", __name__)

@listing_endpoints_blueprint.route("/api/listings/", methods = ["POST"])
def new_listing():
  data = request.json
  seller_id = data.get("seller_id")
  title = data.get("title")
  description = data.get("description")
  price = data.get("price")
  category = data.get("category")
  image_url = data.get("image_url")
  if seller_id is None or title is None or description is None or price is None or category is None or image_url is None:
    return failure_helper("Missing Information", 400)
  listing = ListingService.create_listing(seller_id, title, description, price, category, image_url)
  return success_helper(listing, 201)
  
@listing_endpoints_blueprint.route("/api/listings/")
def listings():
  return ListingService.get_all_listings()

@listing_endpoints_blueprint.route("/api/listings/<int:listing_id>/")
def get_listing_by_id(listing_id):
  return ListingService.get_listing_by_id(listing_id)

@listing_endpoints_blueprint.route("/api/listings/<int:listing_id>/", methods = ["POST"])
def update_listing(listing_id):
  data = request.json
  updated_listing = ListingService.update_listing(listing_id, **data)
  if updated_listing is None:
    return failure_helper("Listing Not Found", 404)
  return success_helper(updated_listing, 200)

@listing_endpoints_blueprint.route("/api/listings/<int:listing_id>/", methods = ["DELETE"])
def remove_listing(listing_id):
  result = ListingService.delete_listing(listing_id)
  if result == False:
    return failure_helper("Deletion Failed", 500)
  return success_helper({"Message": "Listing Deleted"}, 200)


