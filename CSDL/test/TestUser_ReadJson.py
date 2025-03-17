from CSDL.libs.JsonFileFactory import JsonFileFactory
from CSDL.models.User import User

jff=JsonFileFactory()
filename= "../../dataset/user.json"
users=jff.read_data(filename,User)
print("Danh sách người dùng sau khi loading:")
for user in users:
    print(user)