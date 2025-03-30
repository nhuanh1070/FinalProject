import os
import pandas as pd
from collections import Counter
import json
from PyQt6.QtWidgets import QDialog, QMessageBox
from ui.admin.Statistic import Ui_Dialog

class StatisticExt(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Đảm bảo sử dụng đường dẫn tuyệt đối cho các tệp
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        self.bills_path = os.path.join(base_dir, "dataset", "bills.json")
        self.excel_path = os.path.join(base_dir, "dataset", "data_doanhthuve.xlsx")

        # Đọc dữ liệu từ các tệp
        self.load_data()

    def load_data(self):
        # Đọc dữ liệu từ bills.json
        try:
            with open(self.bills_path, 'r', encoding='utf-8') as file:
                self.bills_data = json.load(file)
            # Gọi các hàm tính toán và hiển thị kết quả
            self.display_popular_seats()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while reading the bills data: {e}")

        # Đọc dữ liệu từ file Excel để tính toán các phim có số vé đặt nhiều nhất
        self.load_excel_data()

    def load_excel_data(self):
        try:
            # Đọc tệp Excel với Pandas
            df = pd.read_excel(self.excel_path)

            # Kiểm tra cấu trúc dữ liệu
            if 'Movie' not in df.columns or 'Number of tickets sold' not in df.columns:
                raise ValueError("Excel file does not contain 'Movie' or 'Number of tickets sold' columns.")

            # Tính toán tổng số vé đặt cho mỗi bộ phim
            top_movies = df.groupby('Movie')['Number of tickets sold'].sum().sort_values(ascending=False).head(10)

            # Hiển thị kết quả vào textEditTopMovies trong giao diện (Top Movies with Most Bookings)
            movie_info = "<br>".join([f"<b>{movie}</b> - {tickets} tickets" for movie, tickets in top_movies.items()])
            self.ui.textEditTopMovies.setText(movie_info)

            # Hiển thị kết quả vào textEditTop3Movies trong giao diện (Top 3 Movies with Most Bookings Since Release)
            top_3_movies = top_movies.head(3)
            top_3_movie_info = "<br>".join([f"<b>{movie}</b> - {tickets} tickets" for movie, tickets in top_3_movies.items()])
            self.ui.textEditTop3Movies.setText(top_3_movie_info)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred while reading the Excel data: {e}")

    # Hàm tính toán ghế phổ biến
    def get_popular_seats(self):
        seats = []
        for bill in self.bills_data:
            seats.extend(bill.get("seats", []))  # Thêm ghế từ mỗi bill vào danh sách

        seat_counts = Counter(seats)  # Đếm số lần mỗi ghế xuất hiện
        popular_seats = seat_counts.most_common(5)  # Lấy 5 ghế phổ biến nhất
        return popular_seats

    # Hàm hiển thị các ghế phổ biến lên giao diện
    def display_popular_seats(self):
        popular_seats = self.get_popular_seats()

        if not popular_seats:  # Kiểm tra nếu không có ghế phổ biến nào
            print("No popular seats found.")
            QMessageBox.warning(self, "Warning", "No popular seats found.")
        else:
            # Tạo chuỗi kết quả các ghế phổ biến cách nhau bởi dấu phẩy
            seat_info = ", ".join([seat for seat, count in popular_seats])

            # Hiển thị kết quả vào lineEditTopSeats trong giao diện
            self.ui.lineEditTopSeats.setText(seat_info)

