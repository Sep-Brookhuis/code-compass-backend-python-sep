class CookieService:
    def __init__(self):
        pass

    def set_cookie(self,response,jwt):
        response.set_cookie("jwt", jwt, httponly=True,  secure=True,  samesite="None")
        return response