from flask import Blueprint
from app.services.logout.logout_service import LogoutService

class LogoutController:
    def __init__(self):
        self.logout = LogoutService()

    def route_logout(self):
        return self.logout.logout()

controller = LogoutController()
logout_blueprint = Blueprint("logout_blueprint", __name__, url_prefix="/api")
logout_blueprint.add_url_rule("/logout", "logout", controller.route_logout, methods=["POST"])