from PyQt6.QtWidgets import QMainWindow, QMessageBox

from CSDL.libs.DataConnector import DataConnector
from CSDL.libs.JsonFileFactory import JsonFileFactory
from CSDL.models.Admin import Admin
from CSDL.models.User import User
from ui.admin.AdminUiExt import AdminUiExt
from ui.login.login import Ui_MainWindow
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
       users_list = jff.read_data(filename, User)
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
       users = self.load_user_data("../dataset/user.json")  # Lấy danh sách Admin từ hệ thống
       for u in users:
           if u.Username == Username and u.Password == Password:
               return 1
       return 0

   def coivalidate_admin(self, Username, Password):
       admins = self.load_admin_data("../dataset/admin.json")  # Lấy danh sách Admin từ hệ thống
       for a in admins:
           if a.Username == Username and a.Password == Password:
               return 1
       return 0

   def open_admin_ui(self):
       """ Mở giao diện Admin """
       # self.MainWindow.close()  # Đóng cửa sổ đăng nhập
       self.mainwindow = QMainWindow()
       self.myui = AdminUiExt()
       self.myui.setupUi(self.mainwindow)
       self.myui.showWindow()

   def open_user_ui(self):
       """ Mở giao diện User """
       # self.MainWindow.close()  # Đóng cửa sổ đăng nhập
       self.mainwindow = QMainWindow()
       self.myui = UserUiExt()
       self.myui.setupUi(self.mainwindow)
       self.myui.showWindow()

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
           User1_list = self.load_user_data("../dataset/user.json")  # Tải danh sách user

           user = self.coivalidate_user(Username, Password)  # Kiểm tra User
           if user:
               self.open_user_ui()
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

       # Nếu không chọn quyền đăng nhập
       else:
           msgbox = QMessageBox(self.MainWindow)
           msgbox.setIcon(QMessageBox.Icon.Critical)
           msgbox.setText(f"Vui lòng chọn quyền đăng nhập!")
           msgbox.setWindowTitle("Lỗi hệ thống")
           msgbox.exec()


