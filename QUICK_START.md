# 🎃 QUICK START GUIDE 🎃

## Building Your Halloween Prank in 3 Easy Steps:

### Step 1: Install Python
- Go to https://python.org/downloads/
- Download Python 3.8 or higher
- **IMPORTANT:** Check "Add Python to PATH" during installation

### Step 2: Run the Build Script
- Extract all files to a folder
- Double-click `build.bat`
- Wait 2-5 minutes for it to complete

### Step 3: Share the Prank
- Find the file: `dist/HalloweenPrank.exe`
- Send this file to your friends
- They can run it with just a double-click!

## Alternative: Manual Build (if build.bat doesn't work)

Open Command Prompt in the project folder and run:

```bash
# Install dependencies
pip install pygame Pillow pynput pystray pycaw comtypes pyinstaller

# Build the executable
pyinstaller --onefile --windowed --add-data "spooky-scary-skeletons-trap.mp3;." --add-data "skel.gif;." --name "HalloweenPrank" halloween_prank.py
```

The executable will be in the `dist` folder.

## Troubleshooting

**"Python is not recognized"**
- Python wasn't added to PATH
- Reinstall Python and check "Add Python to PATH"

**"pip is not recognized"**
- Same issue as above

**Antivirus blocks the .exe**
- This is normal for programs with keyboard hooks
- Add an exception in Windows Defender
- Or tell friends to click "More info" > "Run anyway"

**Build takes forever**
- First build can take 5+ minutes
- Be patient!

## What Friends Will See

When they run `HalloweenPrank.exe`:
1. Music starts playing immediately
2. A skeleton appears and dances
3. More skeletons spawn when they:
   - Click on a skeleton
   - Press any key
   - The song loops
4. To quit: Right-click orange icon in system tray > Quit

---

**Have fun and Happy Halloween! 🎃👻💀**
