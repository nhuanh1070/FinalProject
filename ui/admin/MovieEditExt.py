from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.QtGui import QPixmap
from ui.admin.MovieEdit import Ui_Dialog
from utils import resources_banner_rc
from utils import resources_poster_rc
from utils import resources_rc
from utils import resources_logo_rc
class MovieEditExt(QDialog):
    def __init__(self, movie, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.movie = movie  # Lưu thông tin phim để chỉnh sửa

        if self.movie:
            self.load_movie_data()

        # Kết nối nút Save với hàm lưu
        self.ui.pushButtonSave.clicked.connect(self.save_movie_data)

    def load_movie_data(self):
        """ Load dữ liệu phim vào các ô nhập """
        self.ui.lineEditTitle.setText(self.movie["name"])
        self.ui.lineEditAuthor.setText(self.movie["author"])
        self.ui.lineEditGenre.setText(self.movie["genre"])
        self.ui.lineEditCountry.setText(self.movie["country"])
        self.ui.lineEditDuration.setText(self.movie["duration"])
        self.ui.lineEditYear.setText(self.movie["year"])
        self.ui.textEditDescription.setText(self.movie["description"])

        # Hiển thị hình ảnh nếu có
        pixmap = QPixmap(self.movie["image"])
        self.ui.labelImage.setPixmap(pixmap.scaled(150, 200))

    def save_movie_data(self):
        """ Lưu dữ liệu chỉnh sửa """
        self.movie["name"] = self.ui.lineEditTitle.text()
        self.movie["author"] = self.ui.lineEditAuthor.text()
        self.movie["genre"] = self.ui.lineEditGenre.text()
        self.movie["country"] = self.ui.lineEditCountry.text()
        self.movie["duration"] = self.ui.lineEditDuration.text()
        self.movie["year"] = self.ui.lineEditYear.text()
        self.movie["description"] = self.ui.textEditDescription.toPlainText()

        QMessageBox.information(self, "Lưu thành công", "Thông tin phim đã được cập nhật!")
        self.accept()