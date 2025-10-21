from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
import os
from dotenv import load_dotenv
from flask_marshmallow import Marshmallow

load_dotenv()

db = SQLAlchemy()
mg = Migrate()
ma = Marshmallow()

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = (
        f"mysql+pymysql://{os.getenv('DB_USER')}:"
        f"{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:"
        f"{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    db.init_app(app)
    mg.init_app(app, db)
    CORS(app)
    ma.init_app(app)

    from app.models.post import Post
    
    from app.routes.post_routes import post_bp
    app.register_blueprint(post_bp)
    
    return app