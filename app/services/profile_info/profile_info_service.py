from app.database.models import Profiles
from app.errors.Unauthorized import Unauthorized
from flask import request
import jwt

class ProfileInfoService:
    def __init__(self):
        pass

    def get_info(self):
        jwt_token = request.cookies.get("jwt")

        if not jwt_token:
            raise Unauthorized("Authentication token is missing")

        payload = jwt.decode(jwt_token, options={"verify_signature": False})
        user_id = payload.get("sub")

        profile = Profiles.get(Profiles.id == user_id)
        return profile.id, profile.role, profile.display_name
