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

        self.ui.lineEditTitle.setText(movie["filmTitle"])
        self.ui.lineEditAuthor.setText(movie["Author"])
        self.ui.lineEditGenre.setText(movie["Gerne"])
        self.ui.lineEditCountry.setText(movie["Country"])
        self.ui.lineEditDuration.setText(str(movie["Duration"]))
        self.ui.lineEditYear.setText(movie["ReleaseDate"])
        self.ui.textEditDescription.setText(movie["Description"])

        self.ui.lineEditTitle.setReadOnly(True)
        self.ui.lineEditAuthor.setReadOnly(True)
        self.ui.lineEditGenre.setReadOnly(True)
        self.ui.lineEditCountry.setReadOnly(True)
        self.ui.lineEditDuration.setReadOnly(True)
        self.ui.lineEditYear.setReadOnly(True)
        self.ui.textEditDescription.setReadOnly(True)

        image_filename = movie.get("image", "default.jpg")
        image_full_path = os.path.join("../images/Poster/", image_filename)
        pixmap = QPixmap(image_full_path)
        self.ui.labelImage.setPixmap(pixmap.scaled(200, 300))
