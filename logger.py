# Import the logging module for recording events
import logging
# Import datetime module (currently unused - can be removed)
from datetime import datetime

# Configure logging to write to a file with timestamp and message format
logging.basicConfig(
    filename="scan_results.log",  # Output file name
    level=logging.INFO,  # Log level threshold
    format="%(asctime)s - %(message)s"  # Log message format with timestamp
)

# Function to log port scan results
def log_result(host, port, status):
    """Log the scan result for a given host and port."""
    logging.info(f"{host} | Port {port} | {status}")
