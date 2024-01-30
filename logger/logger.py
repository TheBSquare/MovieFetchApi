
from __future__ import annotations
import loguru
import sys
from loguru import logger as _logger

from config import LOGS_PATH, LOG_LEVEL


log: loguru.Logger | None = None

if log is None:
    fmt = "<g>{time}</> | <lvl>{level}</> | <c>{extra[classname]}:{function}:{line}</> - {message}"
    _logger.remove()
    _logger.configure(extra={"classname": "None"})
    _logger.add(LOGS_PATH, backtrace=True, diagnose=True, level="INFO", format=fmt, rotation="1 day")
    _logger.add(sys.stdout, backtrace=True, diagnose=True, level=LOG_LEVEL, format=fmt)
    _logger.info("Started logging successfully")
    log = _logger
