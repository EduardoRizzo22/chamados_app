from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    db.init_app(app)
    login_manager.init_app(app)

    from app.controllers import auth_controller, chamado_controller,user_controller
    app.register_blueprint(auth_controller.bp)
    app.register_blueprint(chamado_controller.bp)
    app.register_blueprint(user_controller.bp)


    return app
