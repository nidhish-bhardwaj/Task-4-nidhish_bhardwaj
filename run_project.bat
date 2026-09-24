@echo off
cd /d "%~dp0"
echo Installing required Python packages...
python -m pip install -r requirements.txt
if errorlevel 1 (
    echo.
    echo Package installation failed.
    pause
    exit /b 1
)
echo.
echo Running AI Project 4 - OCR...
python main.py
pause
