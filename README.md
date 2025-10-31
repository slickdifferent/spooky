# 🎃 Halloween Prank Program 🎃

A spooky Halloween prank that plays music and spawns dancing skeleton GIFs all over the screen!

## What It Does

- 🔊 Automatically unmutes and turns up system volume
- 🎵 Plays "Spooky Scary Skeletons" on loop
- 👻 Spawns transparent skeleton GIFs on top of all windows
- 🖱️ Clicking any skeleton spawns another one
- ⌨️ Pressing any key spawns another one
- 🔁 Each time the song loops, another skeleton appears
- 📊 Maximum of 32 skeletons at once
- 🚪 System tray icon to quit when you've had enough

## Building the Executable

### Prerequisites
- Windows 10 or Windows 11
- Python 3.8 or higher (download from python.org)
- Internet connection (for downloading dependencies)

### Build Steps

1. **Place all files in the same folder:**
   - `halloween_prank.py`
   - `spooky-scary-skeletons-trap.mp3`
   - `skel.gif`
   - `requirements.txt`
   - `build.bat`

2. **Run the build script:**
   - Double-click `build.bat`
   - Wait for installation and build to complete (may take 2-5 minutes)
   - The executable will be created in the `dist` folder

3. **Share with friends:**
   - The file `dist/HalloweenPrank.exe` is your standalone executable
   - This single file can be shared - no installation needed!
   - File size will be approximately 30-50 MB

## Usage

1. **Run the program:**
   - Double-click `HalloweenPrank.exe`
   - The music will start immediately
   - Skeletons will begin appearing on screen

2. **To quit:**
   - Look for the orange icon in your system tray (bottom-right of taskbar)
   - Right-click the icon
   - Select "Quit"

## ⚠️ Important Warnings

### Antivirus False Positives
Your antivirus or Windows Defender may flag this program because it:
- Uses global keyboard/mouse hooks
- Creates transparent overlay windows
- Modifies system audio

**This is a false positive!** The program is completely safe. To run it:
- Windows may show "Windows protected your PC" - click "More info" then "Run anyway"
- You may need to add an exception in Windows Defender
- On some systems, temporarily disable real-time protection

### For Your Friends
Warn your friends that:
- Their antivirus might complain (this is normal)
- The program will unmute their computer
- They'll need to find the system tray icon to quit
- It's just a harmless prank!

## Troubleshooting

**Music doesn't play:**
- Check that your speakers are connected
- Try running as administrator (right-click > Run as administrator)

**Volume doesn't unmute:**
- This is OK - the program will continue without crashing
- Manually unmute your speakers

**Build fails:**
- Make sure Python is added to PATH during installation
- Try running Command Prompt as administrator
- Check that all files are in the same folder

**Skeletons don't appear:**
- Check if Windows transparency effects are enabled
- Try restarting the program

## Technical Details

**Dependencies:**
- pygame: Audio playback
- Pillow: GIF animation
- pynput: Global keyboard/mouse events
- pystray: System tray icon
- pycaw: Windows audio control
- tkinter: Transparent windows (built-in)

**How it's packaged:**
- PyInstaller bundles Python + all libraries + assets into one .exe
- Uses `--onefile` for single executable
- Uses `--windowed` to hide console window
- Assets are extracted to temp folder at runtime

## License

Free to use for personal pranks. Have fun and Happy Halloween! 🎃

---

**Remember:** Always get permission before pranking someone's computer!
