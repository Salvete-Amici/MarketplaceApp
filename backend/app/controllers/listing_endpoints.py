from flask import Blueprint

listing_endpoints_blueprint = Blueprint("listing_endpoints", __name__)

@listing_endpoints_blueprint.route("/api/listings/")
def listings():
  return ""