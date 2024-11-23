import requests
import time
import os
import platform

# URL of the lock status file on the web server
LOCK_STATUS_URL = "http://<WEB_SERVER_IP>/lock_status.txt"

def lock_computer():
    """Locks the computer depending on the operating system."""
    system = platform.system()
    try:
        if system == "Windows":
            os.system("rundll32.exe user32.dll,LockWorkStation")
        elif system == "Darwin":
            os.system("/System/Library/CoreServices/Menu\\ Extras/User.menu/Contents/Resources/CGSession -suspend")
        elif system == "Linux":
            os.system("gnome-screensaver-command -l")  # Adjust for your desktop environment
        else:
            print("Lock command not supported on this OS.")
    except Exception as e:
        print(f"Error locking computer: {e}")

def check_lock_status():
    """Fetches the lock status from the web server and acts accordingly."""
    try:
        response = requests.get(LOCK_STATUS_URL)
        response.raise_for_status()  # Raise an exception for HTTP errors
        status = response.text.strip().lower()
        return status == "locked"
    except requests.RequestException as e:
        print(f"Error fetching lock status: {e}")
        return False

def main():
    locked = False
    while True:
        # Check the lock status from the web server
        new_status = check_lock_status()

        if new_status and not locked:
            print("Locking the computer...")
            lock_computer()
            locked = True
        elif not new_status and locked:
            print("Computer is unlocked remotely.")
            locked = False

        time.sleep(1)  # Check the lock status every second

if __name__ == "__main__":
    main()
