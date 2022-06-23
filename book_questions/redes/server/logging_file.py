import logging

formatter_cmd = logging.Formatter('%(levename)s:%(asctime)s: %(message)s')
formatter_file = logging.Formatter('%(asctime)s: %(message)s')
logger = logging.getLogger(__name__)

file_handler = logging.FileHandler('cups_printers.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter_file)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter_cmd)
stream_handler.setLevel(logging.CRITICAL)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

