import json
import os
from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.QtGui import QPixmap
from ui.admin.MovieEdit import Ui_Dialog
from utils import resources_banner_rc
from utils import resources_poster_rc
from utils import resources_rc
from utils import resources_logo_rc


class MovieEditExt(QDialog):
    def __init__(self, movie, movies, parent=None):
        """
        movie: Dictionary chứa thông tin phim cần chỉnh sửa.
        movies: Danh sách tất cả các phim (list chứa nhiều dictionary).
        """
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.movie = movie
        self.movies = movies
        self.json_file_path = "../dataset/film.json"  # Đường dẫn file JSON

        if self.movie:
            self.load_movie_data()

        self.ui.pushButtonSave.clicked.connect(self.save_movie_data)

    def load_movie_data(self):
        """ Load dữ liệu phim vào các ô nhập """
        self.ui.lineEditTitle.setText(self.movie.get("filmTitle", ""))
        self.ui.lineEditAuthor.setText(self.movie.get("Author", ""))
        self.ui.lineEditGenre.setText(self.movie.get("Gerne", ""))
        self.ui.lineEditCountry.setText(self.movie.get("Country", ""))
        self.ui.lineEditDuration.setText(str(self.movie.get("Duration", "")))
        self.ui.lineEditYear.setText(self.movie.get("ReleaseDate", ""))
        self.ui.textEditDescription.setText(self.movie.get("Description", ""))

        # Hiển thị hình ảnh nếu có
        image_filename = self.movie.get("image", "default.jpg")
        image_full_path = os.path.join("../images/Poster/", image_filename)

        if os.path.exists(image_full_path):  # Kiểm tra nếu ảnh tồn tại
            pixmap = QPixmap(image_full_path)
            self.ui.labelImage.setPixmap(pixmap.scaled(200, 300))

    def save_movie_data(self):
        """ Lưu dữ liệu chỉnh sửa vào JSON trong đường dẫn ../dataset/film.json """
        self.movie["filmTitle"] = self.ui.lineEditTitle.text()
        self.movie["Author"] = self.ui.lineEditAuthor.text()
        self.movie["Gerne"] = self.ui.lineEditGenre.text()
        self.movie["Country"] = self.ui.lineEditCountry.text()
        self.movie["Duration"] = self.ui.lineEditDuration.text()
        self.movie["ReleaseDate"] = self.ui.lineEditYear.text()
        self.movie["Description"] = self.ui.textEditDescription.toPlainText()

        # Cập nhật danh sách phim
        for index, m in enumerate(self.movies):
            if m["filmTitle"] == self.movie["filmTitle"]:  # So sánh bằng tên phim
                self.movies[index] = self.movie
                break

        # Ghi lại vào file JSON ../dataset/film.json
        try:
            with open(self.json_file_path, "w", encoding="utf-8") as json_file:
                json.dump(self.movies, json_file, ensure_ascii=False, indent=4)
            QMessageBox.information(self, "Lưu thành công", "Thông tin phim đã được cập nhật!")
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi lưu dữ liệu: {str(e)}")
