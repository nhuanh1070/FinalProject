import json
import os
import shutil
from PyQt6.QtWidgets import QDialog, QMessageBox, QFileDialog
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
        self.image_folder = "../images/Poster/"

        if not os.path.exists(self.image_folder):
            os.makedirs(self.image_folder)

        self.selected_image = "default.jpg"

        # Kết nối sự kiện cho nút
        self.ui.pushButtonSave.clicked.connect(self.save_movie_data)
        self.ui.pushButton_AddPoster.clicked.connect(self.choose_image)

    def choose_image(self):
        """ Mở File Explorer và cho phép người dùng chọn ảnh từ thư mục Poster """
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Chọn ảnh", self.image_folder, "Hình ảnh (*.png *.jpg *.jpeg)"
        )

        if file_path:  # Nếu người dùng chọn ảnh
            image_name = os.path.basename(file_path)  # Lấy tên file ảnh
            new_image_path = os.path.join(self.image_folder, image_name)

            # Nếu ảnh không nằm trong thư mục Poster thì copy vào
            if not file_path.startswith(self.image_folder):
                shutil.copy(file_path, new_image_path)

            self.selected_image = image_name  # Lưu ảnh đã chọn
            self.ui.labelImage.setPixmap(QPixmap(new_image_path).scaled(200, 300))  # Hiển thị ảnh xem trước

    def save_movie_data(self):
        """ Lưu dữ liệu phim mới """
        new_title = self.ui.lineEditTitle.text().strip()

        if not new_title:  # Kiểm tra nếu tiêu đề trống
            QMessageBox.warning(self, "Lỗi", "Tiêu đề phim không được để trống!")
            return

        new_movie = {
            "filmTitle": new_title,
            "Author": self.ui.lineEditAuthor.text(),
            "Gerne": self.ui.lineEditGenre.text(),
            "Country": self.ui.lineEditCountry.text(),
            "Duration": self.ui.lineEditDuration.text(),
            "ReleaseDate": self.ui.lineEditYear.text(),
            "Description": self.ui.textEditDescription.toPlainText(),
            "image": self.selected_image  # Ảnh đã chọn hoặc mặc định
        }

        try:
            # Đọc dữ liệu hiện có từ file JSON
            if os.path.exists(self.json_file_path):
                with open(self.json_file_path, "r", encoding="utf-8") as file:
                    films = json.load(file)
            else:
                films = []

            # Kiểm tra phim trùng tên
            for film in films:
                if film["filmTitle"].lower() == new_movie["filmTitle"].lower():
                    QMessageBox.warning(self, "Lỗi", "Phim này đã tồn tại trong danh sách!")
                    return

            films.append(new_movie)  # Thêm phim mới vào danh sách

            # Ghi lại vào file JSON
            with open(self.json_file_path, "w", encoding="utf-8") as file:
                json.dump(films, file, indent=4, ensure_ascii=False)

            QMessageBox.information(self, "Thành công", "Phim mới đã được thêm vào danh sách!")
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi lưu dữ liệu: {str(e)}")
