from froggius.logger import Froggius

# ----- Logging/Debugging -----
# Example normal logging
Froggius.debug('This is a normal debug log')

# This writes the log to a log file
Froggius.debug('This is a normal debug log', 'tests/example.log', print_out=False)


# ----- Errors -----
# Example error
Froggius.error('This is an error log')

# This writes the error to a log file
Froggius.error('This is an error log', 'tests/example.log', print_out=False)


# ----- Catching unexpected Errors -----
@Froggius.catch(file_path='tests/example.log')
def example_function():
    """
    Not working function, because of division by zero
    """
    var1 = 5
    var = 0

    result = var1 / var
    print(result)

example_function()