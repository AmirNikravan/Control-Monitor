from PySide6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PySide6.QtGui import QFont, QColor
from PySide6.QtCore import Qt

class BeautifulLabelApp(QWidget):
    def __init__(self):
        super().__init__()
        
        # Set up the window layout
        layout = QVBoxLayout()
        
        # Create and style the QLabel
        label = QLabel("Hello, Beautiful QLabel!")
        label.setAlignment(Qt.AlignCenter)
        
        # Set font properties
        font = QFont("Arial", 16, QFont.Bold)
        label.setFont(font)
        
        # Style the QLabel with a gradient background, rounded corners, and shadow
        label.setStyleSheet("""
            QLabel {
                background: qlineargradient(
                    spread: pad, x1: 0, y1: 0, x2: 1, y2: 1, 
                    stop: 0 rgba(0, 153, 255, 255), stop: 1 rgba(102, 255, 102, 255)
                );
                color: white;
                padding: 20px;
                border-radius: 15px;
                border: 2px solid rgba(255, 255, 255, 100);
                box-shadow: 5px 5px 15px rgba(0, 0, 0, 75);
            }
        """)

        layout.addWidget(label)
        self.setLayout(layout)
        self.setWindowTitle("Beautiful QLabel")
        self.resize(400, 200)

# Run the application
app = QApplication([])
window = BeautifulLabelApp()
window.show()
app.exec()
