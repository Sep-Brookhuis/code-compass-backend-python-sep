class Forbidden(Exception):
    """403 – user authenticated but not allowed (e.g., not admin)."""
    pass
