<p align="center">
  <img src="https://github.com/zlElo/Froggius/blob/main/res/froggius-cropped.png?raw=true" style="width: 200px">
</p>

<p align="center">
  <img src="https://img.shields.io/github/languages/code-size/zlElo/Froggius" alt="GitHub code size in bytes" />
  <img src="https://img.shields.io/github/last-commit/zlElo/Froggius" alt="GitHub last commit" />
  <img src="https://img.shields.io/github/commit-activity/m/zlElo/Froggius" alt="GitHub commit activity month" />
  <img src="https://img.shields.io/github/license/zlElo/Froggius" alt="GitHub license" />
</p>

# Froggius
Froggius is a dumb easy logging tool for python

---------

## Introduction
Froggius is a lightweight python libary, which is designed for easy to use logging for all your programs. It makes it easy for everybody, but also brings a lot of options to configure it like you need it. An very interesting feature for example is the error catching for functions, which makes it easy to log unexpected errors, warnings etc.


## Usage
Here are examples for the usage of Froggius. Import statement is following:

```py
from froggius.logger import Froggius
```

### Using debugger/logger
Use it as debugger/logger with following possible arguments:
- log_msg (log message)
- file_path (None by default, used to set up a log file [...] to append to this file. The file does not have to already exist, if it does not exist, it will be created)
- highliting (True by deafult, used to colorize [DBG] etc.)
- print_out (True by default, used to setup printing to console and stdout)

```py
# Example normal logging
Froggius.debug('This is a normal debug log')

# This writes the log to a log file
Froggius.debug('This is a normal debug log', 'tests/example.log', print_out=False)
```

### Using with predefinied errors
Use it as error logger with following possible arguments:
- log_msg (log message)
- file_path (None by default, used to set up a log file [...] to append to this file. The file does not have to already exist, if it does not exist, it will be created)
- highliting (True by deafult, used to colorize [DBG] etc.)
- print_out (True by default, used to setup printing to console and stdout)
- line (None by default, expects list with following 3 items in this structure: [line number, file name, function name])

```py
# Example error
Froggius.error('This is an error log')

# This writes the error to a log file
Froggius.error('This is an error log', 'tests/example.log', print_out=False)
```

### Using catching errors
Use the catching errors methode, to catch and handle unexpected errors, warnings etc:

```py
@Froggius.catch(file_path='tests/example.log')
def example_function():
    """
    Information: Not working function, because of division by zero
    """
    var1 = 5
    var = 0

    result = var1 / var
    print(result)

example_function()
```

Output in log file:
`
[ERR] [01/04/2024 09:15:00] division by zero | Occured on line: 28 in /Users/username/path/examples.py, example_function()
`
