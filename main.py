import sys, random
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QFrame
from PyQt6.QtGui import QPainter, QBrush, QColor
from PyQt6.QtCore import Qt

class Canvas(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.circles = []
        self.setAttribute(Qt.WidgetAttribute.WA_OpaquePaintEvent)

    def add_circle(self):
        diameter = random.randint(20, 100)
        w = self.width()
        h = self.height()
        if w < diameter or h < diameter:
            x = 0
            y = 0
        else:
            x = random.randint(0, w - diameter)
            y = random.randint(0, h - diameter)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.circles.append((x, y, diameter, color))
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(Qt.PenStyle.NoPen)
        for (x, y, diameter, color) in self.circles:
            painter.setBrush(QBrush(color))
            painter.drawEllipse(x, y, diameter, diameter)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Случайные окружности")
        central = QWidget(self)
        layout = QVBoxLayout(central)
        self.pushButton = QPushButton("Нарисовать окружность", self)
        self.canvas = Canvas(self)
        self.canvas.setMinimumSize(300, 300)
        layout.addWidget(self.pushButton)
        layout.addWidget(self.canvas)
        self.setCentralWidget(central)
        self.pushButton.clicked.connect(self.canvas.add_circle)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
