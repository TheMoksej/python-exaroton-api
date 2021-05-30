class ExarotonPY(Exception):
  pass

class HTTPException(ExarotonPY):
    """
    Raised when accessing the API fails
    """
    def __init__(self, *args, **kwargs):
        self.raised_error = kwargs.get('raised_error', None)
        if isinstance(self.raised_error, dict):
            self.message = self.raised_error.get('message', '')
        else:
            self.message = self.raised_error
            self.status = None
            self.status = kwargs.get('status', None)

        err = f"Status code: {self.status} --> {self.message}"
        super().__init__(err)
