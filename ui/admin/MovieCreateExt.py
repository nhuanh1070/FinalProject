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

        # Kết nối nút Save với hàm lưu phim mới
        self.ui.pushButtonSave.clicked.connect(self.save_movie_data)

    def save_movie_data(self):
        """ Lưu dữ liệu phim mới """
        new_movie = {
            "name": self.ui.lineEditTitle.text(),
            "author": self.ui.lineEditAuthor.text(),
            "genre": self.ui.lineEditGenre.text(),
            "country": self.ui.lineEditCountry.text(),
            "duration": self.ui.lineEditDuration.text(),
            "year": self.ui.lineEditYear.text(),
            "description": self.ui.textEditDescription.toPlainText(),
            "image": "default.jpg"  # Có thể thêm chức năng chọn ảnh sau
        }

        QMessageBox.information(self, "Thêm thành công", "Phim mới đã được thêm vào danh sách!")
        self.accept()
