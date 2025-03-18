import json
import os

from PyQt6.QtWidgets import QMessageBox, QMainWindow, QTableWidgetItem
from PyQt6 import QtWidgets

from CSDL.libs.DataConnector import DataConnector
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
        self.dc = DataConnector()
        # Kết nối các sự kiện
        self.setupSignalAndSlot()

        # Cấu hình bảng
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        # Gán danh sách phim mẫu
        self.movies = self.get_movies_list()

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

    '''def get_sample_movies(self):
        Trả về danh sách phim mẫu
        return [
            # Danh sách phim gốc
            {
                "filmId": "Sample1",
                "filmTitle": "Inception",
                "author": "Christopher Nolan",
                "genre": "Khoa học viễn tưởng",
                "country": "Mỹ",
                "duration": "148 phút",
                "year": "2010",
                "description": "Một kẻ trộm chuyên nghiệp xâm nhập vào giấc mơ của người khác để đánh cắp bí mật.",
                "image": "inception.jpg",
                "language": "Tiếng Anh",
                "releaseDate": "16/07/2010",
                "rating": "PG-13",
                "showtimes": "20:00",
                "inventory": 10
            },
            {
                "filmId": "Sample2",
                "filmTitle": "Parasite",
                "author": "Bong Joon-ho",
                "genre": "Chính kịch",
                "country": "Hàn Quốc",
                "duration": "132 phút",
                "year": "2019",
                "description": "Gia đình nghèo lừa đảo để xâm nhập vào một gia đình giàu có, dẫn đến hậu quả khó lường.",
                "image": "parasite.jpg",
                "language": "Tiếng Hàn",
                "releaseDate": "30/05/2019",
                "rating": "R",
                "showtimes": "18:45",
                "inventory": 8
            },
            {
                "filmId": "Sample3",
                "filmTitle": "The Dark Knight",
                "author": "Christopher Nolan",
                "genre": "Hành động",
                "country": "Mỹ",
                "duration": "152 phút",
                "year": "2008",
                "description": "Batman đối đầu với Joker, kẻ thù đáng gờm nhất của thành phố Gotham.",
                "image": "dark_knight.jpg",
                "language": "Tiếng Anh",
                "releaseDate": "18/07/2008",
                "rating": "PG-13",
                "showtimes": "21:30",
                "inventory": 12
            },

            # Danh sách phim mở rộng
            {
                "filmId": "F1",
                "filmTitle": "Anyone but you",
                "genre": "Tình cảm",
                "duration": "103 phút",
                "country": "Mỹ",
                "language": "Phụ đề tiếng Việt",
                "releaseDate": "25/03/2024",
                "rating": "18",
                "showtimes": "9:30",
                "inventory": 5
            },
            {
                "filmId": "F2",
                "filmTitle": "John Wick 4",
                "genre": "Hành động",
                "duration": "169 phút",
                "country": "Mỹ",
                "language": "Lồng tiếng",
                "releaseDate": "24/03/2024",
                "rating": "18+",
                "showtimes": "20:00",
                "inventory": 10
            },
            {
                "filmId": "F3",
                "filmTitle": "The Marvels",
                "genre": "Siêu anh hùng",
                "duration": "130 phút",
                "country": "Mỹ",
                "language": "Phụ đề tiếng Việt",
                "releaseDate": "22/03/2024",
                "rating": "PG-13",
                "showtimes": "17:30",
                "inventory": 8
            },
            {
                "filmId": "F4",
                "filmTitle": "Oppenheimer",
                "genre": "Chính kịch",
                "duration": "180 phút",
                "country": "Mỹ",
                "language": "Phụ đề tiếng Việt",
                "releaseDate": "21/03/2024",
                "rating": "R",
                "showtimes": "19:00",
                "inventory": 12
            },
            {
                "filmId": "F5",
                "filmTitle": "Inside Out 2",
                "genre": "Hoạt hình",
                "duration": "100 phút",
                "country": "Mỹ",
                "language": "Lồng tiếng",
                "releaseDate": "26/03/2024",
                "rating": "PG",
                "showtimes": "14:00",
                "inventory": 15
            },
            {
                "filmId": "F6",
                "filmTitle": "Dune: Part Two",
                "genre": "Khoa học viễn tưởng",
                "duration": "166 phút",
                "country": "Mỹ",
                "language": "Phụ đề tiếng Việt",
                "releaseDate": "27/03/2024",
                "rating": "PG-13",
                "showtimes": "21:00",
                "inventory": 7
            },
            {
                "filmId": "F7",
                "filmTitle": "Avatar: The Way of Water",
                "genre": "Khoa học viễn tưởng",
                "duration": "192 phút",
                "country": "Mỹ",
                "language": "Phụ đề tiếng Việt",
                "releaseDate": "28/03/2024",
                "rating": "PG-13",
                "showtimes": "18:30",
                "inventory": 9
            },
            {
                "filmId": "F8",
                "filmTitle": "Spider-Man: No Way Home",
                "genre": "Siêu anh hùng",
                "duration": "148 phút",
                "country": "Mỹ",
                "language": "Lồng tiếng",
                "releaseDate": "29/03/2024",
                "rating": "PG-13",
                "showtimes": "20:00",
                "inventory": 6
            },
            {
                "filmId": "F9",
                "filmTitle": "The Conjuring: The Devil Made Me Do It",
                "genre": "Kinh dị",
                "duration": "112 phút",
                "country": "Mỹ",
                "language": "Phụ đề tiếng Việt",
                "releaseDate": "30/03/2024",
                "rating": "R",
                "showtimes": "22:00",
                "inventory": 5
            },
            {
                "filmId": "F10",
                "filmTitle": "Fast X",
                "genre": "Hành động",
                "duration": "141 phút",
                "country": "Mỹ",
                "language": "Lồng tiếng",
                "releaseDate": "31/03/2024",
                "rating": "PG-13",
                "showtimes": "16:00",
                "inventory": 10
            }
        ]
jfijf'''





    def get_movies_list(self):
        """ Đọc danh sách phim từ file JSON """
        file_path = "../dataset/film.json"

        # Kiểm tra file có tồn tại không
        if not os.path.exists(file_path):
            print("❌ Lỗi: File dữ liệu không tồn tại!")
            return []

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)  # Đọc JSON

                if isinstance(data, list):
                    return data  # Trả về danh sách phim

                print("❌ Lỗi: Dữ liệu JSON không hợp lệ!")
                return []
        except json.JSONDecodeError:
            print("❌ Lỗi: Không thể đọc file JSON!")
            return []

    def load_movies(self):
        """ Load danh sách phim vào bảng """
        self.tableWidget.setRowCount(len(self.movies))  # Cập nhật số dòng trong bảng

        for row, movie in enumerate(self.movies):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(movie["filmTitle"]))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(movie["Gerne"]))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(movie["Country"]))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(movie["ReleaseDate"]))

            # ✅ Sửa lỗi duration: Ép thành chuỗi nếu là số
            self.tableWidget.setItem(row, 4, QTableWidgetItem(str(movie["Duration"])))


    '''def load_movies(self):
        """ Load danh sách phim vào bảng """
        self.tableWidget.setRowCount(len(self.movies))
        for row, movie in enumerate(self.movies):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(movie["filmTitle"]))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(movie["Gerne"]))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(movie["Country"]))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(movie["ReleaseDate"]))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(movie["Duration"]))'''

    '''def load_movies(self):
        """ Load danh sách phim vào bảng """
        self.tableWidget.setRowCount(len(self.movies))
        for row, movie in enumerate(self.movies):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(movie.get("filmTitle", "N/A")))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(movie.get("genre", "N/A")))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(movie.get("country", "N/A")))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(movie.get("releaseDate", "N/A")))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(movie.get("duration", "N/A")))'''

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
