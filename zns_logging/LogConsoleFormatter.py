import logging

from colorama import init, Fore, Style

from .LogUtility import log_and_raise

init(autoreset=True)

_LEVEL_COLORS = {
    "DEBUG": Fore.BLUE,
    "INFO": Fore.GREEN,
    "WARNING": Fore.YELLOW,
    "ERROR": Fore.RED,
    "CRITICAL": Fore.MAGENTA,
}

class LogConsoleFormatter(logging.Formatter):
    def __init__(
        self,
        level_colors: dict[str, str],
        color_name: str,
        color_message: str,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)

        if level_colors and not isinstance(level_colors, dict):
            log_and_raise(name=__name__, message="[level_colors] must be a dictionary", exception_type=ValueError)

        self.level_colors = level_colors
        self.color_name = color_name
        self.color_message = color_message

    def format(self, record: logging.LogRecord) -> str:
        record.levelname = f"{self.level_colors.get(record.levelname, Fore.RESET)}{record.levelname:8}{Style.RESET_ALL}"
        record.name = f"{self.color_name}{record.name}{Style.RESET_ALL}"
        record.msg = f"{self.color_message}{record.msg}{Style.RESET_ALL}"

        return super().format(record)
