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
       Username = self.lineEditUsername_Signup.text()
       Password = self.lineEditPassword_Signup.text()
       ConfirmPassword = self.lineEditConfirmPassword_Signup.text()

       if not Username or not Password or not ConfirmPassword:
           msg = QMessageBox(self.MainWindow)
           msg.setIcon(QMessageBox.Icon.Warning)
           msg.setText("Vui lòng nhập đầy đủ thông tin.")
           msg.setWindowTitle("Lỗi")
           msg.exec()
           return


       if Password != ConfirmPassword:
           msg = QMessageBox(self.MainWindow)
           msg.setIcon(QMessageBox.Icon.Warning)
           msg.setText("Mật khẩu xác nhận không khớp. Vui lòng thử lại!")
           msg.setWindowTitle("Lỗi")
           msg.exec()
           self.lineEditConfirmPassword_Signup.setText("")
           return

       user = User(self.lineEditUsername_Signup.text(), self.lineEditConfirmPassword_Signup.text())
       index = self.dc.check_user_exist(user.Username)

       if index == -1:
           try:
               self.dc.save_account(user)
               msgbox = QMessageBox(self.MainWindow)
               msgbox.setIcon(QMessageBox.Icon.Information)
               msgbox.setText("Tạo tài khoản thành công.")
               msgbox.setWindowTitle("Xác nhận tạo khoản thành công")
               msgbox.exec()
               self.clear_user_infor()


               Users_list = self.dc.get_all_users()
               if Users_list is None:
                   Users_list = []
               Users_list.append(User(Username, Password))  # Không cần gán lại

               jff = JsonFileFactory()
               filename = "../dataset/user.json"
               jff.write_data(Users_list, filename)

           except Exception as e:
               msgbox = QMessageBox(self.MainWindow)
               msgbox.setIcon(QMessageBox.Icon.Critical)
               msgbox.setText(f"Lỗi khi lưu tài khoản: {str(e)}")
               msgbox.setWindowTitle("Lỗi hệ thống")
               msgbox.exec()
       else:
           msg = QMessageBox(self.MainWindow)
           msg.setIcon(QMessageBox.Icon.Warning)
           msg.setText("Tài khoản đã tồn tại. Vui lòng tạo tài khoản khác")
           msg.setWindowTitle("Lỗi")
           msg.exec()
           self.clear_user_infor()

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
       # Xác định thư mục gốc của project
       project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
       json_path = os.path.join(project_root, "dataset", "users_data.json")  # Đường dẫn đúng

       try:
           with open(json_path, "r", encoding="utf-8") as file:
               users = json.load(file)
       except FileNotFoundError:
           print(f"❌ LỖI: Không thể tải dữ liệu user! File không tồn tại: {json_path}")
           return None
       except json.JSONDecodeError:
           print("❌ LỖI: File JSON bị lỗi, không thể đọc!")
           return None

       if not users:
           print("❌ LỖI: Danh sách user rỗng!")
           return None

       for user in users:
           if user.get("Username") == Username and user.get("Password") == Password:
               print(f"✅ Đăng nhập thành công: {user}")  # Debug dữ liệu user
               return user  # Trả về toàn bộ thông tin user
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
       """ Mở giao diện UserInfor và truyền dữ liệu user """
       if not user_info:
           print("❌ LỖI: Không có dữ liệu user để mở giao diện!")
           return

       print(f"🚀 Đang mở UserInforExt với dữ liệu: {user_info}")

       from ui.user.UserUiExt import UserUiExt
       self.user_info_dialog = UserInforExt(user_info=user_info, user_ui_ext=self)

       try:
           print("🚀 Hiển thị cửa sổ UserInforExt...")
           self.user_info_dialog.show()  # Đổi từ exec() sang show() để tránh crash
       except Exception as e:
           print(f"❌ LỖI: Không thể mở UserInforExt - {e}")

       """ Lấy thông tin user từ file JSON và điền vào các lineEdit 
       filename = "../dataset/UserS.json"
       user_list = self.load_user_infor(filename)  # Lấy danh sách user

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
           QMessageBox.warning(self, "Lỗi", "Không tìm thấy thông tin người dùng!")


"""

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
               print(f"✅ User hợp lệ: {user_info}")  # Debug xem user có được xác thực không
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
   """def load_user_infor(filename):
        #Đọc danh sách user từ file JSON và trả về danh sách đối tượng UserInfor 
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
           return []"""
