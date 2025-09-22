import os
from dotenv import load_dotenv
from supabase import create_client
from app.errors.Unauthorized import Unauthorized

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_ANON_KEY")

supabase = create_client(url, key)


class Authentication:
    def __init__(self):
        pass

    def supabase_authentication(self, email: str, password: str):
        try:
            response = supabase.auth.sign_in_with_password({
                "email": email,
                "password": password
            })
        except:
            raise Unauthorized(f"Supabase auth failed")

        if response.session:
            return response.session.access_token, response.user.id
        return None
