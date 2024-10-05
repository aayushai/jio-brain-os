#!/usr/bin/env python3
import os
import sys
import datetime
import logging
import traceback
from uuid import uuid4
from enum import Enum
from logging.handlers import TimedRotatingFileHandler
from pythonjsonlogger import jsonlogger
import pytz
#from logging.handlers import RotatingFileHandler


class ProgramTypes(str, Enum):
    cron = "cron"
    api = "api"


trace_id = os.getenv("TRACE_ID", uuid4().hex)

## Create custom json formatter in case of cron job to add trace_id 
class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get("trace_id"):
            log_record["trace_id"] = trace_id

## Main class to initialize logger
class InitializeLogger:
    """Levels and When it’s used:

    DEBUG : Detailed information, typically of interest only when diagnosing problems.

    INFO : Confirmation that things are working as expected.

    WARNING : An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

    ERROR : Due to a more serious problem, the software has not been able to perform some function.

    CRITICAL : A serious error, indicating that the program itself may be unable to continue running.
    """

    def __init__(
        self,
        program_type,
        enable_console_logging=False,
        enable_file_logging=False,
        log_dir_path=None,
        log_file_name="default.log",
        log_file_when="D",
        log_file_interval=1,
        log_file_backupCount=29,
        log_level=logging.DEBUG,
        local_timezone=True,
    ):
        """Write the logs to console and/or local log file. Local Log File's Timed Log Rotation happens based on the product of when and interval. Defaults cases rotates log everyday and keeps backup of 29 days, totaling to 30(1+29) days of logs data available at any time.

        Args:
            program_type (str) : Must be one of the following : ["cron","api"]
            log_dir_path (str) : path of the logs directory.
            enable_console_logging (bool, optional): whether logging should be enabled to console. Defaults to True.
            enable_file_logging (bool, optional): whether logging should be enabled to local log file. Defaults to False.
            log_file_name (str, optional): local log file name if "enable_file_logging" is set to true. Defaults to "default.log".
            log_file_when (str, optional): the unit of frequency to rotate the local log file if "enable_file_logging" is set to true. (works in conjunction with "log_file_interval") Defaults to 'D'.
            log_file_interval (int, optional): interval at which local log file rotation should be done if "enable_file_logging" is set to true.(works in conjunction with "log_file_when") Defaults to 1.
            log_file_backupCount (int, optional): If backupCount is nonzero, at most backupCount files will be kept, and if more would be created when rollover occurs, the oldest one is deleted.. Defaults to 29.
            log_level ([type], optional): the minimum log level to log. Defaults to logging.DEBUG.
            local_timezone (bool, optional): if True, timezone should be local(IST), else UTC
        """
        if program_type in list(ProgramTypes):
            self.PROGRAM_TYPE = program_type
        else:
            logging.critical("Type must be one of the following : ['cron','api']")
            sys.exit(1)

        if enable_file_logging:
            try:
                valid_dir = os.path.isdir(log_dir_path)
                if valid_dir:
                    self.LOG_DIR_PATH = log_dir_path
                else:  # eg. log_dir_path = 'a'
                    logging.critical(f"'{log_dir_path}' is not a valid path")
                    sys.exit(1)
            except TypeError as e:  # TypeError : (log_dir_path) = None
                logging.exception(e)
                logging.critical(
                    "Please provide a valid directory path in 'log_dir_path'"
                )
                sys.exit(1)
            except Exception as e:  # Any other exception other than TypeError
                logging.exception(e)
                sys.exit(1)

        self.LOG_LEVEL = log_level
        self.LOG_TIMEZONE = (
            pytz.timezone("Asia/Kolkata")
            if local_timezone == True
            else pytz.timezone("UTC")
        )
        self.LOG_DATE_FORMAT = "%d-%m-%Y %H:%M:%S"

        if self.PROGRAM_TYPE == ProgramTypes.api.value:
            json_formatter = jsonlogger.JsonFormatter(
                "%(name)s : %(asctime)s : %(levelname)s : %(filename)s : %(funcName)s : %(lineno)d : %(message)s"
            )
        elif self.PROGRAM_TYPE == ProgramTypes.cron.value:
            json_formatter = CustomJsonFormatter(
                "%(name)s : %(asctime)s : %(levelname)s : %(filename)s : %(funcName)s : %(lineno)d : %(message)s : %(trace_id)s"
            )

        self.LOG_HANDLERS = []

        if enable_console_logging:
            console_handler = logging.StreamHandler()
            console_handler.setLevel(self.LOG_LEVEL)
            console_handler.setFormatter(json_formatter)
            self.LOG_HANDLERS.append(console_handler)

        if enable_file_logging:
            self.LOG_FILE_PATH = os.path.join(
                self.LOG_DIR_PATH,
                os.path.splitext(os.path.basename(log_file_name))[0] + ".log",
            )
            self.LOG_FILE_WHEN = log_file_when
            self.LOG_FILE_INTERVAL = log_file_interval
            self.LOG_FILE_BACKUPCOUNT = log_file_backupCount

            file_handler = TimedRotatingFileHandler(
                self.LOG_FILE_PATH,
                when="h", #minutes = m , h = hour
                interval= 1, # 1 hour
                backupCount= 5,
                encoding="utf-8",
            )
            file_handler.setLevel(self.LOG_LEVEL)
            file_handler.setFormatter(json_formatter)
            self.LOG_HANDLERS.append(file_handler)

        logging.basicConfig(
            level=self.LOG_LEVEL,
            datefmt=self.LOG_DATE_FORMAT,
            handlers=self.LOG_HANDLERS,
        )

        logging.Formatter.converter = self.localized_time
        sys.excepthook = self.log_except_hook

    @staticmethod
    def log_except_hook(etype, value, tb):
        traceback_msg = "".join(traceback.format_exception(etype, value, tb))
        logging.error("Unhandled exception: {}".format(traceback_msg))

    # @staticmethod
    def localized_time(self, *args):
        converted_time = (
            pytz.utc.localize(datetime.datetime.utcnow())
            .astimezone(self.LOG_TIMEZONE)
            .timetuple()
        )
        return converted_time
#handler = RotatingFileHandler(LOGFILE, maxBytes=1048576, backupCount=5)

'''if __name__ == "__main__":
    import os

    sys.path.append(os.getenv("PYTHONPATH"))
    from config.general import LOGS_DIR

    InitializeLogger(
        program_type="cron",
        enable_console_logging=True,
        enable_file_logging=True,
        log_dir_path=LOGS_DIR,
        log_file_name=__file__,
    )
    logging.info("Start testing logger")
    try:
        3 / 0
    except ZeroDivisionError as zde:
        logging.exception(zde)
    logging.info("Done testing logger")
    logging.debug("Testing unhandled exception logging")
    4 + d  # Commenting for pylint
    4 + "d"  # Commenting for pylint'''
