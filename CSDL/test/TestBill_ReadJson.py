from CSDL.libs.JsonFileFactory import JsonFileFactory
from CSDL.models.Bill import Bill

jff=JsonFileFactory()
filename= "../../dataset/bills.json"
bill=jff.read_data(filename,Bill)
print("Danh sách thông tin người dùng sau khi loading:")
for bill in bill:
    print(bill,end="")