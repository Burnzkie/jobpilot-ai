class AppException(Exception):
    """
    Base application exception.
    """

    def __init__(self, message: str, status_code: int = 400):
        self.message = message
        self.status_code = status_code


class NotFoundException(AppException):

    def __init__(self, message="Resource not found."):
        super().__init__(message, 404)


class DuplicateResourceException(AppException):

    def __init__(self, message="Resource already exists."):
        super().__init__(message, 409)


class UnauthorizedException(AppException):

    def __init__(self, message="Unauthorized."):
        super().__init__(message, 401)


class ForbiddenException(AppException):

    def __init__(self, message="Forbidden."):
        super().__init__(message, 403)


class ValidationException(AppException):

    def __init__(self, message="Validation error."):
        super().__init__(message, 422)
