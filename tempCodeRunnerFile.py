import sys
from PySide6.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QHBoxLayout
from PySide6.QtCore import Qt, QPropertyAnimation
from PySide6.QtGui import QTextCursor

class NotificationPopup(QWidget):
    def __init__(self, message, remove_callback, parent=None):
        super().__init__(parent)

        # تنظیم استایل کلی پاپ‌آپ
        self.setStyleSheet("""
            QWidget {
                background-color: #4CAF50;
                border-radius: 5px;
                border: 1px solid #388E3C;
                padding: 5px;
                margin-bottom: 5px;  /* فاصله بین نوتیفیکیشن‌ها */
            }
        """)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)

        # چیدمان افقی برای نوتیفیکیشن
        layout = QHBoxLayout(self)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        # ساخت لیبل برای نمایش پیام
        self.message_label = QLabel(f"✖ {message}  ")
        self.message_label.setStyleSheet("""
            QLabel {
                color: white;
                font-size: 12pt;
                padding: 5px;
            }
        """)
        
        # افزودن قابلیت کلیک به متن "حذف"
        self.message_label.setTextInteractionFlags(Qt.TextBrowserInteraction)
        self.message_label.setOpenExternalLinks(False)

        # اتصال کلیک به حذف نوتیفیکیشن
        self.message_label.mousePressEvent = lambda event: self.handle_click(event, remove_callback)

        # اضافه کردن لیبل به چیدمان
        layout.addWidget(self.message_label)

        # نمایش در اندازه مناسب
        self.adjustSize()

        # انیمیشن برای ظاهر شدن نوتیفیکیشن
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(500)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

    def handle_click(self, event, remove_callback):
        # بررسی این که آیا بر روی متن "حذف" کلیک شده است
        if self.message_label.text().startswith("✖"):
            remove_callback()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # تنظیمات اولیه پنجره
        self.setWindowTitle("برنامه نوتیفیکیشن")
        self.setGeometry(300, 300, 400, 300)

        # چیدمان اصلی
        self.layout = QVBoxLayout(self)

        # دکمه‌ها برای تست نوتیفیکیشن
        self.button1 = QPushButton("نوتیفیکیشن 1", self)
        self.button2 = QPushButton("نوتیفیکیشن 2", self)
        self.button3 = QPushButton("نوتیفیکیشن 3", self)

        # تنظیم استایل برای دکمه‌ها
        for button in [self.button1, self.button2, self.button3]:
            button.setStyleSheet("""
                QPushButton {
                    background-color: #1976D2;
                    color: white;
                    padding: 10px;
                    font-size: 12pt;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #1565C0;
                }
            """)

        # اتصال دکمه‌ها به متد مربوطه
        self.button1.clicked.connect(lambda: self.show_notification("ورود با موفقیت انجام شد!"))
        self.button2.clicked.connect(lambda: self.show_notification("عملیات موفقیت‌آمیز بود!"))
        self.button3.clicked.connect(lambda: self.show_notification("پیام جدید دریافت شد!"))

        # اضافه کردن دکمه‌ها به چیدمان اصلی
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.layout.addWidget(self.button3)

    def show_notification(self, message):
        # ایجاد پاپ‌آپ نوتیفیکیشن
        popup = NotificationPopup(message, lambda: self.remove_notification(popup), self)

        # تعیین موقعیت نوتیفیکیشن در گوشه سمت چپ بالا
        popup.move(10, 10 + len(self.layout.children()) * (popup.height() + 5))
        popup.show()

    def remove_notification(self, notification):
        # حذف نوتیفیکیشن از والد
        notification.deleteLater()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
