from datetime import datetime
import time

def get_system_time(format_12hr: bool = False) -> str:
    """Returns the current system time formatted as a string."""
    fmt = "%I:%M:%S %p" if format_12hr else "%H:%M:%S"
    return datetime.now().strftime(fmt)

def get_timestamp() -> float:
    """Returns the current Unix epoch timestamp."""
    return time.time()

if __name__ == "__main__":
    # Example usage:
    print("24-Hour Time:", get_system_time())
    print("12-Hour Time:", get_system_time(format_12hr=True))
    print("Timestamp:   ", get_timestamp())