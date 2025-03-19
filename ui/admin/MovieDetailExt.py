import os

from PyQt6.QtWidgets import QDialog
from PyQt6.QtGui import QPixmap
from ui.admin.MovieDetail import Ui_Dialog  # Import giao diện từ file MovieDetail.py
from utils import resources_banner_rc
from utils import resources_poster_rc
from utils import resources_rc
from utils import resources_logo_rc
class MovieDetailExt(QDialog):
    def __init__(self, movie, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Hiển thị thông tin phim
        self.ui.lineEditTitle.setText(movie["filmTitle"])
        self.ui.lineEditAuthor.setText(movie["Author"])
        self.ui.lineEditGenre.setText(movie["Gerne"])
        self.ui.lineEditCountry.setText(movie["Country"])
        self.ui.lineEditDuration.setText(str(movie["Duration"]))
        self.ui.lineEditYear.setText(movie["ReleaseDate"])
        self.ui.textEditDescription.setText(movie["Description"])

        # Hiển thị hình ảnh phim
        image_filename = movie.get("image", "default.jpg")  # Lấy tên file ảnh từ JSON
        image_full_path = os.path.join("../images/Poster/", image_filename)  # Tạo đường dẫn đầy đủ

        # Load ảnh bằng QPixmap và hiển thị
        pixmap = QPixmap(image_full_path)
        self.ui.labelImage.setPixmap(pixmap.scaled(200, 300))

