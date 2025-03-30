import json
import os
import datetime

import openpyxl
from PyQt6.QtWidgets import QFileDialog, QMessageBox, QDialog
import csv
from PyQt6.QtCore import QDate

from ui.admin.Export import Ui_Dialog


class ExportExt(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Kết nối các nút xuất file với phương thức tương ứng
        self.ui.pushButtonExportCSV.clicked.connect(self.show_export_window)
        self.ui.pushButtonExportExcel.clicked.connect(self.show_export_window)
        self.ui.pushButtonExportJSON.clicked.connect(self.show_export_window)
        self.ui.pushButtonExportTXT.clicked.connect(self.show_export_window)
    def filter_bills_by_date(self, selected_date):
        try:
            # Đọc dữ liệu từ file JSON
            with open(os.path.join(os.path.dirname(__file__), '..', '..', 'dataset', 'bills.json'), 'r') as file:
                bills_data = json.load(file)

            # Chuyển đổi selected_date thành định dạng 'yyyy-MM-dd'
            selected_date_obj = QDate.fromString(selected_date, "yyyy-MM-dd")
            selected_date_str = selected_date_obj.toString("yyyy-MM-dd")

            filtered_bills = []
            for bill in bills_data:
                timestamp = bill.get('timestamp')

                # Kiểm tra nếu timestamp là chuỗi và chuyển nó thành đối tượng datetime
                if isinstance(timestamp, str):
                    try:
                        # Chuyển chuỗi timestamp thành đối tượng datetime
                        bill_date = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d")
                    except ValueError:
                        # Nếu timestamp không đúng định dạng, bỏ qua
                        print(f"Invalid timestamp format: {timestamp}")
                        continue

                    # So sánh với ngày đã chọn
                    if bill_date == selected_date_str:
                        filtered_bills.append(bill)


            return filtered_bills if filtered_bills else None
        except Exception as e:
            return None

    # Export to CSV
    def export_to_csv(self, data, selected_date):
        dataset_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'dataset')
        filename, _ = QFileDialog.getSaveFileName(self, "Save File",
                                                  os.path.join(dataset_dir, f"DoanhThu_{selected_date}.csv"),
                                                  "CSV Files (*.csv)")

        if not filename:
            QMessageBox.warning(self, "Lỗi", "Chưa chọn đường dẫn để lưu file.")
            return

        try:
            with open(filename, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)

            QMessageBox.information(self, "Thành công", f"Đã xuất file CSV thành công: {filename}")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể xuất file: {str(e)}")

    # Export to Excel
    def export_to_excel(self, data, selected_date):
        dataset_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'dataset')
        filename, _ = QFileDialog.getSaveFileName(self, "Save File",
                                                  os.path.join(dataset_dir, f"DoanhThu_{selected_date}.xlsx"),
                                                  "Excel Files (*.xlsx)")

        if not filename:
            QMessageBox.warning(self, "Lỗi", "Chưa chọn đường dẫn để lưu file.")
            return

        try:
            wb = openpyxl.Workbook()
            sheet = wb.active
            sheet.append(list(data[0].keys()))  # Tiêu đề cột

            for row in data:
                # Chuyển danh sách ghế thành chuỗi trước khi xuất
                if isinstance(row['seats'], list):
                    row['seats'] = ', '.join(row['seats'])
                sheet.append(list(row.values()))

            wb.save(filename)
            QMessageBox.information(self, "Thành công", f"Đã xuất file Excel thành công: {filename}")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể xuất file: {str(e)}")


    # Export to JSON
    def export_to_json(self, data, selected_date):
        dataset_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'dataset')
        filename, _ = QFileDialog.getSaveFileName(self, "Save File",
                                                  os.path.join(dataset_dir, f"DoanhThu_{selected_date}.json"),
                                                  "JSON Files (*.json)")

        if not filename:
            QMessageBox.warning(self, "Lỗi", "Chưa chọn đường dẫn để lưu file.")
            return

        try:
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)

            QMessageBox.information(self, "Thành công", f"Đã xuất file JSON thành công: {filename}")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể xuất file: {str(e)}")

    # Export to TXT
    def export_to_txt(self, data, selected_date):
        dataset_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'dataset')
        filename, _ = QFileDialog.getSaveFileName(self, "Save File",
                                                  os.path.join(dataset_dir, f"DoanhThu_{selected_date}.txt"),
                                                  "Text Files (*.txt)")

        if not filename:
            QMessageBox.warning(self, "Lỗi", "Chưa chọn đường dẫn để lưu file.")
            return

        try:
            with open(filename, 'w', encoding='utf-8') as file:
                for bill in data:
                    line = '\t'.join([f"{key}: {value}" for key, value in bill.items()]) + "\n"
                    file.write(line)

            QMessageBox.information(self, "Thành công", f"Đã xuất file TXT thành công: {filename}")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể xuất file: {str(e)}")

    def show_export_window(self):
        selected_date = self.ui.calendarWidget.selectedDate().toString("yyyy-MM-dd")

        # Lọc dữ liệu theo ngày đã chọn
        filtered_bills = self.filter_bills_by_date(selected_date)

        if filtered_bills is None or len(filtered_bills) == 0:
            return

        # Kiểm tra kiểu file và gọi hàm tương ứng
        if self.sender() == self.ui.pushButtonExportCSV:
            self.export_to_csv(filtered_bills, selected_date)
        elif self.sender() == self.ui.pushButtonExportExcel:
            self.export_to_excel(filtered_bills, selected_date)
        elif self.sender() == self.ui.pushButtonExportJSON:
            self.export_to_json(filtered_bills, selected_date)
        elif self.sender() == self.ui.pushButtonExportTXT:
            self.export_to_txt(filtered_bills, selected_date)