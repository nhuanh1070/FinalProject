
import json
import os
from datetime import datetime

import pandas as pd

from PyQt6.QtWidgets import QMessageBox, QMainWindow, QTableWidgetItem
from PyQt6 import QtWidgets, QtCore
from PyQt6 import QtGui
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from CSDL.libs.DataConnector import DataConnector
from CSDL.libs.JsonFileFactory import JsonFileFactory
from CSDL.models.Film import Film
from ui.admin.AdminUi import Ui_MainWindow
from ui.admin.ExportExt import ExportExt
from ui.admin.MovieDetailExt import MovieDetailExt
from ui.admin.MovieCreateExt import MovieCreateExt
from ui.admin.MovieEditExt import MovieEditExt
from ui.admin.StatisticExt import StatisticExt
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
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)
        self.tableWidget.itemSelectionChanged.connect(self.highlight_selected_rows)

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
        self.btnExportFile.clicked.connect(self.show_export_window)
        self.btnStatistic.clicked.connect(self.show_report_window)
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
        self.filtered_movies = movie_list.copy()
        self.tableWidget.setRowCount(len(movie_list))
        for row, movie in enumerate(movie_list):
            columns = [
                movie["filmTitle"],
                movie["Gerne"],
                movie["Country"],
                movie["ReleaseDate"],
                str(movie["Duration"])
            ]
            for col, value in enumerate(columns):
                item = QTableWidgetItem(value)
                item.setFlags(item.flags() & ~QtCore.Qt.ItemFlag.ItemIsEditable)  # Khoá ô không cho sửa
                self.tableWidget.setItem(row, col, item)
        self.highlight_selected_rows()

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
        selected_rows = list(set(index.row() for index in self.tableWidget.selectedIndexes()))
        if not selected_rows:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng chọn ít nhất một bộ phim để xoá!")
            return

        titles_to_delete = [self.filtered_movies[row]["filmTitle"] for row in selected_rows]
        confirm_text = "\n".join(titles_to_delete)

        dlg = QMessageBox(self.MainWindow)
        dlg.setWindowTitle("Xác nhận xoá")
        dlg.setText(f"Bạn có chắc muốn xoá các phim sau không?\n\n{confirm_text}")
        dlg.setIcon(QMessageBox.Icon.Question)
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

        if dlg.exec() == QMessageBox.StandardButton.No:
            return

        try:
            file_path = "../dataset/film.json"
            with open(file_path, "r", encoding="utf-8") as file:
                films = json.load(file)

            updated_films = [film for film in films if film["filmTitle"] not in titles_to_delete]

            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(updated_films, file, indent=4, ensure_ascii=False)

            QMessageBox.information(self.MainWindow, "Thành công", f"Đã xoá {len(titles_to_delete)} phim.")
            self.movies = updated_films
            self.load_all_movies()

            # Deselect all rows before highlighting them again
            self.tableWidget.clearSelection()  # Bỏ chọn tất cả các dòng
            self.highlight_selected_rows()  # Tắt highlight
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Lỗi khi xoá phim: {str(e)}")

    def highlight_selected_rows(self):
        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                if item:
                    item.setBackground(QtGui.QColor("white"))
                    item.setForeground(QtGui.QBrush(QtGui.QColor("black")))

        for index in self.tableWidget.selectionModel().selectedRows():
            row = index.row()
            for col in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, col)
                if item:
                    item.setBackground(QtGui.QColor("#fff3cd"))
                    if col == 0:
                        item.setForeground(QtGui.QBrush(QtGui.QColor("red")))  # Tên phim tô đỏ
                    else:
                        item.setForeground(QtGui.QBrush(QtGui.QColor("black")))

    def load_revenue_data(self):
        try:
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
            movie_file = os.path.join(base_dir, "dataset", "data_doanhthuve.xlsx")
            food_file = os.path.join(base_dir, "dataset", "data_doanhthubapnuoc.xlsx")

            if not os.path.exists(movie_file) or not os.path.exists(food_file):
                QMessageBox.critical(self.MainWindow, "Lỗi", "Không tìm thấy file dữ liệu doanh thu!")
                return


            self.movie_data = pd.read_excel(movie_file, engine="openpyxl")
            self.food_data = pd.read_excel(food_file, engine="openpyxl")


            self.movie_data["Revenue"] = pd.to_numeric(self.movie_data["Revenue"], errors="coerce").fillna(0)
            self.food_data["Revenue"] = pd.to_numeric(self.food_data["Revenue"], errors="coerce").fillna(0)

            if "Datetime" not in self.movie_data.columns or "Datetime" not in self.food_data.columns:
                QMessageBox.critical(self.MainWindow, "Lỗi",
                                     "File Excel không có cột 'Datetime'. Kiểm tra lại dữ liệu!")
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
        start_str = f"{start_month[:4]}-{start_month[5:]}"  # "YYYY-MM"
        end_str = f"{end_month[:4]}-{end_month[5:]}"  # "YYYY-MM"
        if not start_month or not end_month:
            QMessageBox.warning(self.MainWindow, "Lỗi", "Vui lòng chọn tháng bắt đầu và tháng kết thúc để lọc!")
            return

        try:
            # Chuyển chuỗi tháng/năm (YYYY-MM) thành datetime object
            start_date = datetime.strptime(start_month, "%Y-%m")
            end_date = datetime.strptime(end_month, "%Y-%m")

            if end_date < start_date:
                QMessageBox.warning(self.MainWindow, "Lỗi", "Tháng kết thúc phải lớn hơn hoặc bằng tháng bắt đầu!")
                return

            # Lọc các tháng có dữ liệu trong file Excel
            movie_months = set(self.movie_data["Datetime"].unique())  # Các tháng có trong dữ liệu phim
            food_months = set(self.food_data["Datetime"].unique())  # Các tháng có trong dữ liệu thực phẩm

            # Tạo một tập hợp các tháng từ dữ liệu
            all_months_in_data = movie_months.union(food_months)

            # Lọc các tháng nằm trong khoảng từ start_str đến end_str và có trong dữ liệu
            valid_months = [month for month in all_months_in_data
                            if start_date <= datetime.strptime(month, "%Y-%m") <= end_date]


        except ValueError as e:
            QMessageBox.warning(self.MainWindow, "Lỗi", f"Định dạng tháng/năm không đúng: {e}")
            return

        # Lọc dữ liệu theo thời gian
        filtered_movies = self.movie_data[
            (self.movie_data["Datetime"] >= start_str) & (self.movie_data["Datetime"] <= end_str)]
        filtered_foods = self.food_data[
            (self.food_data["Datetime"] >= start_str) & (self.food_data["Datetime"] <= end_str)]

        if filtered_movies.empty and filtered_foods.empty:
            QMessageBox.warning(self.MainWindow, "Thông báo", "Không có dữ liệu cho khoảng thời gian đã chọn!")
            return

        # Cập nhật bảng với dữ liệu đã lọc
        self.populate_table(filtered_movies, self.tableMovies)
        self.populate_table(filtered_foods, self.tableFoods)

        # Cập nhật doanh thu tổng
        self.calculate_total_revenue(filtered_movies, filtered_foods)

        # Vẽ lại biểu đồ với dữ liệu đã lọc
        self.draw_movie_chart(filtered_movies)
        self.draw_food_chart(filtered_foods)

    def populate_table(self, data, table_widget):

        # Xóa nội dung hiện tại trong bảng
        table_widget.clearContents()

        # Đặt số cột dựa trên số cột của DataFrame
        table_widget.setColumnCount(len(data.columns))
        table_widget.setHorizontalHeaderLabels(data.columns.tolist())

        # Thêm dữ liệu vào bảng
        for row_idx, (index, row) in enumerate(data.iterrows()):
            # Dòng đầu tiên bắt đầu từ row_idx == 0
            table_widget.insertRow(row_idx)  # Thêm hàng mới
            for col_idx, value in enumerate(row):
                item = QTableWidgetItem(str(value))  # Chuyển giá trị thành chuỗi
                table_widget.setItem(row_idx, col_idx, item)  # Thêm giá trị vào ô tương ứng

        # Làm mới giao diện bảng
        table_widget.repaint()
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
        plt.xticks(rotation=15)

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
        plt.xticks(rotation=15)

        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)
        canvas.draw()
    def show_export_window(self):
        dialog = ExportExt(self.MainWindow)
        dialog.exec()

    def show_report_window(self):
        try:
            dialog = StatisticExt(self.MainWindow)
            dialog.exec()
        except Exception as e:
            QMessageBox.critical(self.MainWindow, "Lỗi", f"Có lỗi xảy ra khi mở báo cáo: {str(e)}")


