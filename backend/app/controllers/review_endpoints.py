from flask import Blueprint, request, jsonify
from ..services.review_services import ReviewService
from . import success_helper, failure_helper

review_endpoints_blueprint = Blueprint("review_endpoints", __name__)

@review_endpoints_blueprint.route("/api/reviews/<int:listing_id>/", methods = ["POST"])
def post_review(listing_id):
  data = request.json
  reviewer = data.get("reviewer")
  reviewee = data.get("reviewee")
  rating = data.get("rating")
  text = data.get("text")
  if reviewer is None or reviewee is None or rating is None:
    return failure_helper("Missing Information", 400)
  review = ReviewService.post_review(reviewer, reviewee, listing_id, rating, text)
  return success_helper(review, 201)

@review_endpoints_blueprint.route("/api/reviews/<int:review_id>/", methods = ["PUT"])
def edit_review(review_id):
  data = request.json
  updated_review = ReviewService.edit_review(review_id, **data)
  if updated_review is None:
    return failure_helper("Updated Review Not Found", 404)
  return success_helper(updated_review, 200)

@review_endpoints_blueprint.route("/api/reviews/<int:review_id>/")
def read_review(review_id):
  review = ReviewService.read_review(review_id)
  if review is None:
    return failure_helper("Review Not Found", 404)
  return success_helper(review, 200)

@review_endpoints_blueprint.route("/api/users/<int:user_id>/reviews/")
def get_all_reviews_of_user(user_id):
  reviews = ReviewService.get_all_reviews(user_id)
  if reviews is None or not reviews:
    return failure_helper("Reviews Not Found For This User", 404)
  return success_helper(reviews, 200)