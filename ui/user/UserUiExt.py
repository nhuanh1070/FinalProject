from PyQt6.QtWidgets import QMainWindow
from ui.user.UserUi import Ui_MainWindow
from utils import resources_banner_rc
from utils import resources_poster_rc
from utils import resources_rc
class UserUiExt(Ui_MainWindow):
    def __init__(self):
        self.MainWindow = QMainWindow()
        self.setupUi(self.MainWindow)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.MainWindow.ui = self
        # Gán sự kiện click cho các nút chuyển trang
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        # Sự kiện nút bấm chuyển trang
        self.pushButton_Right.clicked.connect(self.nextPage)
        self.pushButton_Left.clicked.connect(self.prevPage)

    def nextPage(self):
        current_index = self.stackedWidget.currentIndex()
        next_index = (current_index + 1) % self.stackedWidget.count()
        self.stackedWidget.setCurrentIndex(next_index)

    def prevPage(self):
        current_index = self.stackedWidget.currentIndex()
        prev_index = (current_index - 1) % self.stackedWidget.count()
        self.stackedWidget.setCurrentIndex(prev_index)