from dotenv import load_dotenv
from flask import request, jsonify
from supabase import create_client
from app.database.models import Profiles
from app.errors.BadRequest import BadRequest
from app.errors.Forbidden import Forbidden
from app.services.jwt_handling.jwt_reading import read_jwt_role
import os

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_SERVICE_ROLE_KEY")

supabase = create_client(url, key)


class CreateUserService:
    def __init__(self):
        pass

    def create_user(self):
        try:
            jwt_key = request.cookies.get("jwt")
            user_role = read_jwt_role(jwt_key)

            if user_role == "TRAINEE":
                raise Forbidden("Admin rights required")

            data = request.get_json(silent=False)

            email = str(data.get("email", "")).strip()
            display_name = str(data.get("displayName", "")).strip()
            role = str(data.get("role", "")).upper()

            res = supabase.auth.admin.create_user({
                "email": email,
                "password": "wachtwoord",
                "email_confirm": True,
                "user_metadata": {"display_name": display_name},
                "app_metadata": {"role": role},
            })

            user_id = res.user.id
            Profiles.create(id=user_id, display_name=display_name, role=role, email=email)

            return jsonify({"ok": "True", "user": display_name}), 201

        except:
            raise BadRequest("Failed to create user")




