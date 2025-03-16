from PyQt6.QtWidgets import QMainWindow
from ui.login.login import Ui_MainWindow
from utils import resources_banner_rc
from utils import resources_poster_rc
from utils import resources_rc
from utils import resources_logo_rc
class LoginUiExt(Ui_MainWindow):
    def __init__(self):
        self.MainWindow = QMainWindow()
        self.setupUi(self.MainWindow)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.MainWindow.ui = self


        # Đặt trang đầu tiên hiển thị
        self.stackedWidget.setCurrentIndex(0)

        # Gán sự kiện click cho các nút chuyển trang
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        """ Gán sự kiện cho các nút để chuyển trang """
        self.pushButtonTo_Register.clicked.connect(self.showRegisterPage)
        self.pushButtonTo_Login.clicked.connect(self.showLoginPage)

    def showRegisterPage(self):
        """ Hiển thị trang đăng ký """
        self.stackedWidget.setCurrentWidget(self.RegisterPage)

    def showLoginPage(self):
        """ Hiển thị trang đăng nhập """
        self.stackedWidget.setCurrentWidget(self.LoginPage)