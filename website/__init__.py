from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' 
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app) #use this database for the flask app
    
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')#url prefix placed here will be registered to the children of that blueprint
    app.register_blueprint(auth, url_prefix='/')
    
    from .models import User, Note
    
    
    create_databases(app)
    
    return app
    
    
def create_databases(app):
    if not path.exists('website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')
    else:
        print(f'Database {DB_NAME} already exists!')