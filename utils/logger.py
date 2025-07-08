import logging
import os

def get_logger(name='my_logger', log_file='app.log', level=logging.INFO):
    """Function to setup a logger that logs to both console and file."""
    
    # Create a custom logger
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Avoid duplicate handlers if logger is called multiple times
    if logger.handlers:
        return logger

    # Create log directory if it doesn't exist
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    # Create handlers
    file_handler = logging.FileHandler(log_file)
    console_handler = logging.StreamHandler()

    # Set log level for handlers
    file_handler.setLevel(level)
    console_handler.setLevel(level)

    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    # Add formatter to handlers
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
