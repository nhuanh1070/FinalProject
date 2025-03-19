from CSDL.libs.JsonFileFactory import JsonFileFactory
from CSDL.models.User import User

users=[]
users.append(User("nhuanh","anh123"))
users.append(User("minhnguyen","minh456"))
users.append(User("linhtran","linh456"))
users.append(User("tuanle","tuan456"))
users.append(User("hoangphat","phat123"))
print ("Danh sách người dùng:")
for user in users:
    print(user)
jff=JsonFileFactory()
filename= "../../dataset/user.json"
jff.write_data(users,filename)