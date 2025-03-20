import json
import os
import pandas as pd

from PyQt6.QtWidgets import QMessageBox, QMainWindow, QTableWidgetItem
from PyQt6 import QtWidgets

from CSDL.libs.DataConnector import DataConnector
from CSDL.libs.JsonFileFactory import JsonFileFactory
from CSDL.models.Film import Film
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



    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.MainWindow.ui = self

        self.setupSignalAndSlot()
        # Cấu hình bảng
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)
        # Gán danh sách phim mẫu

        self.movies = self.get_movies_list()

        # Tải danh sách phim lên bảng
        self.load_movies()



        # Load dữ liệu ban đầu
        self.load_revenue_data()
    def setupSignalAndSlot(self):
        """ Kết nối các nút với các hộp thoại """
        self.pushButtonDetails.clicked.connect(self.show_movie_details)
        self.pushButtonCreate.clicked.connect(self.show_movie_create)
        self.pushButtonEdit.clicked.connect(self.show_movie_edit)
        self.pushButtonDelete.clicked.connect(self.delete_movie)
        self.selected_row = -1
        self.btnFilter.clicked.connect(self.filter_data)
    def showWindow(self):
        """ Hiển thị cửa sổ chính """
        self.MainWindow.show()


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


    def show_movie_details(self):
        """ Hiển thị cửa sổ chi tiết phim """
        selected_row = self.tableWidget.currentRow()
        print(f"Selected row: {selected_row}")  # Debug
        if selected_row == -1:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng chọn một bộ phim!")
            return
        movie = self.movies[selected_row]
        dialog = MovieDetailExt(movie, self.MainWindow)
        dialog.exec()

    '''def delete_movie(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng chọn một bộ phim!")
            return'''



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

#cái này tụi t chưa sửa được
    def delete_movie(self):
        """ Xóa bộ phim đang chọn khỏi danh sách `self.movies` và cập nhật `film.json` """
        selected_row = self.tableWidget.currentRow()  # Lấy dòng được chọn
        if selected_row == -1:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng chọn một bộ phim!")
            return
        #`filmTitle` từ cột 0 của bảng
        filmTitle = self.tableWidget.item(selected_row, 0).text().strip().lower()
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Xác nhận xoá")
        dlg.setText(f'Bạn có chắc muốn xoá "{filmTitle}" không?')
        dlg.setIcon(QMessageBox.Icon.Question)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        dlg.setStandardButtons(buttons)

        if dlg.exec()==QMessageBox.StandardButton.No:
            return
        else:
            jff = JsonFileFactory()
            filename = "../../dataset/film.json"
            films= jff.read_data(filename, Film)
            self.dc.remove_film(films, filmTitle)
        self.load_movies()





        '''film_title = self.tableWidget.item(selected_row, 0).text().strip().lower()
        # ✅ Hộp thoại xác nhận xoá
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Xác nhận xoá")
        dlg.setText(f'Bạn có chắc muốn xoá "{film_title}" không?')
        dlg.setIcon(QMessageBox.Icon.Question)
        buttons = QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        dlg.setStandardButtons(buttons)
        button = dlg.exec()

        if button == QMessageBox.StandardButton.No:
            return  # Không làm gì nếu chọn No

        # ✅ Tìm phim cần xóa trong `self.movies`
        movie_to_delete = None
        for movie in self.movies:
            json_film_title = movie.get("filmTitle", "").strip().lower()
            if json_film_title == film_title:
                movie_to_delete = movie
                break

        # ✅ Nếu tìm thấy phim thì xóa, nếu không báo lỗi
        if movie_to_delete:
            self.movies.remove(movie_to_delete)  # Xóa khỏi danh sách
        else:
            QMessageBox.warning(self.MainWindow, "Lỗi", f"Không tìm thấy phim có tên '{film_title}' để xóa!")
            return
        movies=self.movies
        # ✅ Ghi lại file JSON sau khi xóa
        jff = JsonFileFactory()
        filename = "../dataset/film.json"
        jff.write_data(movies, filename)  # Ghi lại danh sách cập nhật

        # ✅ Cập nhật giao diện
        self.load_movies()

        QMessageBox.information(self.MainWindow, "Thành công", f"Đã xóa bộ phim: {film_title}")'''

    def load_revenue_data(self):
        """Đọc dữ liệu từ Excel và tải vào bảng doanh thu."""
        try:
            # Tìm thư mục gốc của dự án
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

            # Đường dẫn đến file Excel
            movie_file = os.path.join(base_dir, "dataset", "data_doanhthuve.xlsx")
            food_file = os.path.join(base_dir, "dataset", "data_doanhthubapnuoc.xlsx")

            # Kiểm tra file tồn tại
            if not os.path.exists(movie_file) or not os.path.exists(food_file):
                QMessageBox.critical(self.MainWindow, "Lỗi", "Không tìm thấy file dữ liệu doanh thu!")
                return

            # Đọc file Excel
            self.movie_data = pd.read_excel(movie_file, engine="openpyxl")
            self.food_data = pd.read_excel(food_file, engine="openpyxl")

            # Kiểm tra dữ liệu có cột "Thời gian"
            if "Thời gian" not in self.movie_data.columns or "Thời gian" not in self.food_data.columns:
                QMessageBox.critical(self.MainWindow, "Lỗi",
                                     "File Excel không có cột 'Thời gian'. Kiểm tra lại dữ liệu!")
                return

            # Lấy danh sách tháng/năm và thêm vào ComboBox
            unique_months = sorted(set(self.movie_data["Thời gian"]).union(set(self.food_data["Thời gian"])))
            self.comboMonthYear.clear()  # Xóa dữ liệu cũ
            self.comboMonthYear.addItems(unique_months)  # Thêm danh sách mới

            # Hiển thị dữ liệu lên bảng
            self.populate_table(self.movie_data, self.tableMovies)
            self.populate_table(self.food_data, self.tableFoods)
            self.calculate_total_revenue()

        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Lỗi khi đọc file Excel: {str(e)}")

    def populate_table(self, data, table_widget):
        """Hiển thị dữ liệu vào QTableWidget."""
        table_widget.setRowCount(len(data))
        table_widget.setColumnCount(len(data.columns))
        table_widget.setHorizontalHeaderLabels(data.columns)

        for row_idx, row in data.iterrows():
            for col_idx, value in enumerate(row):
                table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

    def filter_data(self):
        """Lọc dữ liệu theo tháng/năm được chọn từ comboMonthYear"""
        selected_month_year = self.comboMonthYear.currentText()  # Lấy giá trị được chọn

        if not selected_month_year:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng chọn tháng/năm để lọc!")
            return

        # Lọc dữ liệu từ DataFrame
        filtered_movies = self.movie_data[self.movie_data["Thời gian"] == selected_month_year]
        filtered_foods = self.food_data[self.food_data["Thời gian"] == selected_month_year]

        if filtered_movies.empty and filtered_foods.empty:
            QMessageBox.warning(self.MainWindow, "Thông báo", "Không có dữ liệu cho tháng đã chọn!")
            return

        # Hiển thị dữ liệu sau khi lọc
        self.populate_table(filtered_movies, self.tableMovies)
        self.populate_table(filtered_foods, self.tableFoods)
        self.calculate_total_revenue(filtered_movies, filtered_foods)

    def calculate_total_revenue(self, movies=None, foods=None):
        """Tính tổng doanh thu và hiển thị."""
        if movies is None:
            movies = self.movie_data
        if foods is None:
            foods = self.food_data

        movie_revenue = movies["Doanh thu"].sum()
        food_revenue = foods["Doanh thu"].sum()
        total_revenue = movie_revenue + food_revenue

        self.lblMovieRevenue.setText(f"Doanh thu phim: {movie_revenue:,} VND")
        self.lblFoodRevenue.setText(f"Doanh thu bắp nước: {food_revenue:,} VND")
        self.lblTotalRevenue.setText(f"Tổng doanh thu: {total_revenue:,} VND")
