from app.services.profile_info.profile_info_service import ProfileInfoService
from flask import Blueprint, jsonify


class ProfileInfoController:
    def __init__(self):
        self.profile_info = ProfileInfoService()

    def get_info(self):
        user_id,user_role,user_name = self.profile_info.get_info()
        return jsonify({"id": user_id,"role": user_role,"display_name": user_name})

controller = ProfileInfoController()
profile_info_blueprint = Blueprint("info_blueprint", __name__, url_prefix="/api")
profile_info_blueprint.add_url_rule("/me", "info", controller.get_info, methods=["GET"])