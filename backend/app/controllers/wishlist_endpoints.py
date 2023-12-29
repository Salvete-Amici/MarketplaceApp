from flask import Blueprint

wishlist_endpoints_blueprint = Blueprint("wishlist_endpoints", __name__)

@wishlist_endpoints_blueprint.route("/api/wishlists/")
def wishlists():
  return ""