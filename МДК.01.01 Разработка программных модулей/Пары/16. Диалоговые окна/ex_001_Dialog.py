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
                self.btn = QPushButton('Отправить')
                self.btn.setStyleSheet('font-size: 24px; padding: 15px 20px; background-color: #323ed7; color: white; border-radius: 15px;')
                
                self.btn.clicked.connect(self.btn_click)
         
                layout.addWidget(label)
                layout.addWidget(self.pofig)
                hlayout.addWidget(self.btn) # Кнопка для ввода имени
            
                layout.addLayout(hlayout)
                self.setLayout(layout)
        
        # Кнопка для отправки имени
        def btn_click(self):
                # Пример стандартного окна
                if self.pofig.text() != "":
                        QMessageBox.information(self, "Готово", f'Вы ввели {self.pofig.text()}')
                else:
                       QMessageBox.warning(self, "Ошибка", 'Вы ничего не поняли')

                # Пример окна с выбором
                if self.pofig.text() != "":
                        # Создаем и настраиваем окно с выбором
                        reply = QMessageBox.question(self, "Подтверждение имени", "Утвердить имя?",
                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                        
                        # Проверяем нажатую кнопку
                        if reply == QMessageBox.StandardButton.Yes:
                               print("Удалено")

                else:
                       QMessageBox.warning(self, "Ошибка", 'Вы ничего не поняли')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())