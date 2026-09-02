"""
QSS стили приложения (Clean Production Version)
"""

MAIN_STYLES = """
/* ==========================================
   Ultimate Life Guide — Stylesheet v2.3
   Base: #1A1A1A | Cards: #222222 | Borders: #333333
   ========================================== */

QMainWindow { background-color: #1A1A1A; }

/* Sidebar */
QListWidget#sidebar {
    background-color: #222222;
    border-right: 1px solid #333333;
    font-size: 14px;
    color: #EEEEEE;
    outline: none;
}
QListWidget#sidebar::item { padding: 12px 15px; border-bottom: 1px solid #2A2A2A; }
QListWidget#sidebar::item:hover { background-color: #2A2A2A; }
QListWidget#sidebar::item:selected {
    background-color: #2E2E2E;
    border-left: 3px solid #4CA885;
    color: #FFFFFF;
}

/* Cards */
QFrame#statusCard {
    background-color: #222222;
    border-radius: 12px;
    padding: 15px;
    border: 1px solid transparent;
}
QFrame#statusCard:hover { background-color: #2A2A2A; border-color: #4CA885; }

QFrame#problemCard {
    background-color: #222222;
    border-radius: 8px;
    padding: 12px;
    border-left: 4px solid #E74C3C;
}
QFrame#problemCard:hover { background-color: #2A2A2A; }

QFrame#guideCard {
    background-color: #222222;
    border-radius: 8px;
    padding: 12px;
    border: 1px solid #333333;
}
QFrame#guideCard:hover { background-color: #2A2A2A; border-color: #79F7F2; }
QFrame#guideCard[completed="true"] { border-left: 4px solid #79F79C; }

/* Labels */
QLabel { color: #EEEEEE; font-size: 14px; }
QLabel#titleLabel { font-size: 18px; font-weight: bold; color: #FFFFFF; }
QLabel#subtitleLabel { font-size: 12px; color: #A0A0A0; }
QLabel#valueLabel { font-size: 24px; font-weight: bold; color: #FFFFFF; }
QLabel#trendUp   { color: #79F79C; }
QLabel#trendDown { color: #E74C3C; }
QLabel#accent    { color: #4CA885; }

/* Buttons */
QPushButton {
    background-color: #4CA885;
    color: #1A1A1A;
    border: none;
    border-radius: 6px;
    padding: 10px 20px;
    font-size: 14px;
    font-weight: bold;
}
QPushButton:hover { background-color: #79D5F7; color: #1A1A1A; }
QPushButton:pressed { background-color: #79F7F2; }
QPushButton:disabled { background-color: #333333; color: #666666; }

QPushButton#primaryButton { background-color: #4CA885; }
QPushButton#primaryButton:hover { background-color: #79D5F7; }
QPushButton#dangerButton { background-color: #E74C3C; color: #FFFFFF; }
QPushButton#dangerButton:hover { background-color: #C0392B; }
QPushButton#successButton { background-color: #79F79C; color: #1A1A1A; }
QPushButton#successButton:hover { background-color: #4CA885; }
QPushButton#infoButton { background-color: #79ADF7; color: #1A1A1A; }
QPushButton#infoButton:hover { background-color: #79D5F7; }

/* Inputs */
QLineEdit, QTextEdit {
    background-color: #222222;
    border: 1px solid #333333;
    border-radius: 6px;
    padding: 10px;
    color: #EEEEEE;
    font-size: 14px;
}
QLineEdit:focus, QTextEdit:focus { border-color: #79F7F2; }
QLineEdit::placeholder { color: #A0A0A0; }

/* Progress */
QProgressBar {
    background-color: #333333;
    border: none;
    border-radius: 4px;
    height: 8px;
    text-align: center;
    color: #EEEEEE;
    font-size: 10px;
}
QProgressBar::chunk { background-color: #4CA885; border-radius: 4px; }
QProgressBar#stressBar::chunk { background-color: #E74C3C; }
QProgressBar#energyBar::chunk { background-color: #79F79C; }
QProgressBar#xpBar::chunk     { background-color: #79D5F7; }

/* Scrollbar */
QScrollBar:vertical { background-color: #222222; width: 10px; border-radius: 5px; }
QScrollBar::handle:vertical { background-color: #333333; border-radius: 5px; min-height: 30px; }
QScrollBar::handle:vertical:hover { background-color: #4CA885; }
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0; }

/* Tabs */
QTabWidget::pane { border: 1px solid #333333; border-radius: 6px; background-color: #222222; }
QTabBar::tab {
    background-color: #333333; color: #EEEEEE;
    padding: 10px 20px; margin-right: 2px;
    border-top-left-radius: 6px; border-top-right-radius: 6px;
}
QTabBar::tab:selected { background-color: #222222; border-bottom: 2px solid #4CA885; }
QTabBar::tab:hover { background-color: #2A2A2A; }

/* ComboBox */
QComboBox {
    background-color: #222222; border: 1px solid #333333;
    border-radius: 6px; padding: 8px 12px; color: #EEEEEE;
}
QComboBox::drop-down { border: none; }
QComboBox QAbstractItemView {
    background-color: #222222; color: #EEEEEE;
    selection-background-color: #333333; border: 1px solid #333333; outline: none;
}

/* CheckBox */
QCheckBox { color: #EEEEEE; spacing: 8px; }
QCheckBox::indicator {
    width: 18px; height: 18px; border-radius: 4px;
    border: 1px solid #333333; background-color: #222222;
}
QCheckBox::indicator:checked { background-color: #4CA885; border-color: #4CA885; }

/* Slider */
QSlider::groove:horizontal { background-color: #333333; height: 6px; border-radius: 3px; }
QSlider::handle:horizontal {
    background-color: #4CA885; width: 16px; height: 16px;
    border-radius: 8px; margin: -5px 0;
}
QSlider::handle:horizontal:hover { background-color: #79D5F7; }

/* MessageBox */
QMessageBox { background-color: #222222; }
QMessageBox QLabel { color: #EEEEEE; }
QMessageBox QPushButton { min-width: 80px; }

/* Utilities */
QWidget[accent="1"] { border-left: 3px solid #4CA885; }
QWidget[accent="2"] { border-left: 3px solid #79D5F7; }
QWidget[accent="3"] { border-left: 3px solid #79F7F2; }
QWidget[accent="4"] { border-left: 3px solid #79F79C; }
QWidget[accent="5"] { border-left: 3px solid #79ADF7; }
"""