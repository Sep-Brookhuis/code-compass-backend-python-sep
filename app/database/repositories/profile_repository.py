from app.database.models.profiles import Profiles
import uuid

class ProfileRepository:
    def __init__(self):
        pass

    def create_profile(self, user_id: uuid.UUID, name: str, role: str, email: str) -> Profiles:
        pass