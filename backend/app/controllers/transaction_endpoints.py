from flask import Blueprint, request, jsonify
from ..services.transaction_services import TransactionService
from . import success_helper, failure_helper

transaction_endpoints_blueprint = Blueprint("transaction_endpoints", __name__)

@transaction_endpoints_blueprint.route("/api/transactions/<int:listing_id>/", methods = ["POST"])
def make_transaction(listing_id):
  data = request.json
  buyer = data.get("buyer")
  seller = data.get("seller")
  transaction_amount = data.get("transaction_amount")
  try:
    transaction = TransactionService.make_transaction(buyer, seller, listing_id, transaction_amount)
    return success_helper(transaction, 201)
  except Exception as e:
    print(f"Transaction Error: {e}")
    return failure_helper("Transaction Failed", 500)

@transaction_endpoints_blueprint.route("/api/transactions/<int:transaction_id>/")
def view_transaction(transaction_id):
  try:
    transaction = TransactionService.view_transaction(transaction_id)
    if transaction is None:
      return failure_helper("Transaction Not Found", 404)
    return success_helper(transaction, 200)
  except Exception as e:
    return failure_helper("Something Went Wrong", 500)

@transaction_endpoints_blueprint.route("/api/seller_transactions/<int:user_id>/")
def retrieve_all_as_seller(user_id):
  try: 
    seller_transactions = TransactionService.retrieve_all_as_seller(user_id)
    return success_helper(seller_transactions, 200)
  except Exception as e:
    print(f"Error: {str(e)}") 
    return failure_helper("Something Went Wrong", 500)
  
@transaction_endpoints_blueprint.route("/api/buyer_transactions/<int:user_id>/")
def retrieve_all_as_buyer(user_id):
  try: 
    buyer_transactions = TransactionService.retrieve_all_as_buyer(user_id)
    return success_helper(buyer_transactions, 200)
  except Exception as e: 
    print(f"Error: {str(e)}")
    return failure_helper("Something Went Wrong", 500)
  
@transaction_endpoints_blueprint.route("/api/users/<int:user_id>/transactions/")
def retrieve_all_transactions(user_id):
  try: 
    all_transactions = TransactionService.retrieve_all_transactions(user_id)
    return success_helper(all_transactions, 200)
  except Exception as e:
    return failure_helper("Something Went Wrong", 500)