# Yandex Music Global Hotkeys

The standard Yandex Music's hotkeys don't work when the app is minimized, but this script allows you to use
customizable hotkeys in any other app.

## Features

- Play / Pause
- Next track
- Previous track
- Configure custom hotkeys
- Reset hotkeys via 'ctrl+alt+r'
- Automatic hotkey activation and deactivation with interface in console when **Yandex Music** is launched and closed

## Installation and manually usage

Run:

```bash
start_watcher.bat
```

## Autostart when Yandex Music launches

To make the watcher run automatically when your PC starts:

Press Win + R, type:
shell:startup

Create shortcut with the following target:

```bash
C:\Path\To\Yandex-Music-Global-Hotkeys\start_watcher.bat
```

## Notes:

- To make the global hotkeys work, manually play or pause a track in Yandex Music once.

- Run as administrator for global hotkeys to work (recommended).

- Hotkeys are saved in hotkeys_config.json.

