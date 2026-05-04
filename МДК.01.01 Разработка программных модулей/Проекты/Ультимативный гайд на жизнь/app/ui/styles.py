# QSS-стили приложения

MAIN_STYLES = """

/* Главные стили */
QMainWindow{
    background-color: #404040;
}

/* Боковое меню(Sidebar) */
QListWidget#sidebar{
    background-color: # 1A1A1A; 
    border-right: 1px solid #0F3460;
    font-size: 14px;
    color: #EEEEEE;
}

/* Элементы меню */
QListWidget#sidebar::item{
    padding: 12px 15px;
    border-bottom: 1px solid rgba(15, 52, 96, 0.5);
}

/* Наведение на элемент меню */
QListWidget#sidebar::item:hover{
    background-color: rgba(76, 168, 133, 0.5);
}

/* Эффект на текущую вкладку */
QListWidget#sidebar::item:selected{
    background-color: #4CA885;
    border-left: 3px solid #79F7F2;
}

/* Карточки статусов */
QFrame#statusCard{
    background-color: #16213E;
    border-radius: 12px;
    padding: 15px;
}

QFrame#statusCard:hover{
    background-color: #1A2744;
}

/* Карточки проблем */
QFrame#problemCard{
    background-color: #16213E;
    border-radius: 8px;
    border-left: 4px solid #FF6B6B;
    padding: 12px;
}

QFrame#problemCard:hover{
    background-color: #1A2744;
}

/* Карточки гайдов */
QFrame#guideCard{
    background-color: #16213E;
    border-radius: 8px;
    padding: 12px;
    border: 1px solid #3F3460;
}

QFrame#guideCard:hover{
    background-color: #1A2744;
    border-color: #4ECDC4;
}

/* Стилизация QLabel */
QLabel{
    color: #EEEEEE;
    font-size: 14px;
}

QLabel#titleLabel{
    font-size: 18px;
    font-weight: bold;
    color: #FFFFFF;
}

QLabel#subtitleLabel{
    font-size: 12px;
    color: #A0A0A0;
}

QLabel#valueLabel{
    font-size: 24px;
    font-weight: bold;
    color: #FFFFFF;
}

QLabel#trendUp{
    color: #00B894;
}

QLabel#trendDown{
    color: #E74C3C;
}

/* Стилизация QPushButton */
QPushButton{
    background-color: #4ECDC4;
    color: #1A1A2E;
    border: none;
    border-radius: 6px;
    padding: 10px 20px;
    font-size: 14px;
    font-weight: bold;
}

QPushButton:hover{
    background-color: #45B7D1;
}

QPushButton:pressed{
    background-color: #3AA8C4;
}

QPushButton#primaryButton{
    background-color: #4ECDC4;
}

QPushButton#dangerButton{
    background-color: #E74C3C;
    color: #FFFFFF;
}

QPushButton#dangerButton:hover{
    background-color: #C0392B;
}

QPushButton#successButton{
    background-color: #00B894;
}

QPushButton#successButton:hover{
    background-color: #00A885;
}

/* Стилизация QLineEdit */
QLineEdit{
    background-color: #16213E;
    border: 1px solid #0F3460;
    border-radius: 6px;
    padding: 10px;
    color: #EEEEEE;
    font-size: 14px;
}

QLineEdit:focus{
    border-color: #4ECDC4;
}

QLideEdit:placeholder{
    color: #A0A0A0;
}

/* Стилизация QTextEdit */
QTextEdit{
    background-color: #16213E;
    border: 1px solid #0F3460;
    border-radius: 6px;
    padding: 10px;
    color: #EEEEEE;
    font-size: 14px;
}

QTextEdit:focus{
    border-color: #4ECDC4;
}

/* Стилизация QProgressBar */
QProgressBar{
    background-color: #0F3460;
    border: none;
    border-radius: 4px;
    height: 8px;
    text-align: center;
}

QProgress::chunk{
    background-color: #4ECDC4;
    border-radius: 4px;
}

QProgressBar#stressBar::chunk{
    background-color: #E74C3C;
}

QProgressBar#energyBar::chunk{
    background-color: #00B894;
}

QProgressBar#xpBar::chunk{
    background-color: #FFEAA7;
}

/* Стилизация QScrollBar */
QScrollBar:vertical{
    background-color: #16213E;
    width: 10px;
    border-radius: 5px;
}

QScrollBar::handle:vertical{
    background-color: #0F3460;
    border-radius: 5px;
    min-height: 30px;
}

QScrollBar::handle:vertical:hover{
    background-color: #1A744;
}

QScrollBar::add-line:vertical,
QScrollBar::sub-line:vertical{
    height: 0;
}

/* Стилизация QTab */
QTabWidget::pane{
    border: 1px solid #0F3460;
    border-radius: 6px;
    background-color: #16213E;
}

QTabBar::tab{
    background-color: #0F3460;
    color: #EEEEEE;
    padding: 10px 20px; 
    margin-right: 2px;
    border-top-left-radius: 6px;
    border-top-right-radius: 6px;
}

QTabBar::tab:selected{
    background-color: #16213E;
    border-bottom: 2px solid #4ECDC4;
}

QTabBar::tab:hover{
    background-color: #1A2744;
}

/* Стилизация QCombobox */
QComboBox{
    background-color: #16213E;
    border: 1px solid #0F3460;
    border-radius: 6px;
    padding: 8px 12px;
    color: #EEEEEE;
}

QComboBox::drop-down{
    border: none;
}

QComboBox OAbstractItemView{
    background-color: #16213E;
    color: #EEEEEE;
    selection-background-color: #0F3460;
    border: 1px solid #0F3460;
}

/* Стилизация QCheckBox */
QCheckBox{
    color: #EEEEEE;
    spacing: 8px;
}

QCheckBox::indicator{
    width: 18px;
    height: 18px;
    border-radius: 4px;
    border: 1px solid #0F3460;
    background-color: #16213E;
}

QCheckBox::indicator:checked{
    background-color: #4ECDC4;
    border-color #4ECDC4;
}

/* QSlider */
QSlider::grove:horizontal{
    background-color: #0F3460;
    height: 6px;
    border-radius: 3px;
}

QSlider::handle:horizontal{
    background-color: #4ECDC4;
    width: 16px;
    height: 16px;
    border-radius: 8px;
    margin: -5px 0;
}

QSlider::handle:horizontal:hover{
    background-color: #45B7D1;
}

/* Стилизация QMessageBox */
QMessageBox{
    background-color: #16213E;
}

QMessageBox QLabel{
    color: #EEEEEE;
}

QMessageBox QPushButton{
    min-width: 80px;
}
"""