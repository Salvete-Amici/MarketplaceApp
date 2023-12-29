from flask import Blueprint

transaction_endpoints_blueprint = Blueprint("transaction_endpoints", __name__)

@transaction_endpoints_blueprint.route("/api/transactions/")
def transactions():
  return ""