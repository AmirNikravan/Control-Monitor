from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem

app = QApplication([])

# ایجاد جدول
table = QTableWidget(10, 3)

# پر کردن جدول با داده‌ها
for row in range(10):
    for col in range(3):
        item = QTableWidgetItem(f"Item {row}, {col}")
        table.setItem(row, col, item)

# تنظیم Style Sheet برای سطرهای یکی در میان
table.setStyleSheet("""
    QTableWidget::item {
        background-color: #FFFFFF;
    }
    QTableWidget::item:alternate {
        background-color: #F0F0F0;
    }
""")

table.setAlternatingRowColors(True)  # فعال کردن رنگ‌بندی یکی در میان
table.show()
app.exec()
