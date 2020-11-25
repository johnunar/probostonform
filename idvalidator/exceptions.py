class AresError(Exception):
    """Base class for Ares Exceptions"""
    pass


class AresConnectionError(AresError):
    """Raised when the program is unable to connect to the ARES server"""
    pass


class AresResponseError(AresError):
    """Raised when the ARES server does not return success code"""

    def __init__(self, response_code):
        self.response_code = response_code
        super().__init__(self.response_code)

    def __str__(self):
        return "Server returned response code {}, try it again later. ".format(self.response_code)


class AresSystemError(AresError):
    """Raised when the ARES server returns an error message"""

    def __init__(self, error_code, error_message):
        self.error_code = error_code
        self.error_message = error_message
        super().__init__(self.error_code, self.error_message)

    def __str__(self):
        return "Server error {0}: {1}".format(self.error_code, self.error_message)
