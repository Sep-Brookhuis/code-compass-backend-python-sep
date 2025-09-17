from app.errors import Unauthorized
from app.services.login.authentication_service import Authentication
from app.services.login.role_check_service import RoleCheck
from app.services.login.validator_service import Validator
from app.errors.Unauthorized import Unauthorized

class LoginService:
    def __init__(self):
        self.validator = Validator()
        self.authenticator = Authentication()
        self.role_check = RoleCheck()

    def login(self):
        # validate input and store validates data
        email,password = self.validator.validate_input()

        # authenticate input and store JWT key in variable
        jwt_key,user_id = self.authenticator.supabase_authentication(email=email, password=password)

        if jwt_key is None:
            raise Unauthorized("Invalid email or password")

        # check user role
        user_role = self.role_check.find_user_role(user_id)
        user_role = user_role.upper()

        # if user role is ADMIN

        # if user role is not admin


        return "siiiii maatje!!!!"

