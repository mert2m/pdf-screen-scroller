import pyautogui
import time

def auto_scroll(interval):
    try:
        while True:
            pyautogui.scroll(-3)  # Scroll down
            time.sleep(interval)  # Wait for the specified interval
    except KeyboardInterrupt:
        print("Scrolling stopped.")

# Call the function with a 3-second interval
auto_scroll(3)
