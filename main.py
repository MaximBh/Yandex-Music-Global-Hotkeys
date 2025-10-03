import keyboard
import win32gui
import win32api
import json
import os
import sys

WM_APPCOMMAND = 0x0319

APPCOMMAND_MEDIA_NEXTTRACK = 11
APPCOMMAND_MEDIA_PREVIOUSTRACK = 12
APPCOMMAND_MEDIA_PLAY_PAUSE = 14

CONFIG_FILE = "hotkeys_config.json"

def enum_windows_callback(hwnd, windows):
    title = win32gui.GetWindowText(hwnd)
    if "Яндекс Музыка" in title:
        windows.append(hwnd)

def find_yandex_music_window():
    windows = []
    win32gui.EnumWindows(enum_windows_callback, windows)
    return windows[0] if windows else None

def send_media_command(command):
    hwnd = find_yandex_music_window()
    if hwnd:
        win32api.SendMessage(hwnd, WM_APPCOMMAND, hwnd, command << 16)
    else:
        print("Yandex Music window not found")

default_hotkeys = {
    "Play/Pause": "ctrl+alt+space",
    "Next": "ctrl+alt+right",
    "Previous": "ctrl+alt+left"
}

def configure_hotkeys():
    print("\nConfigure hotkeys for Yandex Music control.")
    print("Press Enter to keep the default value.\n")
    user_hotkeys = {}
    for action, default in default_hotkeys.items():
        hk = input(f"Enter hotkey for {action} (default {default}): ").strip()
        user_hotkeys[action] = hk if hk else default
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(user_hotkeys, f, indent=4, ensure_ascii=False)
    return user_hotkeys

def register_hotkeys(user_hotkeys):
    keyboard.add_hotkey(user_hotkeys["Play/Pause"], lambda: send_media_command(APPCOMMAND_MEDIA_PLAY_PAUSE))
    keyboard.add_hotkey(user_hotkeys["Next"], lambda: send_media_command(APPCOMMAND_MEDIA_NEXTTRACK))
    keyboard.add_hotkey(user_hotkeys["Previous"], lambda: send_media_command(APPCOMMAND_MEDIA_PREVIOUSTRACK))
    print("\nHotkeys are now active:")
    for action, hotkey in user_hotkeys.items():
        print(f"{hotkey} = {action}")

def reset_hotkeys():
    keyboard.clear_all_hotkeys()
    user_hotkeys = configure_hotkeys()
    register_hotkeys(user_hotkeys)

# --- Main ---
reset_mode = "--reset" in sys.argv

if reset_mode or not os.path.exists(CONFIG_FILE):
    user_hotkeys = configure_hotkeys()
else:
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        user_hotkeys = json.load(f)

register_hotkeys(user_hotkeys)
keyboard.add_hotkey("r", reset_hotkeys)

print("\nPress 'r' at any time to reset hotkeys.")
print("Press Ctrl+C to exit.")
keyboard.wait()
