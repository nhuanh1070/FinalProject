from PyQt6.QtWidgets import QDialog
from PyQt6.QtGui import QPixmap
from ui.admin.MovieDetail import Ui_Dialog  # Import giao diện từ file MovieDetail.py

class MovieDetailExt(QDialog):
    def __init__(self, movie, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Hiển thị thông tin phim
        self.ui.lineEditTitle.setText(movie["name"])
        self.ui.lineEditAuthor.setText(movie["author"])
        self.ui.lineEditGenre.setText(movie["genre"])
        self.ui.lineEditCountry.setText(movie["country"])
        self.ui.lineEditDuration.setText(movie["duration"])
        self.ui.lineEditYear.setText(movie["year"])
        self.ui.textEditDescription.setText(movie["description"])

        # Hiển thị hình ảnh phim
        pixmap = QPixmap(movie["image"])
        self.ui.labelImage.setPixmap(pixmap.scaled(150, 200))