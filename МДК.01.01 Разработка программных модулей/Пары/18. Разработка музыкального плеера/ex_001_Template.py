import sys
from PyQt6.QtWidgets import(
     QApplication, QWidget, QLabel, QPushButton  
)

from PyQt6.QtMultimedia import (
        QMediaPlayer, QAudio
)


from PyQt6.QtGui import QIcon
import pathlib

class MainWindow(QWidget):
        super().__init__()
       
        def setup_ui():
                pass

        def open_track(self):
                pass
        
        def play_track(self):
                pass

        def pause_track(self):
                pass

        def stop_track(self):
                pass

        def check_file(self):
                pass


if __name__ == "__main__":
        application = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(application.exec())