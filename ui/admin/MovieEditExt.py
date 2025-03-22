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

        # Khóa ô nhập tiêu đề phim để tránh thay đổi
        self.ui.lineEditTitle.setReadOnly(True)

        # Hiển thị hình ảnh nếu có
        image_filename = self.movie.get("image", "default.jpg")
        image_full_path = os.path.join("../images/Poster/", image_filename)

        if os.path.exists(image_full_path):  # Kiểm tra nếu ảnh tồn tại
            pixmap = QPixmap(image_full_path)
            self.ui.labelImage.setPixmap(pixmap.scaled(200, 300))

    def save_movie_data(self):
        """ Lưu dữ liệu chỉnh sửa vào JSON trong đường dẫn ../dataset/film.json """
        old_title = self.movie["filmTitle"]  # Tiêu đề phim cũ
        new_title = self.ui.lineEditTitle.text().strip()

        # Kiểm tra nếu người dùng cố gắng đổi tên phim
        if old_title != new_title:
            QMessageBox.warning(
                self, "Cảnh báo",
                "Bạn không được phép đổi tên phim! Tên sẽ được giữ nguyên.",
                QMessageBox.StandardButton.Ok
            )
            self.ui.lineEditTitle.setText(old_title)  # Khôi phục tên cũ
            return  # Không tiếp tục lưu nếu tên bị thay đổi

        # Cập nhật thông tin khác của phim
        updated_movie = {
            "filmTitle": old_title,  # Luôn giữ tiêu đề cũ
            "Author": self.ui.lineEditAuthor.text(),
            "Gerne": self.ui.lineEditGenre.text(),
            "Country": self.ui.lineEditCountry.text(),
            "Duration": self.ui.lineEditDuration.text(),
            "ReleaseDate": self.ui.lineEditYear.text(),
            "Description": self.ui.textEditDescription.toPlainText()
        }

        # Cập nhật dữ liệu trong file JSON
        if self.update_film_info(old_title, updated_movie):
            QMessageBox.information(self, "Lưu thành công", "Thông tin phim đã được cập nhật!")
            self.refresh_movie_data()  # Cập nhật lại thông tin hiển thị từ file JSON
            self.accept()
        else:
            QMessageBox.critical(self, "Lỗi", "Lỗi khi cập nhật dữ liệu!")

    def update_film_info(self, old_title, updated_movie):
        """ Hàm cập nhật thông tin phim trong file JSON """
        try:
            # Đọc dữ liệu hiện có từ file JSON
            with open(self.json_file_path, "r", encoding="utf-8") as file:
                films = json.load(file)

            # Tìm và cập nhật phim trong danh sách
            for film in films:
                if film["filmTitle"] == old_title:
                    film.update(updated_movie)
                    break
            else:
                return False  # Không tìm thấy phim

            # Ghi lại vào file JSON
            with open(self.json_file_path, "w", encoding="utf-8") as file:
                json.dump(films, file, indent=4, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"❌ Lỗi cập nhật film.json: {e}")
            return False

    def refresh_movie_data(self):
        """ Cập nhật lại thông tin hiển thị từ file JSON """
        try:
            with open(self.json_file_path, "r", encoding="utf-8") as file:
                films = json.load(file)

            # Lấy dữ liệu phim mới nhất theo tiêu đề cũ
            for film in films:
                if film["filmTitle"] == self.movie["filmTitle"]:
                    self.movie = film
                    self.load_movie_data()  # Cập nhật lại giao diện
                    break
        except Exception as e:
            print(f"❌ Lỗi cập nhật dữ liệu hiển thị: {e}")
