import psutil
import subprocess
import time
import os

YANDEX_PROCESS = "Яндекс Музыка.exe"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MAIN_SCRIPT = os.path.join(BASE_DIR, "main.py")
CHECK_INTERVAL = 5


def is_running(process_name: str) -> bool:
    """Check if a process with the given name is running."""
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] and process_name.lower() in proc.info['name'].lower():
            return True
    return False


def main():
    print("Watcher started. Waiting for Yandex Music...")
    main_proc = None

    while True:
        yandex_running = is_running(YANDEX_PROCESS)

        # Start main.py in console
        if yandex_running and main_proc is None:
            print("Yandex Music detected — starting main script...")
            cmd_command = f'start "Yandex Hotkeys" cmd /k python "{MAIN_SCRIPT}"'
            main_proc = subprocess.Popen(cmd_command, shell=True)

        # Kill console when Yandex Music closes
        elif not yandex_running and main_proc is not None:
            print("Yandex Music closed — closing console...")
            try:
                # Kill only processes started by watcher
                for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
                    if proc.info['name'] == "cmd.exe" and any(
                            "main.py" in str(arg) for arg in proc.info.get("cmdline", [])):
                        proc.terminate()
                    if proc.info['name'] == "python.exe" and any(
                            "main.py" in str(arg) for arg in proc.info.get("cmdline", [])):
                        proc.terminate()
            except Exception:
                pass
            main_proc = None

        time.sleep(CHECK_INTERVAL)


if __name__ == "__main__":
    main()
