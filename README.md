# Yandex Music Global Hotkeys

The standard Yandex Music's hotkeys dont't work when the app is minimized, but this script allows you to use customizable hotkeys in any other app.

## Features
- Play / Pause
- Next track
- Previous track
- Configure custom hotkeys
- Reset hotkeys via 'r' or command line argument `--reset`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/MaximBh/Yandex_Music_Global_Hotkeys.git
cd Yandex_Music_Global_Hotkeys
```
2. Create a virtual environment (recommended):
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```
## Usage:
```bash
python main.py        # Start the script
```
## Notes:
- Run as administrator for global hotkeys to work (recommended).
- Hotkeys are saved in hotkeys_config.json.