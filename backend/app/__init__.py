from flask import Flask
from flask_sqlalchemy import SQLAlchemy  

db = SQLAlchemy()  
def create_app(config_filename):
    app = Flask(__name__) 
    app.config.from_pyfile(config_filename)
    db.init_app(app)  
    
    with app.app_context():
        from .models import user, listing, review, wishlist, transaction, message, assoc_tables
        db.create_all()

    from .controllers.user_endpoints import user_endpoints_blueprint
    from .controllers.listing_endpoints import listing_endpoints_blueprint
    from .controllers.review_endpoints import review_endpoints_blueprint
    from .controllers.message_endpoints import message_endpoints_blueprint
    from .controllers.transaction_endpoints import transaction_endpoints_blueprint
    from .controllers.wishlist_endpoints import wishlist_endpoints_blueprint
    
    app.register_blueprint(user_endpoints_blueprint)
    app.register_blueprint(listing_endpoints_blueprint)
    app.register_blueprint(review_endpoints_blueprint)
    app.register_blueprint(message_endpoints_blueprint)
    app.register_blueprint(transaction_endpoints_blueprint)
    app.register_blueprint(wishlist_endpoints_blueprint)

    return app  


