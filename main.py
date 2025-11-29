import sys
import random

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor, QPen, QBrush

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)

        self.circles = []

        self.draw_button.clicked.connect(self.add_circle)

    def add_circle(self):
        radius = random.randint(10, 80)
        x = random.randint(radius, self.width() - radius)
        y = random.randint(radius, self.height() - radius)

        self.circles.append(Circle(x, y, radius))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)

        painter.setBrush(QBrush(QColor(255, 255, 0)))
        painter.setPen(QPen(QColor(0, 0, 0), 1))

        for circle in self.circles:
            painter.drawEllipse(
                circle.x - circle.radius,
                circle.y - circle.radius,
                circle.radius * 2,
                circle.radius * 2
            )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
