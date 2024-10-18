import sys
# Define one error handler method

def error_message_detail(error, error_detail:sys):
    _, _, exc_tb = error_detail.exc_info()
    
    # extract error message
    file_name = exc_tb.tb_frame.f_code.co_filename
    
    error_message = f"Error occured python script name: [{0}] line [{1} error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    
    return error_message

# Custom error handling class using inheritance:Exception
class AppException(Exception):
    def __init__(self, error_message, error_detail):
        """
        :param error_message: error message in string format
        """
        super().__init__(error_message)

        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message