<p align="center">
  <img src="https://github.com/zlElo/Froggius/blob/main/res/froggius-cropped.png?raw=true" style="width: 200px">
</p>

<p align="center">
  <img src="https://img.shields.io/github/languages/code-size/zlElo/Froggius" alt="GitHub code size in bytes" />
  <img src="https://img.shields.io/github/last-commit/zlElo/Froggius" alt="GitHub last commit" />
  <img src="https://img.shields.io/github/commit-activity/m/zlElo/Froggius" alt="GitHub commit activity month" />
  <img src="https://img.shields.io/github/license/zlElo/Froggius" alt="GitHub license" />
  <a href="https://pepy.tech/project/structlog"><img src="https://static.pepy.tech/personalized-badge/froggius?period=month&units=international_system&left_color=grey&right_color=blue&left_text=Downloads%20/%20Month" alt="Downloads per month" /></a>
</p>

# Froggius
Froggius is a lightweight and dumb easy logging libary for python

---------

## Introduction
Froggius is a lightweight python libary, which is designed for easy to use logging for all your programs. It makes it easy for everybody, but also brings a lot of options to configure it like you need it. An very interesting feature for example is the error catching for functions, which makes it easy to log unexpected errors, warnings etc.

## Advantages of froggius
Froggius is like in the introduction already said very lightweight and designed for efficiency, which means that the speed of the logging is much faster than other libarys. How fast it is, can you see in this line chart:

<p align="center">
  <img src="https://github.com/zlElo/Froggius/blob/main/res/tests/froggius_exec.png?raw=true" style="width: 770px">
</p>

This example runs following debug command 60 times and prints every time the log to the console and stdout:
```py
logger.debug('Example Debug Message')
```

This massive speed improvement helps your program, to log like you need it without performance disadvantages.

System informations: MacOS Sonoma 14.4.1, MacBook Air M2, Python 3.12.1
## Installation
You can install Froggius with following command:
```
pip install froggius
```

Alternatively you can clone this repository and install then:
```bash
git clone https://github.com/zlElo/Froggius.git
cd Froggius
pip install .
```

## Usage
Here are examples for the usage of Froggius. Import statement is following:

```py
from froggius import Froggius

logger = Froggius()
```

### Using debugger/logger
Use it as debugger/logger with following possible arguments:
- log_msg (log message)
- file_path (None by default, used to set up a log file [...] to append to this file. The file does not have to already exist, if it does not exist, it will be created)
- print_out (True by default, used to setup printing to console and stdout)

```py
# Example normal logging
logger.debug('This is a normal debug log')

# This writes the log to a log file
logger.debug('This is a normal debug log', 'tests/example.log', print_out=False)
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
logger.error('This is an error log')

# This writes the error to a log file
logger.error('This is an error log', 'tests/example.log', print_out=False)
```

### Using information logger
Use it as information logger with following possible arguments:
- log_msg (log message)
- file_path (None by default, used to set up a log file [...] to append to this file. The file does not have to already exist, if it does not exist, it will be created)
- highliting (True by default, used to colorize [INF] etc.)
- print_out (True by default, used to setup printing to console and stdout)

```py
# Example information
logger.information('This is an information log')

# This writes the information to a log file
logger.information('This is an information log', 'tests/example.log', print_out=False)
```

### Using warning logger
Use it as warning logger with following possible arguments:
- log_msg (log message)
- file_path (None by default, used to set up a log file [...] to append to this file. The file does not have to already exist, if it does not exist, it will be created)
- highliting (True by default, used to colorize [WRN] etc.)
- print_out (True by default, used to setup printing to console and stdout)

```py
# Example warning
logger.warning('This is a warning log')

# This writes the warning to a log file
logger.warning('This is a warning log', 'tests/example.log', print_out=False)
```

### Using catching errors
Use the catching errors methode, to catch and handle unexpected errors, warnings etc:

```py
@logger.catch(file_path='tests/example.log')
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

### Using global configuration
If you want to configure the file_path and the print_out for everything, you can do that with following line before all other Froggius statements:

```py
# configure print_out and file_path for everything
logger = Froggius(print_out=False, file_path='tests/example.log')

logger.debug('Test normal')
logger.error('Test error')
logger.information('Test information')
```

It's also possible to say, that you want that all is not printed, but this `logger.debug('Test normal')` or `logger.information('Test information')`. Just work with the available parameters:

```py
# configure print_out and file_path for everything
logger = Froggius(print_out=False, file_path='tests/example.log')

logger.debug('Test normal', print_out=True) # everything is not printed, but this line is printed
logger.error('Test error')
logger.information('Test information')
```
