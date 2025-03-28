import json
import os
import sys

from PyQt6.QtWidgets import QDialog, QMessageBox, QMainWindow, QApplication
from CSDL.libs.DataConnector import DataConnector
from ui.user.UserInforUi import Ui_Dialog

from utils import resources_banner_rc
from utils import resources_poster_rc
from utils import resources_rc

class UserInforExt(QDialog, Ui_Dialog):  # Kế thừa từ Ui_Dialog
    def __init__(self, user_info=None, from_user_ui=False, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.dc = DataConnector()
        self.user_info = user_info or {}
        self.from_user_ui = from_user_ui  # Biến này xác định nếu mở từ UserUiExt

        self.fill_user_data()
        self.setupSignalAndSlot()
    def setupSignalAndSlot(self):

        self.pushButtonConfirm.clicked.connect(self.save_user_info)
        self.pushButtonLogOut.clicked.connect(self.LogOutProcess)


    def LogOutProcess(self):
        """ Xử lý đăng xuất, đóng UserInforExt & UserUiExt, mở lại Login """
        from ui.login.LoginUiExt import LoginUiExt

        # Hiển thị hộp thoại xác nhận
        msgbox = QMessageBox(self)
        msgbox.setText("Bạn có chắc chắn muốn đăng xuất?")
        msgbox.setWindowTitle("Xác nhận đăng xuất")
        msgbox.setIcon(QMessageBox.Icon.Question)
        msgbox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        result = msgbox.exec()

        if result == QMessageBox.StandardButton.Yes:
            # Xóa thông tin đăng nhập
            dataset_path = os.path.join(os.path.dirname(__file__), "../dataset")
            current_user_path = os.path.join(dataset_path, "current_user.json")

            if os.path.exists(current_user_path):
                os.remove(current_user_path)  # Xóa file đăng nhập

            # Đóng cửa sổ UserInforExt
            self.close()

            # Đóng luôn UserUiExt nếu nó tồn tại (vì đã được truyền vào làm parent)
            if self.parent():
                self.parent().close()

            # Mở lại giao diện đăng nhập
            self.mainwindow = QMainWindow()
            self.login_ui = LoginUiExt()
            self.login_ui.setupUi(self.mainwindow)
            self.mainwindow.show()



    def load_user_data(self):
        filename = "users_data.json"  # Cập nhật đường dẫn nếu cần
        try:
            with open(filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def fill_user_data(self):
        self.lineEditUserName.setReadOnly(True)
        self.lineEditUserName.setText(str(self.user_info.get("Username", "")))
        self.lineEditFullName.setText(str(self.user_info.get("fullname", "")))
        self.lineEditBirthDay.setText(str(self.user_info.get("birthday", "")))
        self.lineEditPhoneNumber.setText(str(self.user_info.get("phone", "")))
        self.lineEditEmail.setText(str(self.user_info.get("email", "")))

    def save_user_info(self):
        Username = self.lineEditUserName.text().strip()
        Fullname = self.lineEditFullName.text().strip()
        Birthday = self.lineEditBirthDay.text().strip()
        Phone = self.lineEditPhoneNumber.text().strip()
        Email = self.lineEditEmail.text().strip()


        # Nếu có bất kỳ trường nào bị bỏ trống, yêu cầu người dùng nhập đủ
        if not Fullname or not Birthday or not Phone or not Email:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin trước khi xác nhận.")
            return  # Không đóng cửa sổ, yêu cầu user nhập đủ thông tin

        # Nếu mở từ UserUiExt, chỉ đóng UserInforExt, không mở lại UserUiExt
        if self.from_user_ui:
            self.close()
            return

        # Nếu đây là lần đầu nhập thông tin, cập nhật JSON và mở lại UserUiExt
        success = self.dc.update_user_info(Username, Fullname, Birthday, Phone, Email)

        if success:
            QMessageBox.information(self, "Thành công", "Enjoy your movies <3")
            self.close()
            self.open_user_ui()
        else:
            QMessageBox.critical(self, "Lỗi hệ thống", "Không thể cập nhật thông tin.")
    def open_user_ui(self):
        """ Mở giao diện UserUiExt sau khi hoàn tất thông tin """
        from ui.user.UserUiExt import UserUiExt  # Import tại đây để tránh vòng lặp
        self.mainwindow = QMainWindow()
        self.user_ui = UserUiExt()
        self.user_ui.setupUi(self.mainwindow)
        self.user_ui.showWindow()



