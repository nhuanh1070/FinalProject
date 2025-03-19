from CSDL.libs.JsonFileFactory import JsonFileFactory
from CSDL.models.UserInfor import UserInfor

users = []
users.append(UserInfor("nhuanh", "Phạm Lê Như Anh", "2006-05-15", "0987654321", "nhuanh@example.com"))
users.append(UserInfor("minhnguyen", "Nguyễn Minh", "2005-07-20", "0912345678", "minh@example.com"))
users.append(UserInfor("linhtran", "Trần Kim Linh", "2004-12-10", "0987123456", "linh@example.com"))
users.append(UserInfor("tuanle", "Lê Tuấn", "2003-08-22", "0978123456", "tuanle@example.com"))
users.append(UserInfor("hoangphat", "Ngô Hoàng Phát", "2002-11-30", "0967123456", "hoangphat@example.com"))

print("Danh sách User:")
for user in users:
    print(user)

jff = JsonFileFactory()
filename = "../../dataset/UserS.json"
jff.write_data(users, filename)
