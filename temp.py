from PySide6.QtCore import QTimer

if val["l1"]:
    self.ui.lamp_stop.setStyleSheet("")  # Reset StyleSheet
    QTimer.singleShot(50, lambda: self.ui.lamp_stop.setStyleSheet("""
        QLabel {
            background-color: green;
            border-style: outset;
            border-width: 1px;
            border-radius: 30px;
        }
    """))
else:
    self.ui.lamp_stop.setStyleSheet("")  # Reset StyleSheet
    QTimer.singleShot(50, lambda: self.ui.lamp_stop.setStyleSheet("""
        QLabel {
            background-color: red;
            border-style: outset;
            border-width: 1px;
            border-radius: 30px;
        }
    """))
