import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from .routes import api as api_blueprint

def create_app():
    app = Flask(__name__)
    
    load_dotenv()
    
    CORS(app) 
    
    app.register_blueprint(api_blueprint)

    return app