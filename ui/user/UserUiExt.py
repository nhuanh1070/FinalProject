import json
import os


from PyQt6.QtWidgets import QMainWindow, QMessageBox


from CSDL.libs.DataConnector import DataConnector
from ui.user.BookTicketExt import BookTicketExt
from ui.user.UserInforExt import UserInforExt
from ui.user.UserUi import Ui_MainWindow
from ui.user.ViewDetailExt import ViewDetailExt


from utils import resources_banner_rc
from utils import resources_poster_rc
from utils import resources_rc
from utils import resources_logo_rc




class UserUiExt(Ui_MainWindow):
   def __init__(self):
       self.MainWindow = QMainWindow()
       self.setupUi(self.MainWindow)
       self.movie_data = self.get_movie_data()
   def setupUi(self, MainWindow):
       super().setupUi(MainWindow)
       self.MainWindow = MainWindow
       self.MainWindow.ui = self
       # Gán sự kiện click cho các nút chuyển trang


       self.setupSignalAndSlot()


   def showWindow(self):
       self.MainWindow.show()
   def setupSignalAndSlot(self):
       # Sự kiện nút bấm chuyển trang
       self.pushButton_Right.clicked.connect(self.nextPage)
       self.pushButton_Left.clicked.connect(self.prevPage)
       self.Account_btn.clicked.connect(self.showUserInfo)
       # Kết nối các nút View Details với phim tương ứng
       self.btn_ViewDetails_1.clicked.connect(lambda: self.showMovieDetail(0))
       self.btn_ViewDetails_7.clicked.connect(lambda: self.showMovieDetail(1))
       self.btn_ViewDetails_8.clicked.connect(lambda: self.showMovieDetail(2))
       self.btn_ViewDetails_12.clicked.connect(lambda: self.showMovieDetail(3))
       self.btn_ViewDetails_11.clicked.connect(lambda: self.showMovieDetail(4))
       self.btn_ViewDetails_10.clicked.connect(lambda: self.showMovieDetail(5))
       """Gán sự kiện cho các nút"""
       self.btn_BookTicket_1.clicked.connect(lambda: self.bookTicket(0))
       self.btn_BookTicket_5.clicked.connect(lambda: self.bookTicket(1))
       self.btn_BookTicket_7.clicked.connect(lambda: self.bookTicket(2))
       self.btn_BookTicket_11.clicked.connect(lambda: self.bookTicket(3))
       self.btn_BookTicket_10.clicked.connect(lambda: self.bookTicket(4))
       self.btn_BookTicket_9.clicked.connect(lambda: self.bookTicket(5))


   def bookTicket(self, movie_index):
       """Mở giao diện đặt vé"""
       try:
           movie = self.movie_data[movie_index]
           self.MainWindow.close()
           username = self.get_logged_in_user()
           book_ticket_dialog = BookTicketExt(movie, username=username)
           book_ticket_dialog.exec()
       except IndexError:
           print(f"LỖI: Không tìm thấy phim với index {movie_index}!")
       except Exception as e:
           print(f"LỖI: Không thể mở giao diện BookTicket! {e}")
   def nextPage(self):
       current_index = self.stackedWidget.currentIndex()
       next_index = (current_index + 1) % self.stackedWidget.count()
       self.stackedWidget.setCurrentIndex(next_index)


   def prevPage(self):
       current_index = self.stackedWidget.currentIndex()
       prev_index = (current_index - 1) % self.stackedWidget.count()
       self.stackedWidget.setCurrentIndex(prev_index)
   def showMovieDetail(self, movie_index):
       movie = self.movie_data[movie_index]
       detail_dialog = ViewDetailExt(movie)
       detail_dialog.exec()


   def showUserInfo(self):
       """ Mở giao diện UserInforExt với thông tin user đang đăng nhập """
       print("📌 Debug - Đang mở UserInforExt từ UserUiExt...")


       # Lấy username từ file tạm
       current_username = self.get_logged_in_user()


       if not current_username:
           print("❌ LỖI: Không tìm thấy user đang đăng nhập!")
           QMessageBox.warning(self.MainWindow, "Lỗi", "Không tìm thấy thông tin tài khoản!")
           return


       print(f"✅ Debug - Username đang đăng nhập: {current_username}")


       # Lấy thông tin user từ file JSON
       dc = DataConnector()
       users = dc.get_all_users()
       user_info = next((user for user in users if user["Username"] == current_username), None)


       if not user_info:
           print(f"❌ LỖI: Không tìm thấy user {current_username} trong JSON!")
           QMessageBox.warning(self.MainWindow, "Lỗi", "Tài khoản không tồn tại trong hệ thống!")
           return


       print(f"✅ Debug - Thông tin user đang đăng nhập: {user_info}")


       # Mở cửa sổ UserInforExt và truyền `self.MainWindow` làm parent
       self.user_info_dialog = UserInforExt(user_info=user_info, parent=self.MainWindow)
       self.user_info_dialog.exec()


   def get_movie_data(self):
       # Danh sách dữ liệu phim
       return [
           {
               "filmTitle": "AVATAR: THE WAY OF WATER",
               "room":"Room 1",
               "Showtimes":"18:30",
               "Gerne": "Fiction",
               "Duration": "192'",
               "Language": "English",
               "Rating": "T13",
               "Poster": ":/Poster/images/Poster/Avatar.jpg",
               "Description": "Jake Sully và gia đình anh phải rời bỏ quê hương và tìm đến một bộ tộc sống dưới nước. Họ học cách sinh tồn và thích nghi với môi trường mới, nhưng nguy hiểm vẫn luôn rình rập. Kẻ thù cũ của họ quay trở lại với những âm mưu tàn bạo hơn. Phim mang đến hình ảnh mãn nhãn về thế giới Pandora với kỹ xảo tiên tiến. Đây là một cuộc phiêu lưu đầy cảm xúc về gia đình, lòng trung thành và bảo vệ thiên nhiên."
           },
           {
               "filmTitle": "DUNE PART TWO",
               "room": "Room 2",
               "Showtimes": "21:00",
               "Gerne": "Action",
               "Duration": "165'",
               "Language": "English",
               "Rating": "T16",
               "Poster": ":/Poster/images/Poster/Dune.jpg",
               "Description": "Paul Atreides tiếp tục hành trình của mình để giành lại công lý cho gia đình và bảo vệ hành tinh Arrakis. Khi gia nhập tộc người Fremen, anh phải đối mặt với những thách thức khắc nghiệt của sa mạc và những kẻ thù mạnh mẽ. Tình yêu, lòng trung thành và trách nhiệm trở thành những yếu tố quan trọng trong cuộc chiến này. Bộ phim mang đến những cảnh quay hoành tráng, kết hợp với âm nhạc và hình ảnh mãn nhãn. Đây là phần phim đầy hấp dẫn, tiếp tục mở rộng thế giới Dune kỳ vĩ."
           },
           {
               "filmTitle": "FAST X",
               "room": "Room 3",
               "Showtimes": "16:00",
               "Gerne": "Action",
               "Duration": "141'",
               "Language": "English",
               "Rating": "T13",
               "Poster": ":/Poster/images/Poster/FastX.jpg",
               "Description": "Dominic Toretto và gia đình của anh phải đối mặt với một kẻ thù mới từ quá khứ, kẻ mang trong mình mối hận thù sâu sắc. Những cuộc rượt đuổi tốc độ cao, các vụ nổ hoành tráng và những pha hành động mạo hiểm tiếp tục đẩy loạt phim Fast & Furious lên một tầm cao mới. Bộ phim không chỉ mang đến những pha hành động mãn nhãn mà còn khai thác sâu hơn về tình cảm gia đình và sự trung thành. Những nhân vật cũ trở lại và nhiều bí ẩn mới được tiết lộ, làm tăng thêm kịch tính cho phần phim này. Fast X là một phần quan trọng trong loạt phim, hứa hẹn sẽ mở ra những hướng đi mới đầy bất ngờ."
           },
           {
               "filmTitle": "JOHN WICK 4",
               "room": "Room 4",
               "Showtimes": "20:00",
               "Gerne": "Action",
               "Duration": "169'",
               "Language": "English",
               "Rating": "T18",
               "Poster": ":/Poster/images/Poster/JohnWick.jpg",
               "Description": "John Wick tiếp tục bị thế giới sát thủ truy đuổi và lần này, kẻ thù của anh mạnh mẽ hơn bao giờ hết. Anh phải tìm kiếm đồng minh và lập kế hoạch để đối đầu với những tổ chức quyền lực. Những pha hành động mãn nhãn, các trận đấu căng thẳng và những âm mưu đen tối khiến bộ phim đầy cuốn hút. Sự pha trộn giữa bạo lực, chiến thuật và cảm xúc giúp John Wick 4 trở thành phần phim không thể bỏ lỡ. Liệu anh có thể giành lại tự do hay bị cuốn mãi vào vòng xoáy bạo lực?"
           },
           {
               "filmTitle": "SPIDERMAN",
               "room": "Room 5",
               "Showtimes": "20:00",
               "Gerne": "Adventure",
               "Duration": "133'",
               "Language": "English",
               "Rating": "PG-13",
               "Poster": ":/Poster/images/Poster/Spiderman.jpg",
               "Description": "Peter Parker vô tình mở ra cánh cổng đa vũ trụ khi nhờ Doctor Strange giúp đỡ. Điều này dẫn đến sự xuất hiện của các phản diện từ những vũ trụ khác nhau. Cậu buộc phải chiến đấu để bảo vệ thế giới, đồng thời học cách chấp nhận hậu quả của quyết định mình. Bộ phim mang đến sự kết hợp giữa hành động, hài hước và những khoảnh khắc xúc động. Cao trào của phim là sự hội tụ của nhiều phiên bản Spider-Man, làm hài lòng người hâm mộ."
           },
           {
               "filmTitle": "THE CONJURING",
               "room": "Room 6",
               "Showtimes": "22:00",
               "Gerne": "Horror",
               "Duration": "112'",
               "Language": "English",
               "Rating": "T18",
               "Poster": ":/Poster/images/Poster/TheConjuring.jpg",
               "Description": "Ed và Lorraine Warren điều tra một vụ án giết người liên quan đến hiện tượng quỷ ám đáng sợ. Lần đầu tiên trong lịch sử, một kẻ sát nhân tuyên bố rằng hắn bị quỷ điều khiển để gây án. Những hiện tượng siêu nhiên ngày càng ám ảnh và nguy hiểm hơn bao giờ hết. Bộ phim mang đến những pha hù dọa căng thẳng cùng bầu không khí rùng rợn đặc trưng. Đây là một trong những phần đáng sợ nhất của vũ trụ Conjuring, khiến khán giả thót tim đến giây cuối cùng."
           }
       ]


   def get_logged_in_user(self):
       """ Trả về username của user đang đăng nhập từ dataset/current_user.json """
       try:
           dataset_path = os.path.join(os.path.dirname(__file__), "../dataset")
           current_user_path = os.path.join(dataset_path, "current_user.json")


           with open(current_user_path, "r", encoding="utf-8") as f:
               data = json.load(f)
               return data.get("Username", None)
       except Exception as e:
           print(f"❌ LỖI: Không thể đọc file current_user.json - {e}")
           return None





