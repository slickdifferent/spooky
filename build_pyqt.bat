@echo off
echo ===================================
echo Halloween Prank Builder (PyQt5)
echo ===================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8 or higher from python.org
    pause
    exit /b 1
)

echo Installing dependencies...
pip install -r requirements_pyqt.txt

if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo Building executable with PyInstaller...
pyinstaller --onefile --windowed --noconsole ^
    --add-data "spooky-scary-skeletons-trap.mp3;." ^
    --add-data "skel.gif;." ^
    --icon=NONE ^
    --name "HalloweenPrank" ^
    halloween_prank_pyqt.py

if errorlevel 1 (
    echo ERROR: Build failed
    pause
    exit /b 1
)

echo.
echo ===================================
echo Build completed successfully!
echo ===================================
echo.
echo Your executable is located at:
echo dist\HalloweenPrank.exe
echo.
echo This version uses PyQt5 for better performance:
echo - Smooth GIF animations
echo - No memory crashes
echo - Faster spawning
echo - Debounced keyboard/mouse
echo.
pause
