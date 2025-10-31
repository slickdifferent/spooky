import sys
import os
import random
from PyQt5.QtWidgets import QApplication, QWidget, QSystemTrayIcon, QMenu
from PyQt5.QtGui import QMovie, QPainter, QIcon, QPixmap
from PyQt5.QtCore import Qt, QPoint, QTimer
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl
from pynput import keyboard
import time

# Try to import pycaw for volume control
try:
    from ctypes import cast, POINTER
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
    VOLUME_CONTROL_AVAILABLE = True
except ImportError:
    VOLUME_CONTROL_AVAILABLE = False
    print("Volume control not available - continuing without it")

class SkeletonWindow(QWidget):
    """Individual dancing skeleton window"""
    def __init__(self, gif_path, screen_width, screen_height, parent_app):
        super().__init__()
        self.parent_app = parent_app
        self.gif_path = gif_path
        
        # Set up window properties
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        # Load the GIF animation
        self.movie = QMovie(self.gif_path)
        
        # Get the actual size from the first frame
        self.movie.jumpToFrame(0)
        pixmap = self.movie.currentPixmap()
        self.gif_width = pixmap.width()
        self.gif_height = pixmap.height()
        
        # Set window size
        self.setFixedSize(self.gif_width, self.gif_height)
        
        # Random position on screen
        x = random.randint(0, max(0, screen_width - self.gif_width))
        y = random.randint(0, max(0, screen_height - self.gif_height))
        self.move(x, y)
        
        # Connect repaint on frame change
        self.movie.frameChanged.connect(self.repaint)
        
        # Start animation at native speed
        self.movie.start()
        
        # Show the window
        self.show()
        
        print(f"Skeleton spawned at ({x}, {y})")
    
    def paintEvent(self, event):
        """Paint the current frame of the GIF"""
        painter = QPainter(self)
        current_frame = self.movie.currentPixmap()
        painter.drawPixmap(self.rect(), current_frame)
    
    def mousePressEvent(self, event):
        """When clicked, spawn another skeleton"""
        if event.button() == Qt.LeftButton:
            print("Skeleton clicked - spawning new skeleton")
            self.parent_app.spawn_skeleton()

class HalloweenPrank(QApplication):
    """Main application"""
    def __init__(self, mp3_path, gif_path):
        super().__init__(sys.argv)
        
        self.mp3_path = mp3_path
        self.gif_path = gif_path
        self.skeleton_windows = []
        self.max_skeletons = 32
        self.running = True
        
        # Get screen dimensions
        screen = self.primaryScreen().geometry()
        self.screen_width = screen.width()
        self.screen_height = screen.height()
        
        # Set up volume
        self.setup_volume()
        
        # Set up music player
        self.setup_music()
        
        # Set up keyboard listener with debouncing
        self.last_key_time = 0
        self.key_debounce_ms = 200  # 200ms debounce
        self.setup_keyboard_listener()
        
        # Set up system tray
        self.setup_tray()
        
        # Spawn first skeleton
        self.spawn_skeleton()
        
        print("🎃 Halloween Prank Started! 🎃")
        print(f"Screen: {self.screen_width}x{self.screen_height}")
        print("Click skeletons or press keys to spawn more!")
    
    def setup_volume(self):
        """Try to unmute and turn up volume"""
        if not VOLUME_CONTROL_AVAILABLE:
            print("Skipping volume control")
            return
        
        try:
            devices = AudioUtilities.GetSpeakers()
            interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
            volume = cast(interface, POINTER(IAudioEndpointVolume))
            
            # Unmute
            volume.SetMute(0, None)
            
            # Set volume to 50%
            current_volume = volume.GetMasterVolumeLevelScalar()
            if current_volume < 0.5:
                volume.SetMasterVolumeLevelScalar(0.5, None)
            
            print("Volume adjusted successfully")
        except Exception as e:
            print(f"Could not adjust volume: {e}")
    
    def setup_music(self):
        """Set up looping music playback"""
        try:
            self.music_player = QMediaPlayer()
            
            # Convert path to URL
            url = QUrl.fromLocalFile(os.path.abspath(self.mp3_path))
            content = QMediaContent(url)
            self.music_player.setMedia(content)
            
            # Connect to loop the music
            self.music_player.mediaStatusChanged.connect(self.on_media_status_changed)
            
            # Start playing
            self.music_player.play()
            print("Music started")
        except Exception as e:
            print(f"Failed to start music: {e}")
    
    def on_media_status_changed(self, status):
        """Handle music status changes - loop and spawn skeleton"""
        if status == QMediaPlayer.EndOfMedia:
            print("Music looped - spawning skeleton")
            self.spawn_skeleton()
            # Restart the music
            self.music_player.setPosition(0)
            self.music_player.play()
    
    def setup_keyboard_listener(self):
        """Set up global keyboard listener with debouncing"""
        def on_key_press(key):
            # Debounce - only trigger once per key press
            current_time = time.time() * 1000  # milliseconds
            if current_time - self.last_key_time > self.key_debounce_ms:
                self.last_key_time = current_time
                print("Key pressed - spawning skeleton")
                # Use QTimer to call spawn from main thread
                QTimer.singleShot(0, self.spawn_skeleton)
        
        try:
            self.keyboard_listener = keyboard.Listener(on_press=on_key_press)
            self.keyboard_listener.start()
            print("Keyboard listener started")
        except Exception as e:
            print(f"Failed to start keyboard listener: {e}")
    
    def setup_tray(self):
        """Set up system tray icon"""
        try:
            # Create a simple orange icon
            pixmap = QPixmap(64, 64)
            pixmap.fill(Qt.transparent)
            
            from PyQt5.QtGui import QPainter, QColor
            painter = QPainter(pixmap)
            painter.setBrush(QColor(255, 165, 0))  # Orange
            painter.drawEllipse(4, 4, 56, 56)
            painter.end()
            
            self.tray_icon = QSystemTrayIcon(QIcon(pixmap), self)
            
            # Create menu
            tray_menu = QMenu()
            quit_action = tray_menu.addAction("Quit")
            quit_action.triggered.connect(self.quit_application)
            
            self.tray_icon.setContextMenu(tray_menu)
            self.tray_icon.setToolTip("Halloween Prank")
            self.tray_icon.show()
            
            print("System tray icon created")
        except Exception as e:
            print(f"Failed to create tray icon: {e}")
    
    def spawn_skeleton(self):
        """Spawn a new skeleton window"""
        if len(self.skeleton_windows) >= self.max_skeletons:
            print(f"Max skeletons reached ({self.max_skeletons})")
            return
        
        try:
            skeleton = SkeletonWindow(
                self.gif_path,
                self.screen_width,
                self.screen_height,
                self
            )
            self.skeleton_windows.append(skeleton)
            print(f"Total skeletons: {len(self.skeleton_windows)}")
        except Exception as e:
            print(f"Error spawning skeleton: {e}")
    
    def quit_application(self):
        """Clean shutdown"""
        print("Quitting...")
        self.running = False
        
        # Stop music
        try:
            self.music_player.stop()
        except:
            pass
        
        # Stop keyboard listener
        try:
            self.keyboard_listener.stop()
        except:
            pass
        
        # Close all skeleton windows
        for skeleton in self.skeleton_windows:
            try:
                skeleton.close()
            except:
                pass
        
        # Quit application
        self.quit()

def main():
    # Get the directory where the script/exe is located
    if getattr(sys, 'frozen', False):
        application_path = sys._MEIPASS
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))
    
    mp3_path = os.path.join(application_path, 'spooky-scary-skeletons-trap.mp3')
    gif_path = os.path.join(application_path, 'skel.gif')
    
    # Check if files exist
    if not os.path.exists(mp3_path):
        print(f"ERROR: MP3 file not found: {mp3_path}")
        input("Press Enter to exit...")
        sys.exit(1)
    
    if not os.path.exists(gif_path):
        print(f"ERROR: GIF file not found: {gif_path}")
        input("Press Enter to exit...")
        sys.exit(1)
    
    print("🎃 Halloween Prank Starting... 🎃")
    
    app = HalloweenPrank(mp3_path, gif_path)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
