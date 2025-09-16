from app.database.models.profile import Profile

class ProfileRepository:
    def __init__(self):
        pass

    def create_profile(self,name,role):
        return Profile.create(name=name,role=role)