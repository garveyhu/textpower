from textpower.api.response.code import ResultCode


class CustomException(Exception):
    def __init__(self, result_code: ResultCode, message: str = None):
        self.result_code = result_code
        self.message = message if message else result_code.message
        super().__init__(self.message)