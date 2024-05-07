import logging
from pathlib import Path


# Configure logging settings
def configure_logging():
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )


# Function to provide consistent access to configurations
def get_root_path():
    return str(Path(__file__).resolve().parents[1])


