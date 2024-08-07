import sys
from PyQt5 import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtGui import QPainter, QColor, QBrush,Q
from PyQt5.QtCore import QSize,Qt

class CircularLabel(QLabel):
    def __init__(self, text='', parent=None):
        super().__init__(text, parent)
        self.setAlignment(Qt.AlignCenter)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setMinimumSize(QSize(100, 100))  # Set a minimum size for the circular label

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw the circle
        rect = self.rect()
        radius = min(rect.width(), rect.height()) // 2
        center = rect.center()
        painter.setBrush(QBrush(QColor('lightblue')))
        painter.drawEllipse(center, radius, radius)

        # Draw the text
        painter.setPen(QColor('black'))
        painter.drawText(rect, Qt.AlignCenter, self.text())

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Circular QLabel Example")
        self.setGeometry(100, 100, 300, 300)

        self.circular_label = CircularLabel('Hello World!', self)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.addWidget(self.circular_label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
