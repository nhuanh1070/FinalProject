import json
import os

from PyQt6.QtWidgets import QMainWindow, QMessageBox

from CSDL.models.UserInfor import UserInfor

from CSDL.libs.DataConnector import DataConnector
from CSDL.libs.JsonFileFactory import JsonFileFactory
from CSDL.models.Admin import Admin
from CSDL.models.User import User
from ui.login.login import Ui_MainWindow
from ui.user.UserInforExt import UserInforExt
from ui.user.UserUiExt import UserUiExt
from utils import resources_banner_rc
from utils import resources_poster_rc
from utils import resources_rc
from utils import resources_logo_rc


class LoginUiExt(Ui_MainWindow):
   def __init__(self):
       self.MainWindow = QMainWindow()
       self.setupUi(self.MainWindow)
       self.dc=DataConnector()

   def setupUi(self, MainWindow):
       super().setupUi(MainWindow)
       self.MainWindow = MainWindow
       self.MainWindow.ui = self

       self.stackedWidget.setCurrentWidget(self.LoginPage)


       # Gán sự kiện click cho các nút chuyển trang
       self.setupSignalAndSlot()

   def showWindow(self):
       self.MainWindow.show()
   def setupSignalAndSlot(self):
       """ Gán sự kiện cho các nút để chuyển trang """
       self.pushButtonTo_Register.clicked.connect(self.showRegisterPage)
       self.pushButtonTo_Login.clicked.connect(self.showLoginPage)
       self.pushButtonRegister.clicked.connect(self.register_process)
       self.pushButtonLogin.clicked.connect(self.login_process)

   def showRegisterPage(self):
       """ Hiển thị trang đăng ký """
       self.stackedWidget.setCurrentWidget(self.RegisterPage)

   def showLoginPage(self):
       """ Hiển thị trang đăng nhập """
       self.stackedWidget.setCurrentWidget(self.LoginPage)

   def clear_user_infor(self):
       self.lineEditUsername_Signup.setText("")
       self.lineEditPassword_Signup.setText("")
       self.lineEditConfirmPassword_Signup.setText("")
   dc = DataConnector()

   #Xử lý đăng kí
   def register_process(self):
       Username = self.lineEditUsername_Signup.text().strip()
       Password = self.lineEditPassword_Signup.text().strip()
       ConfirmPassword = self.lineEditConfirmPassword_Signup.text().strip()


       if not Username or not Password or not ConfirmPassword:
           QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng nhập đầy đủ thông tin.")
           return

       if Password != ConfirmPassword:
           QMessageBox.warning(self.MainWindow, "Lỗi", "Mật khẩu xác nhận không khớp. Vui lòng thử lại!")
           self.lineEditConfirmPassword_Signup.clear()
           return

       user = User(Username, Password)
       index = self.dc.check_user_exist(user.Username)

       if index == -1:
           try:
               success = self.dc.save_account(user)

               if success:
                   QMessageBox.information(self.MainWindow, "Thành công", "Tạo tài khoản thành công.")
                   self.clear_user_infor()
               else:
                   QMessageBox.warning(self.MainWindow, "Lỗi", "Lưu tài khoản thất bại!")
           except Exception as e:
               QMessageBox.critical(self.MainWindow, "Lỗi hệ thống", f"Lỗi khi lưu tài khoản: {str(e)}")
       else:
           QMessageBox.warning(self.MainWindow, "Lỗi", "Tên người dùng đã tồn tại!")
    #xử lý đăng nhập
   def load_user_data(self, filename):
       """ Đọc danh sách tài khoản từ file JSON """
       jff = JsonFileFactory()
       users_list = jff.read_data(filename, UserInfor)
       if users_list is None:
           return []
       return users_list

   def load_admin_data(self, filename):
       """ Đọc danh sách tài khoản từ file JSON """
       jff = JsonFileFactory()
       admins_list = jff.read_data(filename, Admin)
       if admins_list is None:
           return []
       return admins_list

   def coivalidate_user(self, Username, Password):
       base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
       json_path = os.path.join(base_path, "dataset", "users_data.json")

       if not os.path.exists(json_path):
           return None

       try:
           with open(json_path, "r", encoding="utf-8") as file:
               users = json.load(file)
       except json.JSONDecodeError:
           return None

       for user in users:
           if user.get("Username") == Username and user.get("Password") == Password:
               return user  # Trả về toàn bộ user_info

       return None

   def coivalidate_admin(self, Username, Password):
       admins = self.load_admin_data("../dataset/admin.json")  # Lấy danh sách Admin từ hệ thống
       for a in admins:
           if a.Username == Username and a.Password == Password:
               return 1
       return 0

   def open_admin_ui(self):
       """ Mở giao diện Admin """
       from ui.admin.AdminUiExt import AdminUiExt

       # self.MainWindow.close()  # Đóng cửa sổ đăng nhập
       self.mainwindow = QMainWindow()
       self.myui = AdminUiExt()
       self.myui.setupUi(self.mainwindow)
       self.myui.showWindow()

   def open_user_ui(self, user_info):
       if not user_info:
           QMessageBox.warning(self.MainWindow, "Lỗi", "Không có dữ liệu người dùng để hiển thị.")
           return

       # Kiểm tra dữ liệu trước khi mở UserInforExt

       try:
           self.user_info_dialog = UserInforExt(user_info=user_info)
           self.user_info_dialog.exec()
       except Exception as e:
           QMessageBox.critical(self.MainWindow, "Lỗi hệ thống", f"Không thể mở giao diện người dùng: {e}")

   def login_process(self):
       Username = self.lineEditUsername_Login.text().strip()
       Password = self.lineEditPassword_Login.text().strip()

       # Kiểm tra nếu username hoặc password rỗng
       if not Username or not Password:
           msgbox = QMessageBox(self.MainWindow)
           msgbox.setIcon(QMessageBox.Icon.Critical)
           msgbox.setText(f"Vui lòng nhập đầy đủ tài khoản và mật khẩu!")
           msgbox.setWindowTitle("Lỗi hệ thống")
           msgbox.exec()
           return

       if self.checkBox.isChecked() and self.checkBox_2.isChecked():
           msgbox = QMessageBox(self.MainWindow)
           msgbox.setIcon(QMessageBox.Icon.Critical)
           msgbox.setText("Không thể đăng nhập cả hai quyền cùng lúc! Vui lòng chọn một.")
           msgbox.setWindowTitle("Lỗi hệ thống")
           msgbox.exec()
           return

       if self.checkBox.isChecked():
           user_info = self.coivalidate_user(Username, Password)  # Kiểm tra User

           if user_info:
               self.MainWindow.close()
               # Đường dẫn đến `current_user.json` trong thư mục `dataset/`
               dataset_path = os.path.join(os.path.dirname(__file__), "../dataset")
               current_user_path = os.path.join(dataset_path, "current_user.json")

               if not os.path.exists(dataset_path):
                   os.makedirs(dataset_path)

               with open(current_user_path, "w", encoding="utf-8") as f:
                   json.dump({"Username": Username}, f)

               self.open_user_ui(user_info)  # Truyền thông tin vào UserInforExt
           else:
               msgbox = QMessageBox(self.MainWindow)
               msgbox.setIcon(QMessageBox.Icon.Critical)
               msgbox.setText(f"Tên đăng nhập hoặc mật khẩu không chính xác!")
               msgbox.setWindowTitle("Lỗi hệ thống")
               msgbox.exec()

       # Nếu chọn đăng nhập Admin
       elif self.checkBox_2.isChecked():
           Admin_list = self.load_admin_data("../dataset/admin.json")  # Tải danh sách admin

           admin = self.coivalidate_admin(Username,Password)
           if admin:
               self.open_admin_ui()
           else:
               msgbox = QMessageBox(self.MainWindow)
               msgbox.setIcon(QMessageBox.Icon.Critical)
               msgbox.setText(f"Tên đăng nhập hoặc mật khẩu không chính xác!")
               msgbox.setWindowTitle("Lỗi hệ thống")
               msgbox.exec()
