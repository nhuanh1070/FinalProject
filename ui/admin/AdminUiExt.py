from ui.admin.Admin import Ui_MainWindow
from Custom_Widgets import QMainWindow
from utils.style_loader import loadStyleJson
from PyQt6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 🟢 Gọi hàm load JSON style từ thư mục utils
        loadStyleJson(self)

        # 🟢 Kết nối sự kiện bấm nút
        self.ui.Menu_btn.clicked.connect(self.toggleLeftMenu)
        self.ui.Account_btn.clicked.connect(self.toggleProfileCont)
        self.ui.mainBody.mousePressEvent = self.onMainBodyClicked

        self.show()

    def toggleLeftMenu(self):
        """Mở rộng hoặc thu nhỏ menu trái và điều chỉnh kích thước mainBody"""
        if self.ui.leftMenu.isVisible():
            self.ui.leftMenu.setVisible(False)
            self.ui.mainBody.setMinimumSize(QSize(self.width(), self.ui.mainBody.height()))
        else:
            self.ui.leftMenu.setVisible(True)
            self.ui.mainBody.setMinimumSize(QSize(self.width() - 250, self.ui.mainBody.height()))  # 250 là chiều rộng của leftMenu

    def toggleProfileCont(self):
        """Hiển thị hoặc ẩn profileCont khi click Account_btn"""
        if self.ui.profileCont.isVisible():
            self.ui.profileCont.setVisible(False)
        else:
            self.ui.profileCont.setVisible(True)

    def onMainBodyClicked(self, event):
        """Ẩn profileCont và leftMenu khi click vào mainBody"""
        if self.ui.profileCont.isVisible():
            self.ui.profileCont.setVisible(False)

        if self.ui.leftMenu.isVisible():
            self.ui.leftMenu.setVisible(False)
            self.ui.mainBody.setMinimumSize(QSize(self.width(), self.ui.mainBody.height()))
