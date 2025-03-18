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
        self.ui.lineEditDuration.setText(movie["Duration"])
        self.ui.lineEditYear.setText(movie["ReleaseDate"])
        self.ui.textEditDescription.setText(movie["Description"])

        # Hiển thị hình ảnh phim
        pixmap = QPixmap(movie["image"])
        self.ui.labelImage.setPixmap(pixmap.scaled(150, 200))