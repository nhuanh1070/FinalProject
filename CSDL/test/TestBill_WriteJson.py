from CSDL.libs.JsonFileFactory import JsonFileFactory
from CSDL.models.Bill import Bill

bills=[]
bills.append(Bill("nhuanh123","SPIDERMAN","20:00","Room 5",["A1", "A2"],100000,150000,250000,"2025-03-28 07:30:10"))

print("Danh sách User:")
for bill in bills:
    print(bill)

jff = JsonFileFactory()
filename = "../../dataset/bills.json"
jff.write_data(bills, filename)