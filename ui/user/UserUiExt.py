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
        self.movie_data = self.get_movie_data()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.MainWindow.ui = self
        # Gán sự kiện click cho các nút chuyển trang
        self.setupSignalAndSlot()

    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        # Sự kiện nút bấm chuyển trang
        self.pushButton_Right.clicked.connect(self.nextPage)
        self.pushButton_Left.clicked.connect(self.prevPage)
        self.Account_btn.clicked.connect(self.showUserInfo)
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
    def get_movie_data(self):
        # Danh sách dữ liệu phim
        return [
            {"title": "AVATAR: THE WAY OF WATER", "genre": "Sci-Fi", "duration": "192'", "language": "English", "rating": "T13", "poster": ":/Poster/images/Poster/Avatar.jpg", "description": "Jake Sully lives with his newfound family on the moon Pandora..."},
            {"title": "DUNE PART TWO", "genre": "Action", "duration": "165'", "language": "English", "rating": "T16", "poster": ":/Poster/images/Poster/Dune.jpg", "description": "Paul Atreides unites with Chani and the Fremen while seeking revenge..."},
            {"title": "FAST X", "genre": "Action", "duration": "141'", "language": "English", "rating": "T13", "poster": ":/Poster/images/Poster/FastX.jpg", "description": "Dominic Toretto and his family are targeted by the vengeful son of drug kingpin Hernan Reyes..."},
            {"title": "JOHN WICK 4", "genre": "Action", "duration": "169'", "language": "English", "rating": "T18", "poster": ":/Poster/images/Poster/JohnWick.jpg", "description": "John Wick uncovers a path to defeating The High Table..."},
            {"title": "SPIDERMAN", "genre": "Adventure", "duration": "133'", "language": "English", "rating": "T12", "poster": ":/Poster/images/Poster/Spiderman.jpg", "description": "Spider-Man must fight foes from multiple universes..."},
            {"title": "THE CONJURING", "genre": "Horror", "duration": "112'", "language": "English", "rating": "T18", "poster": ":/Poster/images/Poster/TheConjuring.jpg", "description": "Paranormal investigators Ed and Lorraine Warren work to help a family terrorized by a dark presence..."}
        ]




