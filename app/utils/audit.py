import logging
import os
from datetime import datetime

LOG_FOLDER = 'logs'
LOG_FILE = 'audit.log'
os.makedirs(LOG_FOLDER, exist_ok=True)

log_path = os.path.join(LOG_FOLDER, LOG_FILE)

logging.basicConfig(
    filename=log_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def log_action(username, action, filename):
    """
    Logs user file actions.

    :param username: str - username performing the action
    :param action: str - action performed ('upload', 'delete', 'download')
    :param filename: str - affected filename
    """
    msg = f'User: {username} | Action: {action} | File: {filename}'
    logging.info(msg)
