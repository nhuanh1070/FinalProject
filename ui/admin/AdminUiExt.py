
import json
import os
from datetime import datetime

import pandas as pd

from PyQt6.QtWidgets import QMessageBox, QMainWindow, QTableWidgetItem
from PyQt6 import QtWidgets, QtCore
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
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

            # Đọc file Excel mà không ép kiểu, để pandas tự xác định kiểu dữ liệu
            self.movie_data = pd.read_excel(movie_file, engine="openpyxl")
            self.food_data = pd.read_excel(food_file, engine="openpyxl")

            # Chuyển cột "Doanh thu" về numeric
            self.movie_data["Revenue"] = pd.to_numeric(self.movie_data["Revenue"], errors="coerce").fillna(0)
            self.food_data["Revenue"] = pd.to_numeric(self.food_data["Revenue"], errors="coerce").fillna(0)

            if "Datetime" not in self.movie_data.columns or "Datetime" not in self.food_data.columns:
                QMessageBox.critical(self.MainWindow, "Lỗi",
                                     "File Excel không có cột 'Thời gian'. Kiểm tra lại dữ liệu!")
                return

            # Chuyển đổi cột "Thời gian" về kiểu datetime (không chỉ định format để linh hoạt hơn)
            self.movie_data["Datetime"] = pd.to_datetime(self.movie_data["Datetime"], errors="coerce")
            self.food_data["Datetime"] = pd.to_datetime(self.food_data["Datetime"], errors="coerce")


            # Chuyển đổi datetime thành chuỗi "YYYY-MM" để đồng nhất cho việc lọc
            self.movie_data["Datetime"] = self.movie_data["Datetime"].dt.strftime('%Y-%m')
            self.food_data["Datetime"] = self.food_data["Datetime"].dt.strftime('%Y-%m')

            # Lấy danh sách tháng năm đã sắp xếp từ dữ liệu
            unique_months = sorted(set(self.movie_data["Datetime"]).union(set(self.food_data["Datetime"])))

            # Cập nhật vào combobox
            self.comboMonthYear_1.clear()
            self.comboMonthYear_1.addItems(unique_months)
            self.comboMonthYear_2.clear()
            self.comboMonthYear_2.addItems(unique_months)

            self.populate_table(self.movie_data, self.tableMovies)
            self.populate_table(self.food_data, self.tableFoods)

            self.tableMovies.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)
            self.tableFoods.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.ResizeToContents)

            self.calculate_total_revenue()

            # Vẽ biểu đồ ban đầu
            self.draw_movie_chart()
            self.draw_food_chart()
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Lỗi khi đọc file Excel: {str(e)}")

    def filter_data(self):
        # Lấy giá trị từ combobox tháng bắt đầu và tháng kết thúc
        start_month = self.comboMonthYear_1.currentText().strip()
        end_month = self.comboMonthYear_2.currentText().strip()

        print(f"Start month: {start_month}, End month: {end_month}")

        if not start_month or not end_month:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng chọn tháng bắt đầu và tháng kết thúc để lọc!")
            return

        try:
            # Chuyển chuỗi tháng/năm (YYYY-MM) thành datetime object
            start_date = datetime.strptime(start_month, "%Y-%m")
            end_date = datetime.strptime(end_month, "%Y-%m")
            print(f"Start date: {start_date}, End date: {end_date}")

            if end_date < start_date:
                QMessageBox.warning(self.MainWindow, "Lỗi", "Tháng kết thúc phải lớn hơn hoặc bằng tháng bắt đầu!")
                return

            # Chuyển datetime về chuỗi định dạng "YYYY-MM" để so sánh với cột "Thời gian"
            start_str = start_date.strftime("%Y-%m")
            end_str = end_date.strftime("%Y-%m")
        except ValueError as e:
            QMessageBox.warning(self.MainWindow, "Lỗi", f"Định dạng tháng/năm không đúng: {e}")
            return

        # Lọc dữ liệu dựa trên chuỗi "YYYY-MM"
        filtered_movies = self.movie_data[
            (self.movie_data["Datetime"] >= start_str) & (self.movie_data["Datetime"] <= end_str)]
        filtered_foods = self.food_data[
            (self.food_data["Datetime"] >= start_str) & (self.food_data["Datetime"] <= end_str)]

        print(f"Filtered movies: {filtered_movies.shape}")
        print(f"Filtered foods: {filtered_foods.shape}")

        if filtered_movies.empty and filtered_foods.empty:
            QMessageBox.warning(self.MainWindow, "Thông báo", "Không có dữ liệu cho khoảng thời gian đã chọn!")
            return

        # Cập nhật lại bảng, doanh thu và biểu đồ với dữ liệu đã lọc
        self.populate_table(filtered_movies, self.tableMovies)
        self.populate_table(filtered_foods, self.tableFoods)
        self.calculate_total_revenue(filtered_movies, filtered_foods)
        self.draw_movie_chart(filtered_movies)
        self.draw_food_chart(filtered_foods)

    def populate_table(self, data, table_widget):
        table_widget.setRowCount(len(data))
        table_widget.setColumnCount(len(data.columns))
        table_widget.setHorizontalHeaderLabels(data.columns)

        for row_idx, row in data.iterrows():
            for col_idx, value in enumerate(row):
                table_widget.setItem(row_idx, col_idx, QTableWidgetItem(str(value)))

    def calculate_total_revenue(self, movies=None, foods=None):
        if movies is None:
            movies = self.movie_data
        if foods is None:
            foods = self.food_data

        movie_revenue = movies["Revenue"].sum()
        food_revenue = foods["Revenue"].sum()
        total_revenue = movie_revenue + food_revenue

        self.lblMovieRevenue.setText(f"{movie_revenue:,}")
        self.lblFoodRevenue.setText(f"{food_revenue:,}")
        self.lblTotalRevenue.setText(f"{total_revenue:,}")

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

    def draw_movie_chart(self, data=None):
        if data is None:
            data = self.movie_data


        # Thiết lập layout cho QFrame frameChartMovie
        layout = self.frameChartMovie.layout()
        if layout is None:
            layout = QtWidgets.QVBoxLayout(self.frameChartMovie)
        else:
            # Xóa hết các widget cũ nếu có
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

        # Tạo figure và vẽ vertical bar chart
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(data["Datetime"], data["Revenue"], color='skyblue')
        ax.set_ylabel("Revenue (VND)")
        ax.set_title("Movie Revenue")
        plt.xticks(rotation=45)  # Xoay nhãn trục x cho dễ đọc

        # Tạo canvas từ figure và thêm vào layout
        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)
        canvas.draw()

    def draw_food_chart(self, data=None):
        if data is None:
            data = self.food_data


        layout = self.frameChartFood.layout()
        if layout is None:
            layout = QtWidgets.QVBoxLayout(self.frameChartFood)
        else:
            # Xóa hết các widget cũ nếu có
            while layout.count():
                child = layout.takeAt(0)
                if child.widget():
                    child.widget().deleteLater()

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.bar(data["Datetime"], data["Revenue"], color='lightgreen')
        ax.set_ylabel("Revenue (VND)")
        ax.set_title("Food Revenue")
        plt.xticks(rotation=45)  # Xoay nhãn trục x cho dễ đọc

        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)
        canvas.draw()



