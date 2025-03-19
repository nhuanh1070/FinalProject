from PyQt6.QtWidgets import QMainWindow

from ui.user.BookTicketExt import BookTicketExt
from ui.user.UserInforExt import UserInforExt
from ui.user.UserUi import Ui_MainWindow
from ui.user.ViewDetailExt import ViewDetailExt
from utils import resources_banner_rc
from utils import resources_poster_rc
from utils import resources_rc
from utils import resources_logo_rc


class UserUiExt(Ui_MainWindow):
    def __init__(self):
        self.MainWindow = QMainWindow()
        self.setupUi(self.MainWindow)

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.MainWindow.ui = self
        # Gán sự kiện click cho các nút chuyển trang
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.Account_btn.clicked.connect(self.showUserInfo)
        # Sự kiện nút bấm chuyển trang
        self.pushButton_Right.clicked.connect(self.nextPage)
        self.pushButton_Left.clicked.connect(self.prevPage)
        # Kết nối các nút View Details với phim tương ứng
        self.btn_ViewDetails_1.clicked.connect(lambda: self.showMovieDetail(0))
        self.btn_ViewDetails_7.clicked.connect(lambda: self.showMovieDetail(1))
        self.btn_ViewDetails_8.clicked.connect(lambda: self.showMovieDetail(2))
        self.btn_ViewDetails_12.clicked.connect(lambda: self.showMovieDetail(3))
        self.btn_ViewDetails_11.clicked.connect(lambda: self.showMovieDetail(4))
        self.btn_ViewDetails_10.clicked.connect(lambda: self.showMovieDetail(5))
        """Gán sự kiện cho các nút"""
        self.btn_BookTicket_1.clicked.connect(lambda: self.bookTicket(0))
        self.btn_BookTicket_5.clicked.connect(lambda: self.bookTicket(1))
        self.btn_BookTicket_7.clicked.connect(lambda: self.bookTicket(2))
        self.btn_BookTicket_11.clicked.connect(lambda: self.bookTicket(3))
        self.btn_BookTicket_10.clicked.connect(lambda: self.bookTicket(4))
        self.btn_BookTicket_9.clicked.connect(lambda: self.bookTicket(5))

    def bookTicket(self, movie_index):
        """Mở giao diện đặt vé"""
        try:
            movie = self.movie_data[movie_index]
            self.MainWindow.close()
            book_ticket_dialog = BookTicketExt(movie)
            book_ticket_dialog.exec()
        except IndexError:
            print(f"LỖI: Không tìm thấy phim với index {movie_index}!")
        except Exception as e:
            print(f"LỖI: Không thể mở giao diện BookTicket! {e}")
    def nextPage(self):
        current_index = self.stackedWidget.currentIndex()
        next_index = (current_index + 1) % self.stackedWidget.count()
        self.stackedWidget.setCurrentIndex(next_index)

    def prevPage(self):
        current_index = self.stackedWidget.currentIndex()
        prev_index = (current_index - 1) % self.stackedWidget.count()
        self.stackedWidget.setCurrentIndex(prev_index)
    def showMovieDetail(self, movie_index):
        movie = self.movie_data[movie_index]
        detail_dialog = ViewDetailExt(movie)
        detail_dialog.exec()
    def showUserInfo(self):
        """Mở cửa sổ thông tin người dùng"""
        self.user_info_dialog = UserInforExt(movie=None)
        self.user_info_dialog.exec()




