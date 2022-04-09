from logging.config import dictConfig
import logging
from log_config import LogConfig

dictConfig(LogConfig().dict())
logger = logging.getLogger("server")

