import json
import os
from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.QtGui import QPixmap
from ui.admin.MovieCreate import Ui_Dialog  # Import giao diện từ file MovieCreate.py
from utils import resources_banner_rc
from utils import resources_poster_rc
from utils import resources_rc
from utils import resources_logo_rc


class MovieCreateExt(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.json_file_path = "../dataset/film.json"

        # Kết nối nút Save với hàm lưu phim mới
        self.ui.pushButtonSave.clicked.connect(self.save_movie_data)

    def save_movie_data(self):
        """ Lưu dữ liệu phim mới """
        new_movie = {
            "filmTitle": self.ui.lineEditTitle.text().strip(),
            "Author": self.ui.lineEditAuthor.text(),
            "Gerne": self.ui.lineEditGenre.text(),
            "Country": self.ui.lineEditCountry.text(),
            "Duration": self.ui.lineEditDuration.text(),
            "ReleaseDate": self.ui.lineEditYear.text(),
            "Description": self.ui.textEditDescription.toPlainText(),
            "image": "default.jpg"  # Có thể thêm chức năng chọn ảnh sau
        }

        try:
            with open(self.json_file_path, "r", encoding="utf-8") as file:
                films = json.load(file)

            films.append(new_movie)  # Thêm phim mới vào danh sách

            with open(self.json_file_path, "w", encoding="utf-8") as file:
                json.dump(films, file, indent=4, ensure_ascii=False)

            QMessageBox.information(self, "Thêm thành công", "Phim mới đã được thêm vào danh sách!")
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi lưu dữ liệu: {str(e)}")
