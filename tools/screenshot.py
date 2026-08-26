import os
import time
from PIL import ImageGrab

def take_screenshot(filename=None):
    """
    Takes a screenshot of the main screen and saves it to the user's Desktop.
    """
    try:
        # Get the path to the user's desktop
        desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
        
        # Generate a default filename if none provided
        if not filename:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"
            
        # Ensure it ends with .png
        if not filename.lower().endswith('.png'):
            filename += '.png'
            
        filepath = os.path.join(desktop, filename)
        
        # Capture the screen and save
        screenshot = ImageGrab.grab()
        screenshot.save(filepath)
        
        return f"Successfully saved screenshot to {filepath}"
    except Exception as e:
        return f"Failed to take screenshot: {str(e)}"
