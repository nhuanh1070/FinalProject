from CSDL.libs.JsonFileFactory import JsonFileFactory
from CSDL.models.User import User

users=[]
users.append(User("Tèo","teo456"))
users.append(User("Tý","ty456"))
users.append(User("Bin","bin456"))
print ("Danh sách người dùng:")
for user in users:
    print(user)
jff=JsonFileFactory()
filename="../dataset/user.json"
jff.write_data(users,filename)