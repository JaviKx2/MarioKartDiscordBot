class DomainError:
    def __init__(self, code, message) -> None:
        self.code = code
        self.message = message


def has_errors(obj):
    return isinstance(obj, DomainError)

