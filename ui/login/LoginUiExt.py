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

       print(f"📌 Debug - Username nhập: {Username}")
       print(f"📌 Debug - Password nhập: {Password}")

       if not Username or not Password or not ConfirmPassword:
           print("❌ LỖI: Không nhập đủ thông tin!")
           QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng nhập đầy đủ thông tin.")
           return

       if Password != ConfirmPassword:
           print("❌ LỖI: Mật khẩu không khớp!")
           QMessageBox.warning(self.MainWindow, "Lỗi", "Mật khẩu xác nhận không khớp. Vui lòng thử lại!")
           self.lineEditConfirmPassword_Signup.clear()
           return

       user = User(Username, Password)
       print(f"📌 Debug - Đang kiểm tra username {Username} trong database...")
       index = self.dc.check_user_exist(user.Username)

       if index == -1:
           try:
               print("📌 Debug - Đang lưu tài khoản vào database...")
               success = self.dc.save_account(user)

               if success:
                   print(f"✅ Tài khoản {Username} đã được lưu!")
                   QMessageBox.information(self.MainWindow, "Thành công", "Tạo tài khoản thành công.")
                   self.clear_user_infor()
               else:
                   print("❌ LỖI: Lưu tài khoản thất bại!")
                   QMessageBox.warning(self.MainWindow, "Lỗi", "Lưu tài khoản thất bại!")
           except Exception as e:
               print(f"❌ LỖI HỆ THỐNG: {str(e)}")
               QMessageBox.critical(self.MainWindow, "Lỗi hệ thống", f"Lỗi khi lưu tài khoản: {str(e)}")
       else:
           print("❌ LỖI: Username đã tồn tại!")
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
           print(f"❌ LỖI: Không tìm thấy file {json_path}")
           return None

       try:
           with open(json_path, "r", encoding="utf-8") as file:
               users = json.load(file)
       except json.JSONDecodeError:
           print("❌ LỖI: File JSON bị lỗi, không thể đọc!")
           return None

       for user in users:
           if user.get("Username") == Username and user.get("Password") == Password:
               print(f"✅ Đăng nhập thành công: {user}")
               return user  # Trả về toàn bộ user_info

       print(f"❌ Không tìm thấy tài khoản: {Username}")
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
       print("📂 Debug - user_info truyền vào UserInforExt:")
       print(user_info)

       try:
           self.user_info_dialog = UserInforExt(user_info=user_info)
           self.user_info_dialog.exec()
       except Exception as e:
           print(f"❌ LỖI: Không thể mở giao diện người dùng - {e}")
           QMessageBox.critical(self.MainWindow, "Lỗi hệ thống", f"Không thể mở giao diện người dùng: {e}")
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
               self.MainWindow.close()
               # 🔹 Đường dẫn đến `current_user.json` trong thư mục `dataset/`
               dataset_path = os.path.join(os.path.dirname(__file__), "../dataset")
               current_user_path = os.path.join(dataset_path, "current_user.json")

               # 🔹 Kiểm tra nếu thư mục `dataset/` không tồn tại, thì tạo mới
               if not os.path.exists(dataset_path):
                   os.makedirs(dataset_path)

               # 🔹 Lưu username đang đăng nhập vào file `dataset/current_user.json`
               try:
                   with open(current_user_path, "w", encoding="utf-8") as f:
                       json.dump({"Username": Username}, f)
                   print(f"✅ Đã lưu user đang đăng nhập: {Username} tại {current_user_path}")
               except Exception as e:
                   print(f"❌ LỖI: Không thể ghi file current_user.json - {e}")

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
