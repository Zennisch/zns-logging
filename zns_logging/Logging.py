import logging
import logging.handlers

from colorama import Fore

from zns_logging.LogConsoleFormatter import LogConsoleFormatter

_date_format_str = "%Y-%m-%d %H:%M:%S"

_file_format_str = "[%(asctime)s] [%(levelname)-8s] [%(name)s]: %(message)s"
_file_mode = "a"
_file_max_bytes = 1024 * 1024
_file_backup_count = 4
_file_encoding = "utf-8"

_console_format_str = "[{asctime}] [{levelname}] [{name}]: {message}"
_color_name = Fore.CYAN
_color_message = Fore.WHITE

def get_logger(
    logger_name: str,
    logging_level: int | str = logging.INFO,
    date_format_str: str = _date_format_str,
    file_format_str: str = _file_format_str,
    file_path: str = None,
    file_mode: str = _file_mode,
    file_max_bytes: int = _file_max_bytes,
    file_backup_count: int = _file_backup_count,
    file_encoding: str = _file_encoding,
    console_format_str: str = _console_format_str,
    color_name: str = _color_name,
    color_message: str = _color_message,
    color_levelname: dict[str, str] = None,
) -> logging.Logger:
    logger = logging.getLogger(name=logger_name)
    logger.setLevel(level=logging_level)

    if file_path:
        file_path = file_path if file_path.endswith(".log") else f"{file_path}.log"
        print(f"Logging to file: {file_path}")
        file_handler = logging.handlers.RotatingFileHandler(
            filename=file_path,
            mode=file_mode,
            maxBytes=file_max_bytes,
            backupCount=file_backup_count,
            encoding=file_encoding,
        )
        file_formatter = logging.Formatter(fmt=file_format_str, datefmt=date_format_str)
        file_handler.setFormatter(fmt=file_formatter)
        logger.addHandler(hdlr=file_handler)

    console_handler = logging.StreamHandler()
    console_formatter = LogConsoleFormatter(
        color_name=color_name,
        color_message=color_message,
        color_levelname=color_levelname,
        fmt=console_format_str,
        datefmt=date_format_str,
        style="{",
    )
    console_handler.setFormatter(fmt=console_formatter)
    logger.addHandler(hdlr=console_handler)

    return logger
