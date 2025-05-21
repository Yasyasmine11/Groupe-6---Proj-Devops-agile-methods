import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler

logger = logging.getLogger(__name__)

# Configuration pour le développement local (sans Azure)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# logger.addHandler(AzureLogHandler(connection_string="InstrumentationKey=xxxx"))

def log_message(message, level="info"):
    """Log un message avec le niveau spécifié"""
    if level.lower() == "info":
        logger.info(message)
    elif level.lower() == "warning":
        logger.warning(message)
    elif level.lower() == "error":
        logger.error(message)
    elif level.lower() == "debug":
        logger.debug(message)