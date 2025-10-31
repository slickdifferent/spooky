"""
Quick test to verify all dependencies can be imported
Run this before building to catch any issues early
"""

print("Testing imports...")

try:
    import tkinter as tk
    print("✓ tkinter")
except ImportError as e:
    print(f"✗ tkinter: {e}")

try:
    import pygame
    print("✓ pygame")
except ImportError as e:
    print(f"✗ pygame: {e}")

try:
    from PIL import Image, ImageTk, ImageSequence
    print("✓ Pillow (PIL)")
except ImportError as e:
    print(f"✗ Pillow: {e}")

try:
    from pynput import mouse, keyboard
    print("✓ pynput")
except ImportError as e:
    print(f"✗ pynput: {e}")

try:
    import pystray
    print("✓ pystray")
except ImportError as e:
    print(f"✗ pystray: {e}")

try:
    from ctypes import cast, POINTER
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
    print("✓ pycaw (Windows audio control)")
except ImportError as e:
    print(f"⚠ pycaw (optional): {e}")

import os
print("\nChecking files...")
if os.path.exists('spooky-scary-skeletons-trap.mp3'):
    print("✓ MP3 file found")
else:
    print("✗ MP3 file missing")

if os.path.exists('skel.gif'):
    print("✓ GIF file found")
else:
    print("✗ GIF file missing")

print("\n✅ All critical dependencies ready!")
print("You can now run build.bat to create the executable")
