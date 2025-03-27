
import json
import os
import pandas as pd

from PyQt6.QtWidgets import QMessageBox, QMainWindow, QTableWidgetItem
from PyQt6 import QtWidgets, QtCore

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
        self.MainWindow = QMainWindow()
        self.setupUi(self.MainWindow)
        self.dc = DataConnector()

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.MainWindow.ui = self

        self.setupSignalAndSlot()
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectionBehavior.SelectRows)

        self.movies = self.get_movies_list()
        self.filtered_movies = self.movies.copy()
        self.load_all_movies()
        self.completer_model = QtCore.QStringListModel()
        self.completer = QtWidgets.QCompleter(self.completer_model, self.lineEdit_6)
        self.completer.setCaseSensitivity(QtCore.Qt.CaseSensitivity.CaseInsensitive)
        self.completer.setFilterMode(QtCore.Qt.MatchFlag.MatchContains)
        self.lineEdit_6.setCompleter(self.completer)

        self.load_revenue_data()

    def setupSignalAndSlot(self):
        self.pushButtonDetails.clicked.connect(self.show_movie_details)
        self.pushButtonCreate.clicked.connect(self.show_movie_create)
        self.pushButtonEdit.clicked.connect(self.show_movie_edit)
        self.pushButtonDelete.clicked.connect(self.delete_movie)
        self.lineEdit_6.textChanged.connect(self.search_movie)
        self.btnFilter.clicked.connect(self.filter_data)

    def showWindow(self):
        self.MainWindow.show()

    def get_movies_list(self):
        file_path = "../dataset/film.json"
        if not os.path.exists(file_path):
            print("❌ Lỗi: File dữ liệu không tồn tại!")
            return []
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data if isinstance(data, list) else []
        except json.JSONDecodeError:
            print("❌ Lỗi: Không thể đọc file JSON!")
            return []

    def load_all_movies(self):
        self.load_movie(self.movies)

    def load_movie(self, movie_list):
        self.filtered_movies = movie_list.copy()  # ✅ fixed: use a copy to avoid reference issues
        self.tableWidget.setRowCount(len(movie_list))
        for row, movie in enumerate(movie_list):
            self.tableWidget.setItem(row, 0, QTableWidgetItem(movie["filmTitle"]))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(movie["Gerne"]))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(movie["Country"]))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(movie["ReleaseDate"]))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(str(movie["Duration"])))

    def show_movie_details(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1 or selected_row >= len(self.filtered_movies):
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng chọn một bộ phim!")
            return
        movie = self.filtered_movies[selected_row]
        dialog = MovieDetailExt(movie, self.MainWindow)
        dialog.exec()

    def show_movie_edit(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1 or selected_row >= len(self.filtered_movies):
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng chọn một bộ phim!")
            return
        movie = self.filtered_movies[selected_row]
        dialog = MovieEditExt(movie, self.MainWindow)
        if dialog.exec():
            self.movies = self.get_movies_list()
            self.load_all_movies()

    def show_movie_create(self):
        dialog = MovieCreateExt(self.MainWindow)
        if dialog.exec():
            # ✅ Đọc lại danh sách phim từ file JSON sau khi tạo mới
            self.movies = self.get_movies_list()
            self.load_all_movies()

    def delete_movie(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row == -1 or selected_row >= len(self.filtered_movies):
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng chọn một bộ phim!")
            return

        filmTitle = self.filtered_movies[selected_row]["filmTitle"]
        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Xác nhận xoá")
        dlg.setText(f'Bạn có chắc muốn xoá "{filmTitle}" không?')
        dlg.setIcon(QMessageBox.Icon.Question)
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if dlg.exec() == QMessageBox.StandardButton.No:
            return

        try:
            file_path = "../dataset/film.json"
            with open(file_path, "r", encoding="utf-8") as file:
                films = json.load(file)

            updated_films = [film for film in films if film["filmTitle"] != filmTitle]

            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(updated_films, file, indent=4, ensure_ascii=False)

            QMessageBox.information(self.MainWindow, "Thành công", "Phim đã được xoá!")
            self.movies = updated_films
            self.load_all_movies()
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Lỗi khi xoá phim: {str(e)}")

    def load_revenue_data(self):
        try:
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
            movie_file = os.path.join(base_dir, "dataset", "data_doanhthuve.xlsx")
            food_file = os.path.join(base_dir, "dataset", "data_doanhthubapnuoc.xlsx")

            if not os.path.exists(movie_file) or not os.path.exists(food_file):
                QMessageBox.critical(self.MainWindow, "Lỗi", "Không tìm thấy file dữ liệu doanh thu!")
                return

            self.movie_data = pd.read_excel(movie_file, engine="openpyxl", dtype=str)
            self.food_data = pd.read_excel(food_file, engine="openpyxl", dtype=str)

            self.movie_data["Doanh thu"] = pd.to_numeric(self.movie_data["Doanh thu"], errors="coerce").fillna(0)
            self.food_data["Doanh thu"] = pd.to_numeric(self.food_data["Doanh thu"], errors="coerce").fillna(0)

            if "Thời gian" not in self.movie_data.columns or "Thời gian" not in self.food_data.columns:
                QMessageBox.critical(self.MainWindow, "Lỗi", "File Excel không có cột 'Thời gian'. Kiểm tra lại dữ liệu!")
                return

            unique_months = sorted(set(self.movie_data["Thời gian"]).union(set(self.food_data["Thời gian"])))
            self.comboMonthYear.clear()
            self.comboMonthYear.addItems(unique_months)
            self.populate_table(self.movie_data, self.tableMovies)
            self.populate_table(self.food_data, self.tableFoods)

            self.tableMovies.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
            self.tableFoods.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)



            self.calculate_total_revenue()

        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Lỗi khi đọc file Excel: {str(e)}")

    def populate_table(self, data, table_widget):
        table_widget.setRowCount(len(data))
        table_widget.setColumnCount(len(data.columns))
        table_widget.setHorizontalHeaderLabels(data.columns)

        for row_idx, row in data.iterrows():
            for col_idx, value in enumerate(row):
                table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

    def filter_data(self):
        selected_month_year = self.comboMonthYear.currentText().strip()
        if not selected_month_year:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng chọn tháng/năm để lọc!")
            return

        # Làm sạch cột thời gian
        self.movie_data["Thời gian"] = self.movie_data["Thời gian"].astype(str).str.strip()
        self.food_data["Thời gian"] = self.food_data["Thời gian"].astype(str).str.strip()

        # Lọc dữ liệu đúng tháng/năm
        filtered_movies = self.movie_data[self.movie_data["Thời gian"] == selected_month_year]
        filtered_foods = self.food_data[self.food_data["Thời gian"] == selected_month_year]

        if filtered_movies.empty and filtered_foods.empty:
            QMessageBox.warning(self.MainWindow, "Thông báo", "Không có dữ liệu cho tháng đã chọn!")
            return

        # Sắp xếp dữ liệu theo đúng thứ tự dòng (nếu có nhiều loại trong tháng)
        filtered_movies = filtered_movies.reset_index(drop=True)
        filtered_foods = filtered_foods.reset_index(drop=True)

        # Hiển thị lại bảng
        self.populate_table(filtered_movies, self.tableMovies)
        self.populate_table(filtered_foods, self.tableFoods)

        # Tính doanh thu
        self.calculate_total_revenue(filtered_movies, filtered_foods)

    def calculate_total_revenue(self, movies=None, foods=None):
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

    def search_movie(self, text):
        text = text.strip().lower()
        if text == "":
            self.load_all_movies()
            return

        filtered_movies = []
        for movie in self.movies:
            title = movie.get("filmTitle", "").lower()
            if text in title:
                filtered_movies.append(movie)

        self.load_movie(filtered_movies)

        completer_list = [movie.get("filmTitle", "") for movie in filtered_movies]
        self.completer_model.setStringList(completer_list)
