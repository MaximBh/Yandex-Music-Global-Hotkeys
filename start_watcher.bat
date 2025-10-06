@echo off
cd /d "%~dp0"
set VENV_DIR=venv
set PYTHON_EXE=%VENV_DIR%\Scripts\pythonw.exe
set PIP_EXE=%VENV_DIR%\Scripts\pip.exe
set REQUIREMENTS=%~dp0requirements.txt
if exist "%PYTHON_EXE%" (
    echo Virtual environment found.
) else (
    echo Virtual environment not found. Creating...
    python -m venv %VENV_DIR%
)
if exist "%PIP_EXE%" (
    echo pip found.
) else (
    echo pip not found. Installing...
    "%PYTHON_EXE%" -m ensurepip --upgrade
)
for /f "usebackq tokens=*" %%r in ("%REQUIREMENTS%") do (
    "%PYTHON_EXE%" -m pip show %%r >nul 2>&1
    if errorlevel 1 (
        echo Dependency %%r not found. Installing...
        "%PIP_EXE%" install %%r
    ) else (
        echo Dependency %%r already installed.
    )
)
echo Script ready to use.
start "" "%PYTHON_EXE%" "%~dp0watcher.py"
