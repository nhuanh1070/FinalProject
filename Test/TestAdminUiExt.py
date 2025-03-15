from PyQt6.QtWidgets import QApplication
from ui.admin.AdminUiExt import AdminUiExt

# Khởi tạo ứng dụng
app = QApplication([])

# Tạo cửa sổ UI
ui = AdminUiExt()
ui.showWindow()  # Hiển thị cửa sổ chính

# Chạy vòng lặp sự kiện
app.exec()
