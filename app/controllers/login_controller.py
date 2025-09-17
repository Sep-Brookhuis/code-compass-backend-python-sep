from flask import Blueprint
from app.services.login.login_service import LoginService

class LoginController:
    def __init__(self):
        self.login_service = LoginService()

    def route_login(self):
        return self.login_service.login()

controller = LoginController()
login_blueprint = Blueprint("login_blueprint", __name__, url_prefix="/api")
login_blueprint.add_url_rule("/login", "login", controller.route_login, methods=["POST"])