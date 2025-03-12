from Custom_Widgets import QMainWindow

from ui.login.login import Ui_MainWindow
from utils.style_login_loader import loadStyleJson


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 🟢 Gọi hàm load JSON style từ thư mục utils
        loadStyleJson(self)



        self.show()