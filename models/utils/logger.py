import logging
import os

def get_logger(script_filename, logs_root='logs', level=logging.INFO):
    """
    Set up a logger for a specific script file.
    
    - Logs will be saved in logs/{script_name}/{script_name}.log
    - Console and file logging enabled
    - Prevents duplicate handlers
    """
    # Extract script name without extension
    script_name = os.path.splitext(os.path.basename(script_filename))[0]
    
    # Define log directory and log file path
    log_dir = os.path.join(logs_root, script_name)
    log_file = os.path.join(log_dir, f'{script_name}.log')

    # Create logger
    logger = logging.getLogger(script_name)
    logger.setLevel(level)

    # Avoid adding handlers multiple times
    if logger.handlers:
        return logger

    # Ensure log directory exists
    os.makedirs(log_dir, exist_ok=True)

    # Handlers
    file_handler = logging.FileHandler(log_file)
    console_handler = logging.StreamHandler()

    # Formatters
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
