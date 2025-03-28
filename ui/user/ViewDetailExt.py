from PyQt6 import QtGui
from PyQt6.QtWidgets import QDialog

from CSDL.test.TestDataConnector import username
from ui.user.BookTicketExt import BookTicketExt
from ui.user.ViewDetail import Ui_Dialog
from utils import resources_banner_rc
from utils import resources_poster_rc
from utils import resources_rc


class ViewDetailExt(QDialog):
   def __init__(self, movie, parent=None):
       super().__init__(parent)
       self.ui = Ui_Dialog()
       self.ui.setupUi(self)
       self.username=username
       self.setMovieDetails(movie)

       # Kết nối nút "Buy Ticket" với hàm mở giao diện đặt vé
       self.ui.pushButtonBuyTickets.clicked.connect(lambda: self.bookTicket(movie))


   def setMovieDetails(self, movie):
       self.ui.label_title.setText(movie["filmTitle"])  # Tiêu đề phim
       self.ui.label_genre.setText(movie["Gerne"])  # Thể loại
       self.ui.label_duration.setText(movie["Duration"])  # Thời lượng
       self.ui.label_language.setText(movie["Language"])  # Ngôn ngữ
       self.ui.label_rating.setText(movie["Rating"])  # Độ tuổi
       self.ui.label_poster.setPixmap(QtGui.QPixmap(movie["Poster"]))

       self.ui.textEditMovieContent.setText(movie["Description"])  # Mô tả phim
       self.ui.textEditMovieContent.setReadOnly(True)


   def bookTicket(self, movie):
       """Mở giao diện đặt vé khi bấm Buy Ticket"""
       self.close()  # Đóng giao diện ViewDetail hiện tại
       self.parent().close()
       self.book_ticket_dialog = BookTicketExt(movie, self.username)  # Truyền thông tin phim
       self.book_ticket_dialog.exec()


