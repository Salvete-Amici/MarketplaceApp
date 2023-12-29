import os
from app import create_app

if os.getenv("FLASK_ENV") == "production":
    app = create_app("production_config.py")
elif os.getenv("FLASK_ENV") == "development":
    app = create_app("development_config.py")
    
if __name__ == '__main__':
    app.run()