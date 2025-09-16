class BadRequest(Exception):
    """400 – request is not valid JSON, etc."""
    pass

class Unauthorized(Exception):
    """401 – wrong/missing credentials (email/password)."""
    pass

class Forbidden(Exception):
    """403 – user authenticated but not allowed (e.g., not admin)."""
    pass
