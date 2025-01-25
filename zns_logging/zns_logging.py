import logging
from logging.handlers import RotatingFileHandler

from colorama import Fore

from .LogConsoleFormatter import LogConsoleFormatter

_DATE_FORMAT_STR = "%Y-%m-%d %H:%M:%S"

_FILE_FORMAT_STR = "[%(asctime)s] [%(levelname)-8s] [%(name)s]: %(message)s"
_FILE_MODE = "a"
_FILE_MAX_BYTES = 1024 * 1024
_FILE_BACKUP_COUNT = 4
_FILE_ENCODING = "utf-8"

_CONSOLE_FORMAT_STR = "[{asctime}] [{levelname}] [{name}]: {message}"
_COLOR_NAME = Fore.CYAN
_COLOR_MESSAGE = Fore.RESET
_LEVEL_COLORS = {
    "DEBUG": Fore.BLUE,
    "INFO": Fore.GREEN,
    "WARNING": Fore.YELLOW,
    "ERROR": Fore.RED,
    "CRITICAL": Fore.MAGENTA,
}

_ENABLE_FILE_LOGGING = True
_ENABLE_CONSOLE_LOGGING = True


def get_logger(
    logger_name: str,
    logging_level: int | str = logging.INFO,
    date_format_str: str = _DATE_FORMAT_STR,
    file_format_str: str = _FILE_FORMAT_STR,
    file_path: str = None,
    file_mode: str = _FILE_MODE,
    file_max_bytes: int = _FILE_MAX_BYTES,
    file_backup_count: int = _FILE_BACKUP_COUNT,
    file_encoding: str = _FILE_ENCODING,
    console_format_str: str = _CONSOLE_FORMAT_STR,
    color_name: str = _COLOR_NAME,
    color_message: str = _COLOR_MESSAGE,
    level_colors: dict[str, str] = None,
    enable_file_logging: bool = _ENABLE_FILE_LOGGING,
    enable_console_logging: bool = _ENABLE_CONSOLE_LOGGING,
) -> logging.Logger:
    logger = logging.getLogger(name=logger_name)
    logger.setLevel(level=logging_level)

    if enable_file_logging and file_path:
        file_path = file_path if file_path.endswith(".log") else f"{file_path}.log"
        file_handler = RotatingFileHandler(
            filename=file_path,
            mode=file_mode,
            maxBytes=file_max_bytes,
            backupCount=file_backup_count,
            encoding=file_encoding,
        )
        file_formatter = logging.Formatter(
            fmt=file_format_str,
            datefmt=date_format_str,
        )
        file_handler.setFormatter(fmt=file_formatter)
        logger.addHandler(hdlr=file_handler)

    if enable_console_logging:
        console_handler = logging.StreamHandler()

        level_colors = level_colors or _LEVEL_COLORS

        console_formatter = LogConsoleFormatter(
            level_colors=level_colors,
            color_name=color_name,
            color_message=color_message,
            fmt=console_format_str,
            datefmt=date_format_str,
            style="{",
        )
        console_handler.setFormatter(fmt=console_formatter)
        logger.addHandler(hdlr=console_handler)

    return logger


__all__ = ["get_logger"]
