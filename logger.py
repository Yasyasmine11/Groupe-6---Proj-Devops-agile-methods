# Logs vers App Insights
import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.addHandler(AzureLogHandler(connection_string="InstrumentationKey=xxxx"))

def log_message(msg):
    logger.info(msg)
