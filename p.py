import random
import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QPushButton, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle('MainWindow')

        # Создаем центральный виджет и устанавливаем его
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Создаем вертикальный layout
        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        # Создаем кнопку
        self.pushButton = QPushButton('Draw', self)
        self.pushButton.clicked.connect(self.paint)
        self.layout.addWidget(self.pushButton)

        # Флаг для рисования
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_flag(self, qp):
        a = random.randint(10, 100)  # Размер круга
        r = random.randint(0, 255)  # Красный цвет
        g = random.randint(0, 255)  # Зеленый цвет
        b = random.randint(0, 255)  # Синий цвет
        qp.setBrush(QColor(r, g, b))

        # Рисуем круг в случайной позиции
        qp.drawEllipse(random.randint(0, self.width()), random.randint(0, self.height()), a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
