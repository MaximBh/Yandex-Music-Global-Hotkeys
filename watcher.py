import psutil
import subprocess
import time
import os
import sys

# Name of the Yandex Music process (check it in Task Manager if needed)
YANDEX_PROCESS = "Яндекс Музыка.exe"

# Path to the main hotkey script
SCRIPT_PATH = os.path.join(os.path.dirname(__file__), "main.py")

# How often to check for the Yandex Music process (in seconds)
CHECK_INTERVAL = 5


def is_running(process_name: str) -> bool:
    """Check if a process with the given name is currently running."""
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] and process_name.lower() in proc.info['name'].lower():
            return True
    return False


def kill_process_by_name(name: str):
    """Terminate all processes with the given name."""
    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name'] and name.lower() in proc.info['name'].lower():
                proc.terminate()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue


def main():
    print("Watcher started. Waiting for Yandex Music to launch...")
    hotkey_proc = None

    while True:
        # Check if Yandex Music is running
        yandex_running = is_running(YANDEX_PROCESS)

        # If Yandex Music starts and the hotkey script isn't running — start it
        if yandex_running and not hotkey_proc:
            print("Yandex Music detected — activating global hotkeys...")
            hotkey_proc = subprocess.Popen([sys.executable, SCRIPT_PATH])

        # If Yandex Music is closed — stop the hotkey script
        elif not yandex_running and hotkey_proc:
            print("Yandex Music closed — stopping hotkey script.")
            try:
                hotkey_proc.terminate()
            except Exception:
                pass
            hotkey_proc = None

        # Wait before checking again
        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Watcher stopped by user.")
    except Exception as e:
        print(f"Error: {e}")
