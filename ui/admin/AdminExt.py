from PyQt6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PyQt6 import QtWidgets

from ui.admin.MovieDetailExt import MovieDetailExt
from ui.admin.test import Ui_MainWindow
  # Import class xử lý cửa sổ chi tiết phim

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Cấu hình bảng
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

        # Danh sách phim mẫu
        self.movies = [
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

        # Load phim vào bảng
        self.load_movies()

        # Bắt sự kiện nút xem chi tiết
        self.ui.pushButtonDetails.clicked.connect(self.show_movie_details)

    def load_movies(self):
        self.ui.tableWidget.setRowCount(len(self.movies))
        for row, movie in enumerate(self.movies):
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(movie["name"]))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(movie["genre"]))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(movie["country"]))
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(movie["year"]))
            self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(movie["duration"]))

    def show_movie_details(self):
        # Lấy dòng được chọn
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một bộ phim!")
            return

        # Lấy thông tin phim
        movie = self.movies[selected_row]

        # Hiển thị cửa sổ chi tiết phim
        dialog = MovieDetailExt(movie, self)
        dialog.exec()