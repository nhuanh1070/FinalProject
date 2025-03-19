from CSDL.libs.JsonFileFactory import JsonFileFactory
from CSDL.models.UserInfor import UserInfor

jff=JsonFileFactory()
filename= "../../dataset/users_data.json"
user=jff.read_data(filename,UserInfor)
print("Danh sách thông tin người dùng sau khi loading:")
for user in user:
    print(user,end="")
