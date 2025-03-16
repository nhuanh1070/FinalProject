from PyQt6.QtWidgets import QMessageBox, QMainWindow, QTableWidgetItem
from PyQt6 import QtWidgets
from ui.admin.AdminUi import Ui_MainWindow
from ui.admin.MovieDetailExt import MovieDetailExt
from ui.admin.MovieCreateExt import MovieCreateExt
from ui.admin.MovieEditExt import MovieEditExt
from utils import resources_banner_rc
from utils import resources_poster_rc
from utils import resources_rc
from utils import resources_logo_rc

class AdminUiExt(Ui_MainWindow):
    def __init__(self):
        self.MainWindow = QMainWindow()  # Tạo một QMainWindow mới
        self.setupUi(self.MainWindow)  # Áp dụng giao diện UI

        # Kết nối các sự kiện
        self.setupSignalAndSlot()

        # Cấu hình bảng
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        # Gán danh sách phim mẫu
        self.movies = self.get_sample_movies()

        # Tải danh sách phim lên bảng
        self.load_movies()

    def setupSignalAndSlot(self):
        """ Kết nối các nút với các hộp thoại """
        self.pushButtonDetails.clicked.connect(self.show_movie_details)
        self.pushButtonCreate.clicked.connect(self.show_movie_create)
        self.pushButtonEdit.clicked.connect(self.show_movie_edit)

    def showWindow(self):
        """ Hiển thị cửa sổ chính """
        self.MainWindow.show()

    def get_sample_movies(self):
        """ Trả về danh sách phim mẫu """
        return [
            {
                "name": "Inception",
                "author": "Christopher Nolan",
                "genre": "Khoa học viễn tưởng",
                "country": "Mỹ",
                "duration": "148 phút",
                "year": "2010",
                "description": "Một kẻ trộm chuyên nghiệp xâm nhập vào giấc mơ của người khác để đánh cắp bí mật.",
                "image": "inception.jpg"
            },
            {
                "name": "Parasite",
                "author": "Bong Joon-ho",
                "genre": "Chính kịch",
                "country": "Hàn Quốc",
                "duration": "132 phút",
                "year": "2019",
                "description": "Gia đình nghèo lừa đảo để xâm nhập vào một gia đình giàu có, dẫn đến hậu quả khó lường.",
                "image": "parasite.jpg"
            },
            {
                "name": "The Dark Knight",
                "author": "Christopher Nolan",
                "genre": "Hành động",
                "country": "Mỹ",
                "duration": "152 phút",
                "year": "2008",
                "description": "Batman đối đầu với Joker, kẻ thù đáng gờm nhất của thành phố Gotham.",
                "image": "dark_knight.jpg"
            }
        ]

    def load_movies(self):
        """ Load danh sách phim vào bảng """
        self.tableWidget.setRowCount(len(self.movies))
        for row, movie in enumerate(self.movies):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(movie["name"]))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(movie["genre"]))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(movie["country"]))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(movie["year"]))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(movie["duration"]))

    def show_movie_details(self):
        """ Hiển thị cửa sổ chi tiết phim """
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng chọn một bộ phim!")
            return

        movie = self.movies[selected_row]
        dialog = MovieDetailExt(movie, self.MainWindow)
        dialog.exec()

    def show_movie_edit(self):
        """ Hiển thị cửa sổ chỉnh sửa phim """
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng chọn một bộ phim!")
            return

        movie = self.movies[selected_row]
        dialog = MovieEditExt(movie, self.MainWindow)
        if dialog.exec():
            # Cập nhật lại bảng sau khi chỉnh sửa
            self.load_movies()

    def show_movie_create(self):
        """ Hiển thị cửa sổ tạo phim mới """
        dialog = MovieCreateExt(self.MainWindow)
        if dialog.exec():
            # Thêm phim mới vào danh sách (nếu cần)
            new_movie = {
                "name": dialog.ui.lineEditTitle.text(),
                "author": dialog.ui.lineEditAuthor.text(),
                "genre": dialog.ui.lineEditGenre.text(),
                "country": dialog.ui.lineEditCountry.text(),
                "duration": dialog.ui.lineEditDuration.text(),
                "year": dialog.ui.lineEditYear.text(),
                "description": dialog.ui.textEditDescription.toPlainText(),
                "image": "default.jpg"
            }
            self.movies.append(new_movie)
            self.load_movies()
