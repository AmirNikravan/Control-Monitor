import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel
from PySide6.QtCore import QTimer
from PySide6.QtGui import QColor

class ColorChangeApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the label and button
        self.label = QLabel("Click the button to change its color", self)
        self.button = QPushButton("Click Me", self)
        self.button.setStyleSheet("background-color: red")

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

        # Connect button click to the function
        self.button.clicked.connect(self.change_color)

    def change_color(self):
        # Change the button color to green
        self.button.setStyleSheet("background-color: green")

        # Set a timer to change the color back to red after 3 seconds
        QTimer.singleShot(3000, self.reset_color)

    def reset_color(self):
        # Change the button color back to red
        self.button.setStyleSheet("background-color: red")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = ColorChangeApp()
    window.setWindowTitle("Color Change Example")
    window.resize(300, 150)
    window.show()

    sys.exit(app.exec())
