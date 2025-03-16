# TestUserUiExt.py
from PyQt6.QtWidgets import QMainWindow, QApplication

from ui.user.UserUiExt import UserUiExt

app = QApplication([])
mainwindow = QMainWindow()
myui = UserUiExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()
