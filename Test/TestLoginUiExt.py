from PyQt6.QtWidgets import QApplication, QMainWindow
from ui.login.LoginUiExt import LoginUiExt

app = QApplication([])
mainwindow = QMainWindow()
myui = LoginUiExt()
myui.setupUi(mainwindow)
myui.showWindow()
app.exec()