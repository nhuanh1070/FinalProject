from PyQt6.QtWidgets import QMainWindow, QMessageBox

from CSDL.libs.DataConnector import DataConnector
from CSDL.libs.JsonFileFactory import JsonFileFactory
from CSDL.models.User import User
from CSDL.test.TestDataConnector import dc
from CSDL.test.TestUser_WriteJson import users
from ui.login.login import Ui_MainWindow

class LoginUiExt(Ui_MainWindow):
    def __init__(self):
        self.MainWindow = QMainWindow()
        self.setupUi(self.MainWindow)

        self.dc=DataConnector()


    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.MainWindow.ui = self


        # Đặt trang đầu tiên hiển thị
        self.stackedWidget.setCurrentIndex(0)

        # Gán sự kiện click cho các nút chuyển trang
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        """ Gán sự kiện cho các nút để chuyển trang """
        self.pushButtonTo_Register.clicked.connect(self.showRegisterPage)
        self.pushButtonTo_Login.clicked.connect(self.showLoginPage)
        self.pushButtonRegister.clicked.connect(self.register_process)
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

    '''def register_process(self):
        Username=self.lineEditUsername_Signup.text()
        Password=self.lineEditPassword_Signup.text()
        ConfirmPassword=self.lineEditConfirmPassword_Signup.text()
        user=User(Username,Password)
        index = self.dc.check_user_exist(user.Username)
        if Password==ConfirmPassword:
            if index == -1:
                self.dc.save_account(user)
                msgbox = QMessageBox(self.MainWindow)
                msgbox.setIcon(QMessageBox.Icon.Information)
                msgbox.setText("Tạo tài khoản thành công.")
                msgbox.setWindowTitle("Xác nhân tạo khoản thành công")
                self.clear_user_infor()
            else:
                self.msg = QMessageBox(self.MainWindow)
                self.msg.setText("Tài khoản đã tồn tại. Vui lòng tạo tài khoản khác")
                self.msg.exec()
                self.clear_user_infor()
        else:
            self.msg = QMessageBox(self.MainWindow)
            self.msg.setText("Vui lòng xác nhận đúng mật khẩu đã nhập")
            self.msg.exec()
            self.lineEditConfirmPassword_Signup.setText("")'''

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
                #self.dc.save_account(user)
                msgbox = QMessageBox(self.MainWindow)
                msgbox.setIcon(QMessageBox.Icon.Information)
                msgbox.setText("Tạo tài khoản thành công.")
                msgbox.setWindowTitle("Xác nhận tạo khoản thành công")
                msgbox.exec()  # Gọi exec() để hiển thị hộp thoại
                self.clear_user_infor()
                Users_list=dc.get
                jff = JsonFileFactory()
                filename = "../dataset/user.json"
                jff.write_data(users, filename)
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











