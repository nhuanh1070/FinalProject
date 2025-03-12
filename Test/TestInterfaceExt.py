# myApp.py
import sys
from PyQt6.QtWidgets import QApplication
from ui.interfaceExt import MainWindow  # Import class từ file `interfaceExt.py`

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
