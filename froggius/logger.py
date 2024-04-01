# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

import datetime
import sys
import traceback

class Froggius():
    """
    Main class of Froggius
    Includes logging methods
    """
    def debug(log_msg, file_path=None, print_out=True):
        """
        Writes logs, optionally to a file.

        Parameters
        ----------
        log_msg : str
            The message to be logged.
        file_path : str, optional
            The path to the file where the log should be saved, by default None
        highliting : bool, optional
            Whether the DEBUG tag should be highlighted with ANSI escape sequences, by default True
        print_out : bool, optional
            Whether the log should be printed to the stdout, by default True
        """
        current_date = datetime.datetime.now()
        log_string = f'[DBG] [{current_date.strftime("%d/%m/%Y %H:%M:%S")}] {log_msg}'

        # check for filepath
        if file_path is not None:
            with open(file_path, 'a') as log:
                log.write(f'\n[DBG] [{current_date.strftime("%d/%m/%Y %H:%M:%S")}] {log_msg}')

        if print_out:
            print(log_string, file=sys.stdout)

    def error(log_msg, file_path=None, highlighting=True, print_out=True, line=None):
        """
        Writes errors, optionally to a file.

        Parameters
        ----------
        log_msg : str
            The message to be logged.
        file_path : str, optional
            The path to the file where the log should be saved, by default None
        highlighting : bool, optional
            Whether the ERROR tag should be highlighted with ANSI escape sequences,
            by default True
        print_out : bool, optional
            Whether the log should be printed to the stdout, by default True
        line : List[str], optional
            A list containing information about the line where the error occurred,
            by default None. The list should contain [line number, file name,
            function name].
        """

        # get datetime
        current_date = datetime.datetime.now()
        if highlighting == True:
            log_string = f'[\033[91mERR\033[0m] [{current_date.strftime("%d/%m/%Y %H:%M:%S")}] {log_msg} {f"| Occured on line: {line[0]} in {line[1]}, {line[2]}()" if line is not None else ""}'
        else:
            log_string = f'[ERR] [{current_date.strftime("%d/%m/%Y %H:%M:%S")}] {log_msg} {f"| Occured on line: {line[0]} in {line[1]}, {line[2]}()" if line is not None else ""}'

        # check for filepath
        if file_path is not None:
            with open(file_path, 'a') as log:
                log.write(f'\n[ERR] [{current_date.strftime("%d/%m/%Y %H:%M:%S")}] {log_msg} {f"| Occured on line: {line[0]} in {line[1]}, {line[2]}()" if line is not None else ""}')

        if print_out == True:
            print(log_string, file=sys.stderr)
    
    @staticmethod
    def catch(file_path=None, continue_onexpception=True):
        """
        A decorator that catches exceptions and logs them with LogMx.error

        Parameters
        ----------
        file_path : str, optional
        contiune_onexpception : bool, optional

        Returns
        -------
        decorator
        """
        def decorator(func):
            def wrapper(*args, **kwargs):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    _, _, tb = sys.exc_info()
                    traceback_info = traceback.extract_tb(tb)
                    line = traceback_info[-1][1]
                    file = traceback_info[-1][0]
                    function_name = traceback_info[-1][2]

                    Froggius.error(log_msg=str(e), highlighting=True, print_out=True, line=[line, file, function_name], file_path=file_path)

                    if not continue_onexpception:
                        raise e
            return wrapper
        return decorator
    
    def information(log_msg, file_path=None, highlighting=True, print_out=True):
        current_date = datetime.datetime.now()

        if highlighting:
            log_string = f'\033[92m[INF]\033[0m [{current_date.strftime("%d/%m/%Y %H:%M:%S")}] {log_msg}'
        else:
            log_string = f'[INF] [{current_date.strftime("%d/%m/%Y %H:%M:%S")}] {log_msg}'
        
        # check for filepath
        if file_path is not None:
            with open(file_path, 'a') as log:
                log.write(f'\n[INF] [{current_date.strftime("%d/%m/%Y %H:%M:%S")}] {log_msg}')
        
        if print_out == True:
            print(log_string, file=sys.stdout)