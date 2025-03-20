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
        # Khi nhấn nút "Xác nhận", lưu thông tin vào users_data.json
        self.pushButtonConfirm.clicked.connect(self.save_user_info)

        self.pushButtonLogOut.clicked.connect(self.LogOutProcess)
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
                print("✅ Đã đăng xuất và xóa thông tin người dùng!")

            # Đóng cửa sổ UserInforExt
            self.close()

            # Đóng luôn UserUiExt nếu nó tồn tại (vì đã được truyền vào làm parent)
            if self.parent():
                print("📌 Đóng luôn UserUiExt!")
                self.parent().close()

            # Mở lại giao diện đăng nhập
            self.mainwindow = QMainWindow()
            self.login_ui = LoginUiExt()
            self.login_ui.setupUi(self.mainwindow)
            self.mainwindow.show()



    def load_user_data(self):
        """ Đọc dữ liệu từ file UserS.json """
        filename = "UserS.json"  # Cập nhật đường dẫn nếu cần
        try:
            with open(filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def fill_user_data(self):
        # Đảm bảo không có giá trị None trước khi gán vào UI
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

        print(f"📌 Debug - Kiểm tra thông tin user {Username}")
        print(f"📌 Fullname: {Fullname}, Birthday: {Birthday}, Phone: {Phone}, Email: {Email}")

        # Nếu có bất kỳ trường nào bị bỏ trống, yêu cầu người dùng nhập đủ
        if not Fullname or not Birthday or not Phone or not Email:
            print("❌ LỖI: Một trong các trường bị bỏ trống!")
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin trước khi xác nhận.")
            return  # Không đóng cửa sổ, yêu cầu user nhập đủ thông tin

        # Nếu mở từ UserUiExt, chỉ đóng UserInforExt, không mở lại UserUiExt
        if self.from_user_ui:
            print(f"✅ User {Username} đang xem lại thông tin, chỉ đóng UserInforExt.")
            self.close()
            return

        # Nếu đây là lần đầu nhập thông tin, cập nhật JSON và mở lại UserUiExt
        print(f"📌 Debug - Cập nhật thông tin cho user: {Username}")
        success = self.dc.update_user_info(Username, Fullname, Birthday, Phone, Email)

        if success:
            print(f"✅ Cập nhật thành công user {Username}!")
            QMessageBox.information(self, "Thành công", "Thông tin đã được cập nhật.")
            self.close()
            self.open_user_ui()
        else:
            print(f"❌ LỖI: Không tìm thấy user {Username} trong JSON!")
            QMessageBox.critical(self, "Lỗi hệ thống", "Không thể cập nhật thông tin.")
    def open_user_ui(self):
        """ Mở giao diện UserUiExt sau khi hoàn tất thông tin """
        from ui.user.UserUiExt import UserUiExt  # Import tại đây để tránh vòng lặp
        print("📌 Debug - Đang mở giao diện User UI...")
        self.mainwindow = QMainWindow()
        self.user_ui = UserUiExt()
        self.user_ui.setupUi(self.mainwindow)
        self.user_ui.showWindow()



