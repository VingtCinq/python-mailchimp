class ConfigError(Exception):
    pass


class ParseError(Exception):
    def __init__(self, message, usage):
        Exception.__init__(self, message)
        self.usage = usage


class Error(Exception):
    """A general error derived from Exception."""

    def __init__(self, request):
        Exception.__init__(self, request.text)
        self.request = request


class ServerError(Error):
    """Miscellaneous server error"""
    # HTTP error code 5xx
    pass


class ConnectionError(Error):
    """An error caused by network connection."""
    pass


class Redirection(ConnectionError):
    """HTTP 3xx redirection."""
    pass


class ClientError(ConnectionError):
    """Miscellaneous client error."""
    # HTTP error 4xx
    pass


class ResourceConflict(ClientError):
    """An error raised when there is a resource conflict."""
    # 409 Conflict
    pass


class TooManyRequests(ClientError):
    """An error raised by requesting too many times"""
    # 429 Too Many Requests
    pass


class RetryWithDelay(ClientError):
    """An error raised when a resource must be retried."""
    # 449 Retry With
    pass


class ResourceInvalid(ClientError):
    """An error raised when a resource is invalid."""
    # 422 Resource Invalid
    pass


class ResourceNotFound(ClientError):
    """An error raised when a resource is not found."""
    # 404 Resource Not Found
    pass


class BadRequest(ClientError):
    """An error raised when client sends a bad request."""
    # 400 Bad Request
    pass


class UnauthorizedAccess(ClientError):
    """An error raised when an access is unauthorized."""
    # 401 Unauthorized
    pass


class ForbiddenAccess(ClientError):
    """An error raised when access is not allowed."""
    # 403 Forbidden
    pass


class MethodNotAllowed(ClientError):
    """An error raised when a method is not allowed."""
    # 405 Method Not Allowed
    pass
