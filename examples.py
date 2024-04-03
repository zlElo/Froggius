# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

from froggius import Froggius

logger = Froggius()

# ----- Logging/Debugging -----
# Example normal logging
logger.debug('This is a normal debug log')

# This writes the log to a log file
logger.debug('This is a normal debug log', 'tests/example.log', print_out=False)


# ----- Errors -----
# Example error
logger.error('This is an error log')

# This writes the error to a log file
logger.error('This is an error log', 'tests/example.log', print_out=False)


# ----- Informations -----
# Example information
logger.information('This is an information log')

# This writes the information to a log file
logger.information('This is an information log', 'tests/example.log', print_out=False)


# ----- Warnings -----
# Example warning
logger.warning('This is a warning log')

# This writes the warning to a log file
logger.warning('This is a warning log', 'tests/example.log', print_out=False)


# ----- Catching unexpected Errors -----
@logger.catch(file_path='tests/example.log')
def example_function():
    """
    Not working function, because of division by zero
    """
    var1 = 5
    var = 0

    result = var1 / var
    print(result)

example_function()