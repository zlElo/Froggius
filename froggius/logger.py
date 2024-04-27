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
    
    def __init__(self, file_path=None, print_out=None, date_format=None) -> None:
        self.glob_file_path = file_path
        self.glob_print_out = print_out
        self.glob_date_format = date_format

    def debug(self, log_msg, file_path=None, print_out=None, date_format=None):
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
        if date_format is None:
            if self.glob_date_format is not None:
                date_format = self.glob_date_format
            else:
                date_format = "%Y/%m/%d %H:%M:%S"
        log_string = f'[DBG] [{current_date.strftime(date_format)}] {log_msg}'

        # check for vars for filepath
        if self.glob_file_path is not None and file_path is None:
            file_path = self.glob_file_path

        if file_path is not None:
            with open(file_path, 'a') as log:
                log.write(f'\n[DBG] [{current_date.strftime(date_format)}] {log_msg}')

        if self.glob_print_out:
            if print_out == False:
                pass
            else:
                print(log_string, file=sys.stdout)
        if print_out and not self.glob_print_out:
            print(log_string, file=sys.stdout)
        if self.glob_print_out is None and print_out is None:
            print(log_string, file=sys.stdout)

    def error(self, log_msg, file_path=None, highlighting=True, print_out=None, line=None, date_format=None):
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
        if date_format is None:
            if self.glob_date_format is not None:
                date_format = self.glob_date_format
            else:
                date_format = "%Y/%m/%d %H:%M:%S"

        if highlighting:
            log_string = f'[\033[91mERR\033[0m] [{current_date.strftime(date_format)}] {log_msg} {f"| Occured on line: {line[0]} in {line[1]}, {line[2]}()" if line is not None else ""}'
        else:
            log_string = f'[ERR] [{current_date.strftime(date_format)}] {log_msg} {f"| Occured on line: {line[0]} in {line[1]}, {line[2]}()" if line is not None else ""}'

        # check for filepath
        if self.glob_file_path is not None and file_path is None:
            file_path = self.glob_file_path

        if file_path is not None:
            with open(file_path, 'a') as log:
                log.write(f'\n[ERR] [{current_date.strftime(date_format)}] {log_msg} {f"| Occured on line: {line[0]} in {line[1]}, {line[2]}()" if line is not None else ""}')

        if self.glob_print_out:
            if print_out == False:
                pass
            else:
                print(log_string, file=sys.stderr)
        if print_out and not self.glob_print_out:
            print(log_string, file=sys.stderr)
        if self.glob_print_out is None and print_out is None:
            print(log_string, file=sys.stderr)
    
    # @staticmethod
    def catch(self, file_path=None, continue_onexpception=True, print_out=None):
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
                file_path = None
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    _, _, tb = sys.exc_info()
                    traceback_info = traceback.extract_tb(tb)
                    line = traceback_info[-1][1]
                    file = traceback_info[-1][0]
                    function_name = traceback_info[-1][2]
                    highliting_loc = None

                    if self.glob_file_path is not None and file_path is None:
                        file_path = self.glob_file_path
                    if self.glob_print_out:
                        if print_out == False:
                            pass
                        else:
                            highliting_loc = True
                    if print_out and not self.glob_print_out:
                        highliting_loc = True
                    if self.glob_print_out is None and print_out is None:
                        highliting_loc = True

                    self.error(log_msg=str(e), highlighting=highliting_loc, print_out=print_out, line=[line, file, function_name], file_path=file_path)

                    if not continue_onexpception:
                        raise e
            return wrapper
        return decorator
    
    def information(self, log_msg, file_path=None, highlighting=True, print_out=None, date_format=None):
        """
        A function to log information with optional file output and highlighting.
        
        Parameters:
            log_msg (str): The message to be logged.
            file_path (str, optional): The file path to log to. Defaults to None.
            highlighting (bool, optional): Whether to highlight the log message. Defaults to True.
            print_out (bool, optional): Whether to print the log message. Defaults to True.
        """

        current_date = datetime.datetime.now()
        if date_format is None:
            if self.glob_date_format is not None:
                date_format = self.glob_date_format
            else:
                date_format = "%Y/%m/%d %H:%M:%S"

        if highlighting:
            log_string = f'[\033[32mINF\033[0m] [{current_date.strftime(date_format)}] {log_msg}'
        else:
            log_string = f'[INF] [{current_date.strftime(date_format)}] {log_msg}'
        
        # check for filepath
        if self.glob_file_path is not None and file_path is None:
            file_path = self.glob_file_path

        if file_path is not None:
            with open(file_path, 'a') as log:
                log.write(f'\n[INF] [{current_date.strftime(date_format)}] {log_msg}')
        
        if self.glob_print_out:
            if print_out == False:
                pass
            else:
                print(log_string, file=sys.stdout)
        if print_out and not self.glob_print_out:
            print(log_string, file=sys.stdout)
        if self.glob_print_out is None and print_out is None:
            print(log_string, file=sys.stdout)

    def info(self, log_msg, file_path=None, highlighting=True, print_out=None, date_format=None):
        """
        A function to log information with optional file output and highlighting.
        
        Parameters:
            log_msg (str): The message to be logged.
            file_path (str, optional): The file path to log to. Defaults to None.
            highlighting (bool, optional): Whether to highlight the log message. Defaults to True.
            print_out (bool, optional): Whether to print the log message. Defaults to True.
        """
        return self.information(log_msg, file_path, highlighting, print_out, date_format)

    def warning(self, log_msg, file_path=None, highlighting=True, print_out=None, date_format=None):
        """
        Logs a warning message with an optional file path, highlighting, and print out.

        Parameters:
            log_msg (str): The warning message to be logged.
            file_path (str, optional): The file path to write the log message to. Defaults to None.
            highlighting (bool, optional): Whether to highlight the log message. Defaults to True.
            print_out (bool, optional): Whether to print the log message to the console. Defaults to True.
        """
        current_date = datetime.datetime.now()
        if date_format is None:
            if self.glob_date_format is not None:
                date_format = self.glob_date_format
            else:
                date_format = "%Y/%m/%d %H:%M:%S"

        if highlighting:
            log_string = f'[\033[93mWRN\033[0m] [{current_date.strftime(date_format)}] {log_msg}'
        else:
            log_string = f'[WRN] [{current_date.strftime(date_format)}] {log_msg}'

        # check for filepath
        if self.glob_file_path is not None and file_path is None:
            file_path = self.glob_file_path

        if file_path is not None:
            with open(file_path, 'a') as log:
                log.write(f'\n[WRN] [{current_date.strftime(date_format)}] {log_msg}')
        
        if self.glob_print_out:
            if print_out == False:
                pass
            else:
                print(log_string, file=sys.stdout)
        if print_out and not self.glob_print_out:
            print(log_string, file=sys.stdout)
        if self.glob_print_out is None and print_out is None:
            print(log_string, file=sys.stdout)
