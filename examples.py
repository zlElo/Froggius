from loggiusm.logger import LogMx

# ----- Logging/Debugging -----
# Example normal logging
LogMx.debug('This is a normal debug log')

# This writes the log to a log file
LogMx.debug('This is a normal debug log', 'tests/example.log', print_out=False)


# ----- Errors -----
# Example error
LogMx.error('This is an error log')

# This writes the error to a log file
LogMx.error('This is an error log', 'tests/example.log', print_out=False)


# ----- Catching unexpected Errors -----
@LogMx.catch
def example_function():
    """
    Not working function, because of division by zero
    """
    var1 = 5
    var = 0

    result = var1 / var
    print(result)

example_function()