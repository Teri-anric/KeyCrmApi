class BaseKeyCrmError(BaseException):
    pass

class UnAuthorizedError(BaseKeyCrmError):
    ...

class TooManyRequests(BaseKeyCrmError):
    ...

