from PyQt6 import QtGui
from PyQt6.QtWidgets import QDialog

from ui.user.UserInfor import Ui_Dialog
from utils import resources_banner_rc
from utils import resources_poster_rc
from utils import resources_rc


class UserInforExt(QDialog):
    def __init__(self, movie, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)


