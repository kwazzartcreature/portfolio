import logging
import os

logging.basicConfig(
    level=logging.DEBUG if os.Getenv("DEBUG") == "true" else logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
