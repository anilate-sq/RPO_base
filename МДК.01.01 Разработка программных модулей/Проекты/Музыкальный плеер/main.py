# Импортируем необходимые модули
import sys          # Модуль для работы с системными параметрами
import os           # Модуль для взаимодействия с операционной системой
from pathlib import Path  # Класс для работы с путями к файлам

# Импортируем виджеты и компоненты PyQt6 для создания GUI
from PyQt6.QtWidgets import (
    QApplication,    # Главный класс приложения PyQt
    QWidget,         # Базовый класс для виджетов
    QPushButton,    # Кнопка
    QSlider,        # Ползунок для регулировки значений
    QLabel,         # Надпись (лейбл)
    QVBoxLayout,    # Вертикальный слой для размещения элементов
    QHBoxLayout,    # Горизонтальный слой для размещения элементов
    QFileDialog,    # Диалоговое окно для выбора файлов
    QSizePolicy,    # Класс для управления политикой изменения размера
    QSpacerItem     # Элемент-разделитель для выравнивания
)

# Импортируем дополнительные компоненты PyQt6
from PyQt6.QtCore import Qt, QUrl, QTimer, QSize  # Основные классы Qt: перечисления, URL, таймер, размеры
from PyQt6.QtGui import QIcon                     # Класс для работы с иконками
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput  # Классы для воспроизведения аудио

# Определяем пути к директориям проекта
BASE_DIR = Path(__file__).resolve().parent  # Получаем путь к текущему файлу и его родительскую директорию
AUDIO_DIR = BASE_DIR / "media" / "audio"    # Путь к папке с аудиофайлами
ICON_DIR = BASE_DIR / "assets" / "icons"    # Путь к папке с иконками

class PlayerUI(QWidget):
    """
    Класс главного окна плеера
    Наследуется от QWidget - базового класса для всех объектов пользовательского интерфейса
    """
    def __init__(self):
        super().__init__()  # Вызываем конструктор родительского класса

        # Устанавливаем заголовок окна и минимальный размер
        self.setWindowTitle("MP3 Плеер (PyQt6)")
        self.setMinimumSize(600, 400)

        # Создаем директорию для аудиофайлов, если она не существует
        AUDIO_DIR.mkdir(parents=True, exist_ok=True)

        # Создаем объекты для воспроизведения аудио
        self.player = QMediaPlayer()      # Объект для воспроизведения медиафайлов
        self.audio_output = QAudioOutput() # Объект для вывода звука
        self.player.setAudioOutput(self.audio_output)  # Привязываем аудиовыход к проигрывателю

        # Переменная для хранения текущего аудиофайла
        self.current_url = None

        # Инициализируем интерфейс и соединяем сигналы
        self.init_ui()
        self.init_signals()

        # Создаем таймер для обновления позиции воспроизведения
        self.timer = QTimer()
        self.timer.setInterval(500)  # Интервал обновления 500 мс
        self.timer.timeout.connect(self.update_position)  # При срабатывании таймера вызываем метод update_position

    def init_ui(self):
        """
        Метод инициализации пользовательского интерфейса
        Здесь создаются и настраиваются все виджеты (кнопки, слайдеры и т.д.)
        """
        # Кнопка выбора файла
        self.btn_open = QPushButton("Выбрать файл")  # Создаем кнопку с надписью
        # Настраиваем стиль кнопки с помощью CSS
        self.btn_open.setStyleSheet("""
            color: #F43232;
            border: 1px solid #F43232;
            background-color: transparent;
            border-radius: 4px;
            padding: 8px 16px;
        """)

        # Кнопки управления воспроизведением
        self.btn_play = QPushButton()   # Кнопка воспроизведения (без текста, только иконка)
        self.btn_pause = QPushButton()  # Кнопка паузы (без текста, только иконка)
        self.btn_stop = QPushButton()   # Кнопка остановки (без текста, только иконка)
        icon_size = 64  # Размер иконок 64x64 пикселей

        # Загружаем иконки с проверкой их существования
        play_icon_path = ICON_DIR / "play.png"
        pause_icon_path = ICON_DIR / "pause.png"
        stop_icon_path = ICON_DIR / "stop.png"

        # Если иконки существуют, устанавливаем их на соответствующие кнопки
        if play_icon_path.exists():
            self.btn_play.setIcon(QIcon(str(play_icon_path)))
        if pause_icon_path.exists():
            self.btn_pause.setIcon(QIcon(str(pause_icon_path)))
        if stop_icon_path.exists():
            self.btn_stop.setIcon(QIcon(str(stop_icon_path)))

        # Настройка стиля и поведения всех кнопок управления
        for btn in (self.btn_play, self.btn_pause, self.btn_stop):
            btn.setFlat(True)  # Убираем рамку кнопки
            btn.setIconSize(QSize(icon_size, icon_size))  # Устанавливаем размер иконки
            btn.setCursor(Qt.CursorShape.PointingHandCursor)  # Меняем курсор на указатель при наведении
            # Настраиваем стиль кнопки с эффектом при наведении
            btn.setStyleSheet("""
                QPushButton {
                    border: none;
                    background-color: transparent;
                }
                QPushButton:hover {
                    background-color: rgba(244, 50, 50, 0.1);
                    border-radius: 4px;
                }
            """)

        # Создаем горизонтальный слой для размещения кнопок управления
        # addStretch() добавляет растягивающийся элемент, чтобы центрировать кнопки
        controls_layout = QHBoxLayout()
        controls_layout.addStretch()
        controls_layout.addWidget(self.btn_open)
        controls_layout.addWidget(self.btn_play)
        controls_layout.addWidget(self.btn_pause)
        controls_layout.addWidget(self.btn_stop)
        controls_layout.addStretch()

        # Слайдер позиции трека - позволяет перемещаться по времени воспроизведения
        self.position_slider = QSlider(Qt.Orientation.Horizontal)  # Горизонтальный ползунок
        self.position_slider.setRange(0, 1000)  # Устанавливаем диапазон от 0 до 1000
        # Настраиваем внешний вид слайдера
        self.position_slider.setStyleSheet("""
            QSlider::groove:horizontal { height: 6px; background: #ccc; }
            QSlider::handle:horizontal { background: #F43232; width: 14px; margin: -4px 0; border-radius: 7px; }
            QSlider::sub-page:horizontal { background: #F43232; }
        """)

        # Метка с названием трека - показывает имя текущего файла
        self.label_track = QLabel("Файл не выбран")
        self.label_track.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Центрируем текст

        # Метка времени - показывает текущую позицию и общую длительность
        self.label_time = QLabel("00:00 / 00:00")
        self.label_time.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Слайдер громкости - вертикальный ползунок для регулировки громкости
        self.volume_slider = QSlider(Qt.Orientation.Vertical)
        self.volume_slider.setRange(0, 100)  # Диапазон от 0% до 100%
        self.volume_slider.setValue(50)      # Устанавливаем начальное значение 50%
        self.volume_slider.setInvertedAppearance(True)  # Инвертируем направление (снизу вверх)
        # Настраиваем стиль вертикального слайдера
        self.volume_slider.setStyleSheet("""
            QSlider::groove:vertical {
                width: 6px;
                background: #ccc;
                border-radius: 3px;
            }
            QSlider::handle:vertical {
                background: #F43232;
                height: 14px;
                margin: 0 -4px;
                border-radius: 7px;
            }
            QSlider::add-page:vertical {
                background: #F43232;
                border-radius: 3px;
            }
            QSlider::sub-page:vertical {
                background: #ccc;
                border-radius: 3px;
            }
        """)
        # Устанавливаем политику размера - фиксированная ширина, расширяющаяся высота
        self.volume_slider.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)

        # Создаем вертикальный слой для основных элементов плеера
        player_layout = QVBoxLayout()
        player_layout.addLayout(controls_layout)  # Добавляем слой с кнопками
        player_layout.addWidget(self.position_slider)  # Слайдер позиции
        player_layout.addWidget(self.label_track)      # Название трека
        player_layout.addWidget(self.label_time)       # Время
        player_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Центрируем содержимое

        # Обертка для центрирования всей панели по вертикали
        center_layout = QVBoxLayout()
        center_layout.addStretch()  # Растягиваемый элемент сверху
        center_layout.addLayout(player_layout)  # Основное содержимое
        center_layout.addStretch()  # Растягиваемый элемент снизу

        # Основной слой: слева плеер в центре, справа слайдер громкости
        main_layout = QHBoxLayout()
        main_layout.addLayout(center_layout)  # Левая часть - основной плеер
        main_layout.addWidget(self.volume_slider)  # Правая часть - слайдер громкости
        main_layout.setContentsMargins(10, 10, 10, 10)  # Отступы по краям окна

        self.setLayout(main_layout)  # Устанавливаем основной слой для окна

    def init_signals(self):
        """
        Метод для подключения сигналов (событий) к слотам (обработчикам)
        Сигналы возникают при действиях пользователя (нажатие кнопки и т.д.)
        """
        # Подключаем нажатие кнопок к соответствующим методам
        self.btn_open.clicked.connect(self.open_file_from_audio_dir)  # Выбор файла
        self.btn_play.clicked.connect(self.play)   # Воспроизведение
        self.btn_pause.clicked.connect(self.pause) # Пауза
        self.btn_stop.clicked.connect(self.stop)   # Остановка

        # Подключаем изменение значения слайдеров к соответствующим методам
        self.volume_slider.valueChanged.connect(self.change_volume)  # Изменение громкости
        self.position_slider.sliderMoved.connect(self.seek)          # Перемещение по треку

        # Подключаем сигналы от медиаплеера
        self.player.durationChanged.connect(self.update_duration)  # Изменение длительности трека
        self.player.positionChanged.connect(self.update_position)  # Изменение текущей позиции

    def open_file_from_audio_dir(self):
        """
        Метод для открытия аудиофайла из директории audio
        Открывает диалоговое окно для выбора файла
        """
        # Открываем диалоговое окно для выбора аудиофайла
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Выберите аудиофайл из media/audio",
            str(AUDIO_DIR),
            "Audio Files (*.mp3 *.wav)"
        )

        # Если пользователь не выбрал файл, выходим
        if not file_path:
            return

        file_path = Path(file_path)
        if os.path.commonpath([str(file_path.parent), str(AUDIO_DIR)]) != str(AUDIO_DIR):
            self.label_track.setText("Файл должен быть из media/audio")
            return

        self.current_url = QUrl.fromLocalFile(str(file_path))
        self.player.setSource(self.current_url)
        self.label_track.setText(file_path.name)

    def play(self):
        if self.current_url is None:
            return
        self.player.play()
        self.timer.start()

    def pause(self):
        self.player.pause()

    def stop(self):
        self.player.stop()
        self.timer.stop()

    def change_volume(self, value):
        self.audio_output.setVolume(value / 100.0)

    def seek(self, value):
        duration = self.player.duration()
        if duration > 0:
            self.player.setPosition(int(duration * (value / 1000)))

    def update_duration(self, duration):
        self.update_position()

    def update_position(self):
        duration = self.player.duration()
        position = self.player.position()
        if duration > 0:
            self.position_slider.blockSignals(True)
            self.position_slider.setValue(int(position / duration * 1000))
            self.position_slider.blockSignals(False)

        self.label_time.setText(f"{self.ms_to_time(position)} / {self.ms_to_time(duration)}")

    # Перевод милисекунд в секунды
    @staticmethod
    def ms_to_time(ms):
        sec = int(ms / 1000)
        m = sec // 60
        s = sec % 60
        return f"{m:02}:{s:02}"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PlayerUI()
    window.show()

    sys.exit(app.exec())
