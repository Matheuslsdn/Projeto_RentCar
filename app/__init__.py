from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = "mopazmano"
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=1)

    db.init_app(app)
    
    from .routes import bp
    app.register_blueprint(bp)
    
    from .main_bp import main_bp
    app.register_blueprint(main_bp)
    
    from .user_bp import user_bp
    app.register_blueprint(user_bp)
    
    

    return app
