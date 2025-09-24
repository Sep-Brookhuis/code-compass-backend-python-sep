class CookieService:
    def __init__(self):
        pass

    def set_cookie(self,response,jwt):
        response.set_cookie(
            "jwt",
            jwt,
            httponly=True,
            secure=False,
            samesite="Lax",
            max_age=60 * 60 * 24 * 7
        )

        return response