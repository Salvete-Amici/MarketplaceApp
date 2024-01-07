from ..models.transaction import Transaction
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
    return transaction.serialize()
  
  @staticmethod
  def retrieve_all_as_buyer(buyer):
    """
    Get all transactions as buyers using user_id.
    
    Parameters:
    buyer: integer user identifier for buyer.
    
    Returns: a list of serialized buyer transactions.
    """
    transactions = Transaction.query.filter_by(buyer = buyer).all()
    buyer_lst = [transaction.serialize() for transaction in transactions]
    return buyer_lst
  
  @staticmethod
  def retrive_all_as_seller(seller):
    """
    Get all transactions as sellers using user_id.
    
    Parameters:
    buyer: integer user identifier for seller.
    
    Returns: a list of serialized seller transactions.
    """
    transactions = Transaction.query.filter_by(seller = seller).all()
    seller_lst = [transaction.serialize() for transaction in transactions]
    return seller_lst
  
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