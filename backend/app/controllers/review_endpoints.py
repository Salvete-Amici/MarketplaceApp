from flask import Blueprint

review_endpoints_blueprint = Blueprint("review_endpoints", __name__)

@review_endpoints_blueprint.route("/api/reviews/")
def reviews():
  return ""