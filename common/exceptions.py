class InvalidEmailException(Exception):
    """Custom Exception that raised when email doesn't matches the pattern"""

    def __init__(self, email: str, message: str) -> None:
        self.email = email
        self.message = message
        super().__init__(f"{message}: {email}")


class Non200StatusCodeError(Exception):
    """Custom Exception that raised when status code is different than 200"""

    def __init__(self, status_code: int, message: str) -> None:
        self.status_code = status_code
        self.message = message
        super().__init__(f"{message}: Status Code: {status_code}")
