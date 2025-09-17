from app.database.models import Profiles
from app.errors.NotFound import NotFound

class RoleCheck:
    def __init__(self):
        pass

    def find_user_role(self, user_id):
        try:
            profile = Profiles.get(Profiles.id == user_id)
            return profile.role
        except:
            raise NotFound("User not in database")
