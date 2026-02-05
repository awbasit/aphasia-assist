class AphasiaAssistError(Exception):
    """Base exception for Aphasia Assist application."""
    pass


class LLMError(AphasiaAssistError):
    """Raised when LLM communication fails."""
    pass


class InvalidInputError(AphasiaAssistError):
    """Raised for malformed or unsupported user input."""
    pass