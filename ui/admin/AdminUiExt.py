from PyQt6.QtWidgets import QMainWindow, QMessageBox
from PyQt6 import QtWidgets

from ui.admin.AdminUi import Ui_MainWindow
from ui.admin.MovieDetailExt import MovieDetailExt
from ui.admin.MovieCreateExt import MovieCreateExt
from ui.admin.MovieEditExt import MovieEditExt

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setupSignalAndSlot()
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

        self.load_movies()

    def setupSignalAndSlot(self):
        """ Kết nối các nút với các hộp thoại """
        self.ui.pushButtonDetails.clicked.connect(self.show_movie_details)
        self.ui.pushButtonCreate.clicked.connect(self.show_movie_create)
        self.ui.pushButtonEdit.clicked.connect(self.show_movie_edit)

    def load_movies(self):
        """ Load danh sách phim vào bảng """
        self.ui.tableWidget.setRowCount(len(self.movies))
        for row, movie in enumerate(self.movies):
            self.ui.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(movie["name"]))
            self.ui.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(movie["genre"]))
            self.ui.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(movie["country"]))
            self.ui.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(movie["year"]))
            self.ui.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(movie["duration"]))

    def show_movie_details(self):
        """ Hiển thị cửa sổ chi tiết phim """
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một bộ phim!")
            return

        movie = self.movies[selected_row]
        dialog = MovieDetailExt(movie, self)
        dialog.exec()

    def show_movie_edit(self):
        """ Hiển thị cửa sổ chỉnh sửa phim """
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Lỗi", "Vui lòng chọn một bộ phim!")
            return

        movie = self.movies[selected_row]
        dialog = MovieEditExt(movie, self)
        if dialog.exec():
            # Cập nhật lại bảng sau khi chỉnh sửa
            self.load_movies()

    def show_movie_create(self):
        """ Hiển thị cửa sổ tạo phim mới """
        dialog = MovieCreateExt(self)
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