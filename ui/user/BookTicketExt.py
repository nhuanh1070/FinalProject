import json
import os
from datetime import datetime


from PyQt6 import QtGui, QtCore
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QDialog, QMessageBox, QHBoxLayout, QWidget, QLabel, QSpinBox, QPushButton, QVBoxLayout, \
   QFrame

from CSDL.libs.DataConnector import DataConnector
from CSDL.libs.JsonFileFactory import JsonFileFactory
from CSDL.models.Bill import Bill
from CSDL.models.UserInfor import UserInfor
from ui.user.UserInforExt import UserInforExt
from utils import resources_rc
from utils import resources_food_rc
from ui.user.BookTicket import Ui_Dialog


class BookTicketExt(QDialog):
   def __init__(self, movie, username, parent=None):
       super().__init__(parent)
       self.MainWindow = self
       self.ui = Ui_Dialog()
       self.ui.setupUi(self)
       self.ui.stackedWidget.setCurrentWidget(self.ui.pageChonGhe)
       self.movie = movie  # Lưu thông tin phim
       self.username= username
       self.showUserInfo()
       self.selected_seats = set()
       self.ticket_price_per_seat = 50000


       self.ui.label_MovieName.setText(self.movie.get("filmTitle", ""))
       self.ui.label_Showtime.setText(self.movie.get("Showtimes", ""))
       self.ui.label_ScreenRoom.setText(self.movie.get("room", "Room ?"))


       image_filename = self.movie.get("image", "default.jpg")
       image_path = self.movie.get("Poster", ":/Poster/images/Poster/default.jpg")
       pixmap = QPixmap(image_path)
       self.ui.label.setPixmap(pixmap.scaled(185, 273))

       base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
       dataset_path = os.path.join(base_path, "dataset")
       if not os.path.exists(dataset_path):
           os.makedirs(dataset_path)

       self.current_user_path = os.path.join(dataset_path, "current_user.json")
       if not os.path.exists(self.current_user_path):
           QMessageBox.critical(self.MainWindow, "Lỗi", f"Không tìm thấy file: {self.current_user_path}")

       self.setupSignalAndSlot()
       self.selected_foods = []




   def setupSignalAndSlot(self):
       """Gán sự kiện cho các nút trong giao diện"""
       self.ui.pushButtonContinue.clicked.connect(self.goToProductCategory)
       self.ui.pushButton_Confirm.clicked.connect(self.goToHoaDon)
       self.ui.pushButtonPayment.clicked.connect(self.showSuccessMessage)


       self.ui.pushButtonBackHomePage.clicked.connect(self.backToHomePage)


       self.ui.pushButton_BackProductCatalog.clicked.connect(self.backToProductCatalog)
       self.ui.pushButton_BackChonGhe.clicked.connect(self.backToChonGhe)
       # Gán sự kiện cho các nút ghế và nút thêm sản phẩm
       self.setupSeatButtons()
       self.setupFoodButtons()


   def setupSeatButtons(self):
       """Gán sự kiện cho các nút ghế"""
       for i in range(2, 42):  # pushButton_2 đến pushButton_41
           button_name = f"pushButton_{i}"
           button = getattr(self.ui, button_name, None)
           if button:
               button.clicked.connect(lambda _, btn=button: self.toggleSeatSelection(btn))


   def setupFoodButtons(self):
       """Gán sự kiện cho các nút + để thêm sản phẩm"""
       for i in range(1, 10):
           button_name = f"pushButton_Plus_{i}"
           button = getattr(self.ui, button_name, None)
           if button:
               button.clicked.connect(lambda _, idx=i: self.addFoodToCheckout(idx))


   def backToHomePage(self):
       from ui.user.UserUiExt import UserUiExt
       self.close()  # Đóng cửa sổ hiện tại
       self.user_ui = UserUiExt()
       self.user_ui.showWindow()


   def goToProductCategory(self):
       self.ui.stackedWidget.setCurrentWidget(self.ui.page_ProductCatalog)


   def backToChonGhe(self):
       """Quay lại trang Chọn Ghế"""
       self.ui.stackedWidget.setCurrentWidget(self.ui.pageChonGhe)
   def toggleSeatSelection(self, button):
       """Xử lý đổi màu ghế khi được chọn hoặc bỏ chọn"""
       seat_number = button.text()
       seat_color = button.palette().color(button.backgroundRole()).name()


       if seat_color == "#d32f2f":  # Màu đỏ (đã có người đặt)
           msg_box = QMessageBox()
           msg_box.setIcon(QMessageBox.Icon.Warning)
           msg_box.setWindowTitle("Thông báo")
           msg_box.setText("Ghế này đã có người chọn. Vui lòng chọn ghế khác!")
           msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
           msg_box.exec()
           return


       if seat_number in self.selected_seats:
           # Bỏ chọn ghế
           button.setStyleSheet("background-color: rgb(224, 224, 224);")
           self.selected_seats.remove(seat_number)
       else:
           # Chọn ghế
           button.setStyleSheet("background-color: rgb(251, 190, 20);")
           self.selected_seats.add(seat_number)
       self.updateTotalTicketPrice()
       self.ui.label_Seats.setText(", ".join(sorted(self.selected_seats)))


   def updateTotalTicketPrice(self):
       total = len(self.selected_seats) * self.ticket_price_per_seat
       self.ui.label_TotalPriceTicket.setText(f"{total} VNĐ")
       self.ui.label_Price.setText(f"{total}")


   def addFoodToCheckout(self, index):
       """Thêm sản phẩm vào checkout hoặc cập nhật số lượng nếu đã có sẵn"""
       label_name = getattr(self.ui, f"label_NameProduct_{index}", None)
       label_price = getattr(self.ui, f"label_PriceProduct_{index}", None)
       if not label_name or not label_price:
           return


       product_name = label_name.text()
       product_price = label_price.text().replace("VNĐ", "").strip()
       # Kiểm tra xem sản phẩm đã có trong checkout chưa
       for i in range(self.ui.verticalLayout_Checkout.count()):
           widget = self.ui.verticalLayout_Checkout.itemAt(i).widget()
           existing_label = widget.findChild(QLabel, "label_NameProduct")
           if existing_label and existing_label.text() == product_name:
               quantity_label = widget.findChild(QLabel, "label_Quantity")
               price_label = widget.findChild(QLabel, "label_PriceFood")


               new_quantity = int(quantity_label.text()) + 1
               quantity_label.setText(str(new_quantity))


               # Cập nhật lại giá mới dựa trên số lượng
               new_price = int(product_price.replace("VNĐ", "").strip()) * new_quantity
               price_label.setText(f"{new_price} VNĐ")
               self.updateTotalPriceFood()
               return


       # Nếu chưa có thì tạo widget mới
       food_widget = QWidget()
       food_widget.setObjectName("widget_FoodCheckout")
       food_widget.setFixedSize(221, 82)
       food_widget.setStyleSheet("background-color: rgb(243, 246, 250); border-radius: 10px;")


       # Tạo frame chứa label_NameProduct và các nút số lượng
       frame_container = QFrame(food_widget)
       frame_container.setObjectName("frame_2")
       frame_layout = QVBoxLayout()


       label_product = QLabel(product_name)
       label_product.setObjectName("label_NameProduct")
       label_product.setFixedSize(97, 24)
       label_product.setStyleSheet("font: 75 9pt 'Segoe UI Variable Display';")
       label_product.setWordWrap(True)


       # Tạo QLabel và nút cộng trừ
       label_quantity = QLabel("1", frame_container)
       label_quantity.setObjectName("label_Quantity")
       label_quantity.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
       btnMinus = QPushButton("-", frame_container)
       btnPlus = QPushButton("+", frame_container)


       btnMinus.setStyleSheet("border: none; font-size: 16px;")
       btnPlus.setStyleSheet("border: none; font-size: 16px;")


       btnMinus.clicked.connect(lambda: self.updateQuantity(label_quantity, -1, label_price, product_price,product_name))
       btnPlus.clicked.connect(lambda: self.updateQuantity(label_quantity, 1, label_price, product_price,product_name))


       quantity_layout = QHBoxLayout()
       quantity_layout.addWidget(btnMinus)
       quantity_layout.addWidget(label_quantity)
       quantity_layout.addWidget(btnPlus)


       frame_layout.addWidget(label_product)
       frame_layout.addLayout(quantity_layout)
       frame_container.setLayout(frame_layout)


       # Tạo frame giá và nút xóa
       frame_price_delete = QFrame()
       frame_price_delete.setObjectName("frame_80")
       frame_layout_price_delete = QVBoxLayout()
       frame_layout_price_delete.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)


       label_price = QLabel(f"{product_price} VNĐ")
       label_price.setObjectName("label_PriceFood")
       label_price.setStyleSheet("font: 75 bold 10pt 'MS Shell Dlg 2';")


       button_delete = QPushButton()
       button_delete.setIcon(QtGui.QIcon(":/WhiteIcons/images/icons/WhiteIcons/delete_ic.svg"))
       button_delete.setIconSize(QtCore.QSize(20, 20))
       button_delete.setStyleSheet("background-color: rgb(145, 8, 12); border-radius: 5px;")
       button_delete.clicked.connect(lambda _, w=food_widget: self.removeFoodFromCheckout(w))


       frame_layout_price_delete.addWidget(button_delete)
       frame_layout_price_delete.addWidget(label_price)
       frame_price_delete.setLayout(frame_layout_price_delete)


       food_layout = QHBoxLayout()
       food_layout.addWidget(frame_container)
       food_layout.addWidget(frame_price_delete)
       food_widget.setLayout(food_layout)


       self.ui.verticalLayout_Checkout.addWidget(food_widget)
       self.updateTotalPriceFood()

       for food in self.selected_foods:
           if food["name"] == product_name:
               food["quantity"] += 1
               food["price"] = int(product_price)
               break
       else:
           self.selected_foods.append({
               "name": product_name,
               "quantity": 1,
               "price": int(product_price)
           })

   def clearLayout(self, layout):
       while layout.count():
           child = layout.takeAt(0)
           if child.widget():
               child.widget().deleteLater()

   def displayFoodInInvoice(self):
       layout = self.ui.verticalLayout_FoodPayment
       # Xóa toàn bộ widget cũ
       while layout.count():
           child = layout.takeAt(0)
           if child.widget():
               child.widget().deleteLater()

       # Hiển thị từng món ăn
       for food in self.selected_foods:
           row = QHBoxLayout()
           name = QLabel(f"{food['name']}")
           qty = QLabel(f"{food['quantity']} x")
           price = QLabel(f"{food['price'] * food['quantity']} VNĐ")

           row.addWidget(qty)
           row.addWidget(name)
           row.addStretch()
           row.addWidget(price)

           container = QWidget()
           container.setLayout(row)
           layout.addWidget(container)


   def updateTotalPriceFood(self):
       """Cập nhật tổng giá của các sản phẩm trong danh sách checkout"""
       total_price = 0
       for i in range(self.ui.verticalLayout_Checkout.count()):
           widget = self.ui.verticalLayout_Checkout.itemAt(i).widget()
           price_label = widget.findChild(QLabel, "label_PriceFood")
           if price_label:
               price_text = price_label.text().replace("VNĐ", "").strip().replace(",", "")
               total_price += int(price_label.text().replace("VNĐ", "").strip())


       self.ui.label_TotalPriceFood.setText(f"{total_price} ")




   def updateQuantity(self, quantity_label, change, price_label, original_price,product_name):
       """Cập nhật số lượng và giá sản phẩm khi nhấn nút + hoặc -"""
       '''current_quantity = int(quantity_label.text())
       new_quantity = max(1, current_quantity + change)
       quantity_label.setText(str(new_quantity))

       new_price = int(original_price.replace("VNĐ", "").strip()) * new_quantity
       price_label.setText(f"{new_price} VNĐ")
       self.updateTotalPriceFood()'''

       current_quantity = int(quantity_label.text())
       new_quantity = max(1, current_quantity + change)
       quantity_label.setText(str(new_quantity))

       for food in self.selected_foods:
           if food["name"] == product_name:
               food["quantity"] = new_quantity

       new_price = int(original_price.replace("VNĐ", "").strip()) * new_quantity
       price_label.setText(f"{new_price} VNĐ")
       self.updateTotalPriceFood()


   def removeFoodFromCheckout(self, widget):
       """Xóa sản phẩm khỏi danh sách checkout"""
       if widget:
           self.ui.verticalLayout_Checkout.removeWidget(widget)
           widget.setParent(None)
           widget.deleteLater()
           self.updateTotalPriceFood()


   def addFoodToPayment(self):
       total_price = self.ui.label_TotalPriceFood.text().strip()
       self.ui.label_BillFood.setText(f"{total_price} VNĐ")
       self.ui.label_BillMovie.setText(self.ui.label_TotalPriceTicket.text())


   def goToHoaDon(self):
       self.addFoodToPayment()  # Thêm dòng này để cập nhật giá
       self.displayFoodInInvoice()
       self.updateTotalBill()
       self.showMovieInfo()
       self.showUserInfo()
       self.ui.stackedWidget.setCurrentWidget(self.ui.pageHoaDon)


   def showUserInfo(self):
       dc = DataConnector()

       # Bước 1: Đọc tên đăng nhập hiện tại từ current_user.json
       base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
       current_user_path = os.path.join(base_path, "dataset", "current_user.json")

       with open(current_user_path, "r", encoding="utf-8") as f:
           username = json.load(f).get("Username")

       # Bước 2: Lấy tất cả người dùng từ DataConnector
       users = dc.get_all_users()

       # Bước 3: Tìm đúng user theo Username
       for user in users:
           if user.get("Username") == username:
               self.ui.label_NameCustomer.setText(user.get("fullname", ""))
               self.ui.label_PhoneCustomer.setText(user.get("phone", ""))
               self.ui.label_ScreenRoom_3.setText(user.get("email", ""))
               return

       # Không tìm thấy thì gán mặc định
       self.ui.label_NameCustomer.setText("Unknown")
       self.ui.label_PhoneCustomer.setText("Unknown")
       self.ui.label_ScreenRoom_3.setText("Unknown")


   def showMovieInfo(self):
       self.ui.label_MovieName_2.setText(self.movie.get("filmTitle", ""))
       self.ui.label_Showtime_2.setText(self.movie.get("Showtimes", ""))
       self.ui.label_ScreenRoom_2.setText(self.movie.get("room", ""))
       self.ui.label_Seats_2.setText(", ".join(sorted(self.selected_seats)))
       self.ui.label_Price_2.setText(self.ui.label_TotalPriceTicket.text())


   def updateTotalBill(self):
       ticket_text = self.ui.label_BillMovie.text().replace("VNĐ", "").strip()
       ticket_total = int(ticket_text) if ticket_text else 0
       # Lấy tiền đồ ăn
       food_text = self.ui.label_BillFood.text().replace("VNĐ", "").strip()
       food_total = int(food_text) if food_text else 0
       # Tổng cộng
       total = ticket_total + food_total
       self.ui.label_TotalBill.setText(f"{total} VNĐ")


   def backToProductCatalog(self):
       """Quay lại trang Product Catalog"""
       self.ui.stackedWidget.setCurrentWidget(self.ui.page_ProductCatalog)
   def showSuccessMessage(self):
       self.save_ticket_to_json()
       msg_box = QMessageBox()
       msg_box.setIcon(QMessageBox.Icon.Information)
       msg_box.setWindowTitle("Thông báo")
       msg_box.setText("Thực hiện giao dịch thành công")
       msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
       msg_box.exec()


   def save_ticket_to_json(self):
       jff = JsonFileFactory()
       filename = "../dataset/bills.json"

       ticket_price = len(self.selected_seats) * self.ticket_price_per_seat
       food_price = sum(item["price"] * item["quantity"] for item in self.selected_foods)
       total = ticket_price + food_price

       new_bill = Bill(
           username=self.username,
           filmTitle=self.movie.get("filmTitle"),
           Showtimes=self.movie.get("Showtimes"),
           room=self.movie.get("room"),
           seats=list(self.selected_seats),
           ticket_price=ticket_price,
           food_price=food_price,
           total_price=total,
           timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
       )


       bills = jff.read_data(filename, Bill)
       bills.append(new_bill)
       jff.write_data(bills, filename)















