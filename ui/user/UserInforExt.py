from PyQt6.QtWidgets import QDialog, QMessageBox, QMainWindow

from ui.user.UserInfor import Ui_Dialog

from utils import resources_banner_rc
from utils import resources_poster_rc
from utils import resources_rc

class UserInforExt(QDialog):
    def __init__(self,username=None, user_ui_ext=None, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        #self.username=username

        self.user_ui_ext = user_ui_ext  # Lưu tham chiếu UserUiExt

        self.ui.pushButtonLogOut.clicked.connect(self.LogOutProcess)
        self.ui.pushButtonConfirm.clicked.connect(self.ConfirmProcess)

    print("UserInforExt setup xong!")  # Debug kiểm tra

    #ABC=LoginUiExt
    '''def load_user_data(filename):
        """ Đọc danh sách user từ file JSON và trả về danh sách đối tượng UserInfor """
        import json
        try:
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)  # Đọc dữ liệu (danh sách [])
                # Kiểm tra nếu dữ liệu không phải danh sách
                if not isinstance(data, list):
                    return []
                user_list = [
                    UserInfor(user["Username"], user["fullname"], user["birthday"], user["phone"], user["email"])
                    for user in data]
                return user_list
        except (FileNotFoundError, json.JSONDecodeError):
            return []  # Trả về danh sách trống nếu có lỗi

    def fill_user_data(self):
        """ Lấy thông tin user từ file JSON và điền vào các lineEdit """
        filename = "../dataset/UserS.json"

        user_list = self.load_user_data(filename)  # Lấy danh sách user

        # Tìm user theo username
        user_info = None
        for user in user_list:
            if user.Username == self.username:  # So sánh username
                user_info = user
                break  # Dừng vòng lặp khi tìm thấy

        # Nếu tìm thấy user thì gán giá trị vào các QLineEdit
        if user_info:
            self.ui.lineEdit.setText(str("nhuanh"))  # Username (String)
            self.ui.lineEdit_2.setText(str("Phạm Lê Như Anh"))  # Họ và tên (String)
            self.ui.lineEdit_6.setText(str("20-5-2025"))  # Ngày sinh (String)
            self.ui.lineEdit_5.setText(str("0901030490"))  # Số điện thoại (String)
            self.ui.lineEdit_4.setText(str("NhuAnh@gmail.com"))  # Email (String)
        else:
            QMessageBox.warning(self, "Lỗi", "Không tìm thấy thông tin người dùng!")'''

    def LogOutProcess(self):
        from ui.login.LoginUiExt import LoginUiExt
        # Hiển thị hộp thoại xác nhận
        msgbox = QMessageBox(self)
        msgbox.setText("Thoát he em")
        msgbox.setWindowTitle("Xác nhận thoát")
        msgbox.setIcon(QMessageBox.Icon.Warning)
        msgbox.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        result = msgbox.exec()
        if result == QMessageBox.StandardButton.Yes:
            self.close()  # Đóng UserInforExt
            # Đóng luôn UserUiExt nếu có
            if self.user_ui_ext:
                self.user_ui_ext.MainWindow.close()
            # Mở màn hình đăng nhập
            self.mainwindow = QMainWindow()
            self.myui = LoginUiExt()
            self.myui.setupUi(self.mainwindow)
            self.mainwindow.show()

    def ConfirmProcess(self):
        from ui.user.UserUiExt import UserUiExt
        if self.ui.checkBox.isChecked():
            self.close()
            msgbox = QMessageBox(self)
            msgbox.setText("Xác nhận đã đăng nhập thành công")
            msgbox.setWindowTitle("Xác nhận đăng nhập")
            msgbox.setIcon(QMessageBox.Icon.Information)
            msgbox.setStandardButtons(QMessageBox.StandardButton.Yes)
            msgbox.exec()

            if self.user_ui_ext:
                self.user_ui_ext.MainWindow.close()

            # Mở màn hình đăng nhập
            self.mainwindow = QMainWindow()
            self.myui = UserUiExt()
            self.myui.setupUi(self.mainwindow)
            self.mainwindow.show()
        else:
            msgbox = QMessageBox(self)
            msgbox.setText("Vui lòng đánh dấu xác nhận với những điều khoản pháp lý")
            msgbox.setWindowTitle("Xác nhận điều khoản")
            msgbox.setIcon(QMessageBox.Icon.Information)
            msgbox.setStandardButtons(QMessageBox.StandardButton.Yes)

            msgbox.exec()
