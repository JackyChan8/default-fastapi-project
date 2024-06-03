from fastapi import HTTPException, status


class BaseAuthException(HTTPException):
    """
        Base Auth Exception
    """
    detail = ""
    status_code = 500

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class InvalidTokenException(BaseAuthException):
    """
        Invalid Token Exception
    """
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Неверный формат токена'


class ExpiredTokenException(BaseAuthException):
    """
        Expired Token Exception
    """
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Токен истек'


class UserNotExistsException(BaseAuthException):
    """
        User Not Exists Exception
    """
    status_code = status.HTTP_401_UNAUTHORIZED

