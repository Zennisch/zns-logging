import logging

from colorama import Fore, Style, init

init(autoreset=True)

class LogConsoleFormatter(logging.Formatter):
    def __init__(
        self,
        color_name: str,
        color_message: str,
        color_levelname: dict[str, str],
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.color_name = color_name
        self.color_message = color_message
        self.color_levelname = color_levelname or {
            "DEBUG": Fore.BLUE,
            "INFO": Fore.GREEN,
            "WARNING": Fore.YELLOW,
            "ERROR": Fore.RED,
            "CRITICAL": Fore.MAGENTA,
        }

    def format(self, record: logging.LogRecord) -> str:
        record.name = f"{self.color_name}{record.name}{Style.RESET_ALL}"
        record.msg = f"{self.color_message}{record.msg}{Style.RESET_ALL}"
        record.levelname = (
            f"{self.color_levelname.get(record.levelname, Fore.WHITE)}"
            f"{record.levelname:<8}"
            f"{Style.RESET_ALL}"
        )

        return super().format(record)
