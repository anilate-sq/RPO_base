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

                self.file_btn = QPushButton('Загрузить файл')
                self.file_btn.setStyleSheet('font-size: 24px; padding: 15px 20px; background-color: #963f81; color: white; border-radius: 15px;')
                self.btn.clicked.connect(self.btn_click)
                self.rename_btn.clicked.connect(self.new_name)
                self.file_btn.clicked.connect(self.load_file)
                layout.addWidget(label)
                layout.addWidget(self.pofig)
                hlayout.addWidget(self.file_btn) # Кнопка для загрузки файла
                layout.addLayout(hlayout)
                self.setLayout(layout)
                
        # Кнопка для загрузки файла
        def load_file(self):
               file_path, _ = QFileDialog.getOpenFileName(
                      self,
                      "Открыть файл",
                      "",
                      "Все файлы (*.*)"
               )
               with open(file_path, "r", encoding='UTF-8') as file:
                      print(file.read())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())