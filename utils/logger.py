import logging
from datetime import datetime

from utils.constants import LOG_DIR

#logging 
#log  should be store with date and time


def setup_logger():

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    log_file = LOG_DIR / f"run_{timestamp}.txt"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler(),
        ],
    )

    return logging.getLogger(__name__)