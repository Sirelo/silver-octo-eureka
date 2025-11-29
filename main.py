import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor, QPen, QBrush

from ui_file import Ui_MainWindow


class Circle:
    def __init__(self, x, y, radius, color: QColor):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.circles = []

        self.ui.draw_button.clicked.connect(self.add_circle)

    def add_circle(self):
        radius = random.randint(20, 80)

        w = self.ui.centralwidget.width()
        h = self.ui.centralwidget.height()

        x = random.randint(radius, w - radius)
        y = random.randint(radius, h - radius - 100)

        color = QColor(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

        self.circles.append(Circle(x, y, radius, color))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)

        for circle in self.circles:
            painter.setBrush(QBrush(circle.color))
            painter.setPen(QPen(QColor(0, 0, 0), 2))

            painter.drawEllipse(
                circle.x - circle.radius,
                circle.y - circle.radius,
                circle.radius * 2,
                circle.radius * 2
            )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
