from PyQt6 import QtGui
from PyQt6.QtWidgets import QDialog
from ui.user.ViewDetail import Ui_Dialog
from utils import resources_banner_rc
from utils import resources_poster_rc
from utils import resources_rc
from utils import resources_logo_rc
class ViewDetailExt(QDialog):
    def __init__(self, movie, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setMovieDetails(movie)

    def setMovieDetails(self, movie):
        self.ui.label_title.setText(movie["title"])  # Tiêu đề phim
        self.ui.label_genre.setText(movie["genre"])  # Thể loại
        self.ui.label_duration.setText(movie["duration"])  # Thời lượng
        self.ui.label_language.setText(movie["language"])  # Ngôn ngữ
        self.ui.label_rating.setText(movie["rating"])  # Độ tuổi
        self.ui.label_poster.setPixmap(QtGui.QPixmap(movie["poster"]))  # Cập nhật poster
        self.ui.textEditMovieContent.setText(movie["description"])  # Mô tả phim