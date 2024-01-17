from ..models.transaction import Transaction
from ..models.user import User
from ..models.listing import Listing
from .. import db

class TransactionService:
  
  @staticmethod 
  def make_transaction(buyer, seller, item, transaction_amount):
    """
    Make a transaction.
    
    Parameters: 
    buyer: integer user identifier
    seller: integer user identifier 
    item: integer item listing identifier
    transaction_amount: amount of money paid during transaction
    
    Returns: serialized new transaction.
    """
    buyer = User.query.get(buyer)
    seller = User.query.get(seller)
    if not buyer or not seller:
      raise ValueError("Buyer or seller not found") 
    transaction = Transaction(buyer = buyer, seller = seller, item = item, transaction_amount = transaction_amount)
    db.session.add(transaction)
    db.session.commit()
    return transaction.serialize()
  
  @staticmethod
  def view_transaction(transaction_id):
    """
    Get a specific transaction by id.
    
    Parameters:
    transaction_id: integer identifier of transaction 
    
    Returns: serialized transaction data. 
    """
    transaction = Transaction.query.get(transaction_id)
    if transaction is None:
      return None
    return transaction.serialize()
  
  @staticmethod
  def retrieve_all_as_buyer(buyer_id):
    """
    Get all transactions as buyers using user_id.
    
    Parameters:
    buyer: integer user identifier for buyer.
    
    Returns: a list of serialized buyer transactions.
    """
    buyer = User.query.get(buyer_id)
    if buyer is None:
      raise ValueError("Buyer Not Found")
    transactions = Transaction.query.filter_by(buyer_id = buyer.id).all()
    buyer_lst = [transaction.serialize() for transaction in transactions]
    return buyer_lst
  
  @staticmethod
  def retrieve_all_as_seller(seller_id):
    """
    Get all transactions as sellers using user_id.
    
    Parameters:
    buyer: integer user identifier for seller.
    
    Returns: a list of serialized seller transactions.
    """
    seller = User.query.get(seller_id)
    if seller is None:
      raise ValueError("Seller Not Found")
    transactions = Transaction.query.filter_by(seller_id = seller.id).all()
    seller_lst = [transaction.serialize() for transaction in transactions]
    return seller_lst
  
  @staticmethod
  def retrieve_all_transactions(user_id):
    buyer_transactions = Transaction.query.filter_by(buyer_id = user_id).all()
    seller_transactions = Transaction.query.filter_by(seller_id = user_id).all()
    all_transactions = buyer_transactions + seller_transactions
    return [transaction.serialize() for transaction in all_transactions]
  
  @staticmethod
  def update_transaction(transaction_id, new_status):
    """
    Update transaction data.
    
    Parameters:
    transaction_id: integer identifier of transaction.
    
    Returns: updated transaction (serialized).
    """
    transaction = Transaction.query.get(transaction_id)
    transaction.update_transaction_status(new_status)
    db.session.commit()
    return transaction.serialize()