import time
import logging
import random
import os
from datetime import datetime

logging.basicConfig(level=logging.INFO)

container_name = os.getenv("CONTAINER_NAME", "unknown-container")
counter = 1

while True:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logging.info(f"[{container_name}] [{timestamp}] [#{counter}]")
    counter += 1
    time.sleep(5)


