from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SERVER_KEY'] = 'hgjhghjghjxfsdfsdfsd' #helps secure cookies and session data 
    
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')#url prefix placed here will be registered to the children of that blueprint
    app.register_blueprint(auth, url_prefix='/')
    
    return app