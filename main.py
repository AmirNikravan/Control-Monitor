from UI_main import Ui_MainWindow
from PySide6.QtWidgets import *
import sys
class App(QMainWindow):
    def __init__(self,parent = None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
if __name__=='__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
        
        
