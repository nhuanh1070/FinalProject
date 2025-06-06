from CSDL.libs.JsonFileFactory import JsonFileFactory
from CSDL.models.UserInfor import UserInfor

users = []
users.append(UserInfor("nhuanh", "anh123","Phạm Lê Như Anh", "2006-05-15", "0987654321", "nhuanh@example.com"))
users.append(UserInfor("minhnguyen","minh456", "Nguyễn Minh", "2005-07-20", "0912345678", "minh@example.com"))
users.append(UserInfor("linhtran", "linh456","Trần Kim Linh", "2004-12-10", "0987123456", "linh@example.com"))
users.append(UserInfor("tuanle", "tuan456","Lê Tuấn", "2003-08-22", "0978123456", "tuanle@example.com"))
users.append(UserInfor("hoangphat", "phat123","Ngô Hoàng Phát", "2002-11-30", "0967123456", "hoangphat@example.com"))

print("Danh sách User:")
for user in users:
    print(user)

jff = JsonFileFactory()
filename = "../../dataset/users_data.json"
jff.write_data(users, filename)
