import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui.untitled import Ui_MainWindow
class Example(QMainWindow):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.show()

if __name__ == '__main__':
    e = Example()
    sys.exit(e.app.exec())








