from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget, QVBoxLayout, QLabel
from PySide6.QtCore import QTimer
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # ایجاد دو صفحه نمونه
        self.page1 = QWidget()
        self.page1_layout = QVBoxLayout()
        self.page1_layout.addWidget(QLabel("Page 1"))
        self.page1.setLayout(self.page1_layout)

        self.page2 = QWidget()
        self.page2_layout = QVBoxLayout()
        self.page2_layout.addWidget(QLabel("Page 2"))
        self.page2.setLayout(self.page2_layout)

        self.stacked_widget.addWidget(self.page1)
        self.stacked_widget.addWidget(self.page2)

        # تایمر برای تغییر صفحه
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.change_page)
        self.timer.start(1000)  # تغییر هر ۱ ثانیه

        self.current_page = 0

    def change_page(self):
        self.current_page = (self.current_page + 1) % self.stacked_widget.count()
        self.stacked_widget.setCurrentIndex(self.current_page)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
