import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QListWidget, QLineEdit, QVBoxLayout, QHBoxLayout,
    QComboBox, QPushButton, QMessageBox, QInputDialog, QFileDialog
)

class MainWindow(QWidget):
        def __init__(self):
                super().__init__()
                layout = QVBoxLayout()
                hlayout = QHBoxLayout()
                
                label = QLabel("Кароче пофиг")
                label.setStyleSheet('font-size: 24px; margin-bottom: 15px;')
                
                self.pofig = QLineEdit()
                self.pofig.setStyleSheet('font-size: 24px; ')                

                self.rename_btn = QPushButton('Переименовать')
                self.rename_btn.setStyleSheet('font-size: 24px; padding: 15px 20px; background-color: #3f9654; color: white; border-radius: 15px;')

                self.btn.clicked.connect(self.btn_click)
                self.rename_btn.clicked.connect(self.new_name)
                self.file_btn.clicked.connect(self.load_file)
                layout.addWidget(label)
                layout.addWidget(self.pofig)
                hlayout.addWidget(self.rename_btn) # Кнопка для переименования
                layout.addLayout(hlayout)
                self.setLayout(layout)
                
        # Кнопка для смены имени
        def new_name(self):
              text, ok = QInputDialog.getText(
                     self, "Новое имя", "Введите название: "
              ) 
              if ok and text:
                     self.pofig.setText(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())