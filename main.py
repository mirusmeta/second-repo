#!/usr/bin/env python3
import sys, random
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QFrame
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
        self.circles.append((x, y, diameter))
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        brush = QBrush(QColor(255, 255, 0))
        painter.setBrush(brush)
        painter.setPen(Qt.PenStyle.NoPen)
        for (x, y, diameter) in self.circles:
            painter.drawEllipse(x, y, diameter, diameter)

def main():
    app = QApplication(sys.argv)
    window = uic.loadUi("UI.ui")
    old_canvas = window.findChild(QFrame, "canvas")
    if old_canvas is not None:
        new_canvas = Canvas(old_canvas.parent())
        new_canvas.setGeometry(old_canvas.geometry())
        parent_layout = old_canvas.parent().layout()
        if parent_layout is not None:
            index = parent_layout.indexOf(old_canvas)
            parent_layout.removeWidget(old_canvas)
            old_canvas.deleteLater()
            parent_layout.insertWidget(index, new_canvas)
        window.canvas = new_canvas
    else:
        sys.exit(1)
    window.pushButton.clicked.connect(window.canvas.add_circle)
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
