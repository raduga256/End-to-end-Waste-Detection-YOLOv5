# Helper Function

import logging
import os
from datetime import datetime
from from_root import from_root

# create logging string-name format
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%S')}.log" #log datime for action 

# Create path to log file folder
log_path = os.path.join(from_root(), 'log', LOG_FILE) #create log if not exits and save logs to it

# Create a *log* directory folder
os.makedirs(log_path, exist_ok=True)

# Define log file path
LOG_FILE_PATH = os.path.join(log_path, LOG_FILE)

# Configure Custom logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(name)s : %(levelname)s : %(message)s",
    level=logging.INFO
)

# test logging by executing app.py file
