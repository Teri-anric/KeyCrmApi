class BaseKeyCrmError(BaseException):
    pass


class UnAuthorizedError(BaseKeyCrmError):
    ...

class NotFound(BaseKeyCrmError):
    ...


class TooManyRequests(BaseKeyCrmError):
    ...
