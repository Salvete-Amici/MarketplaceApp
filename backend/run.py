import os
from app import create_app

config_dir_path = os.path.join(os.path.dirname(__file__), "config")

if os.getenv("APP_ENV") == "production":
    config_file_path = os.path.join(config_dir_path, "production_config.py")
    app = create_app(config_file_path)
elif os.getenv("APP_ENV") == "development":
    config_file_path = os.path.join(config_dir_path, "development_config.py")
    app = create_app(config_file_path)
else: 
    raise ValueError("Invalid APP_ENV")
    
if __name__ == "__main__":
    app.run(debug = app.config["DEBUG"])
    
    
    

