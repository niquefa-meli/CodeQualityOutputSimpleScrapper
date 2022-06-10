class CodeQualityScraperError(Exception):
    """A base class for CodeQualityScraperError exceptions."""


class IssuesCountError(CodeQualityScraperError):
    def __init__(self, *args, **kwargs):
        super().__init__(*args)
        self.message = kwargs.get("message")
