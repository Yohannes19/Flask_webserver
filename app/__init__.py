from flask import Flask
from config import Config

def create_app(config_class=Config):
    app=Flask(__name__)
    app.config.from_object(config_class)
    #intialize the flask extensions 
    
    #register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    from app.posts import bp as posts_bp
    app.register_blueprint(posts_bp,url_prefix='/posts')
    from app.questions import bp as questions_bp
    app.register_blueprint(questions_bp,url_prefix='/questions')
    
    
    @app.route('/test/')
    def test_page():
        return 'Testing the app'
    
    return app
    