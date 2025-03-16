from CSDL.libs.JsonFileFactory import JsonFileFactory
from CSDL.models.Admin import Admin

admins=[]
admins.append(Admin("Nhật Minh","minh123"))
admins.append(Admin("Như Anh","anh123"))
admins.append(Admin("Anh Tài","tai123"))
admins.append(Admin("Kim Linh","linh123"))
admins.append(Admin("Trường Sơn","son123"))
print("Danh sách Admin:")
for admin in admins:
    print(admin)
jff=JsonFileFactory()
filename="../dataset/admin.json"
jff.write_data(admins,filename)