# Yandex Music Global Hotkeys

The standard Yandex Music's hotkeys dont't work when the app is minimized, but this script allows you to use
customizable hotkeys in any other app.

## Features

- Play / Pause
- Next track
- Previous track
- Configure custom hotkeys
- Reset hotkeys via 'ctrl+alt+r'
- Automatic hotkey activation when **Yandex Music.exe** is launched

## Installation

1. Clone the repository:

```bash
git clone https://github.com/MaximBh/Yandex-Music-Global-Hotkeys.git
cd Yandex-Music-Global-Hotkeys
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a virtual environment (optional):

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

## Usage:

Run manually:

```bash
python main.py        # Start the script
```

Or use the automatic watcher:

```bash
python watcher.py       # Start the script
```

## Autostart on Windows

To make the watcher run automatically when your PC starts:

Press Win + R, type:
shell:startup

Create shortcuts with the following targets:

"C:\Path\To\Python\pythonw.exe"
"C:\Path\To\Yandex-Music-Global-Hotkeys\start_watcher.bat"

## Notes:

- To make the global hotkeys work, manually play or pause a track in Yandex Music once

- Run as administrator for global hotkeys to work (recommended).

- Hotkeys are saved in hotkeys_config.json.

