from PyQt6 import QtGui, QtCore
from PyQt6.QtWidgets import QDialog, QMessageBox, QHBoxLayout, QWidget, QLabel, QSpinBox, QPushButton, QVBoxLayout, \
    QFrame
from utils import resources_rc
from utils import resources_food_rc
from ui.user.BookTicket import Ui_Dialog



class BookTicketExt(QDialog):
    def __init__(self, movie, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageChonGhe)
        self.movie = movie  # Lưu thông tin phim
        self.selected_seats = set()

        self.setupSignalAndSlot()


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

    def goToProductCategory(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_ProductCatalog)

    def goToHoaDon(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageHoaDon)

    def showSuccessMessage(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setWindowTitle("Thông báo")
        msg_box.setText("Thực hiện giao dịch thành công")
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()

    def backToHomePage(self):
        from ui.user.UserUiExt import UserUiExt
        self.close()  # Đóng cửa sổ hiện tại
        self.user_ui = UserUiExt()
        self.user_ui.showWindow()

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

    def addFoodToCheckout(self, index):
        """Thêm sản phẩm vào danh sách checkout"""
        label_name = getattr(self.ui, f"label_NameProduct_{index}", None)
        if not label_name:
            return

        product_name = label_name.text()

        # Tạo widget chứa thông tin sản phẩm
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

        # Thay QSpinBox bằng QLabel và hai QPushButton
        self.labelQuantity = QLabel("1", frame_container)  # Hiển thị số lượng
        self.labelQuantity.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)  # Căn giữa số lượng
        self.btnMinus = QPushButton("-", frame_container)
        self.btnPlus = QPushButton("+", frame_container)

        # Xóa màu nền nút
        self.btnMinus.setStyleSheet("border: none; font-size: 16px;")
        self.btnPlus.setStyleSheet("border: none; font-size: 16px;")

        # Gán sự kiện tăng giảm số lượng
        self.btnMinus.clicked.connect(lambda: self.updateQuantity(self.labelQuantity, -1))
        self.btnPlus.clicked.connect(lambda: self.updateQuantity(self.labelQuantity, 1))

        # Thêm vào layout
        quantity_layout = QHBoxLayout()
        quantity_layout.addWidget(self.btnMinus)
        quantity_layout.addWidget(self.labelQuantity)
        quantity_layout.addWidget(self.btnPlus)
        frame_layout.addWidget(label_product)
        frame_layout.addLayout(quantity_layout)
        frame_container.setLayout(frame_layout)

        # Tạo frame chứa label_PriceFood và pushButton_Delete
        frame_price_delete = QFrame()
        frame_price_delete.setObjectName("frame_80")
        frame_layout_price_delete = QVBoxLayout()
        frame_layout_price_delete.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)  # Căn trái để không che chữ "VNĐ"

        label_price = QLabel("75000 VNĐ")
        label_price.setObjectName("label_PriceFood")
        label_price.setStyleSheet("font: 75 bold 10pt 'MS Shell Dlg 2';")

        button_delete = QPushButton()
        button_delete.setObjectName("pushButton_Delete")
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

        # Thêm widget vào layout
        self.ui.verticalLayout_Checkout.addWidget(food_widget)

    def removeFoodFromCheckout(self, widget):
        """Xóa sản phẩm khỏi danh sách checkout"""
        if widget:
            self.ui.verticalLayout_Checkout.removeWidget(widget)
            widget.setParent(None)
            widget.deleteLater()

    def updateQuantity(self, label, value):
        """Hàm xử lý tăng giảm số lượng sản phẩm"""
        current_quantity = int(label.text())
        new_quantity = max(1, current_quantity + value)  # Không cho phép số lượng < 1
        label.setText(str(new_quantity))

    def backToProductCatalog(self):
        """Quay lại trang Product Catalog"""
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_ProductCatalog)

    def backToChonGhe(self):
        """Quay lại trang Chọn Ghế"""
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageChonGhe)