from PyQt6.QtWidgets import QApplication
from ui.admin.AdminUiExt import AdminUiExt

app = QApplication([])
ui = AdminUiExt()
ui.showWindow()
app.exec()
