from CSDL.libs.JsonFileFactory import JsonFileFactory
from CSDL.models.Admin import Admin

admins=[]
admins.append(Admin("NhatMinh","minh123"))
admins.append(Admin("NhuAnh","anh123"))
admins.append(Admin("AnhTai","tai123"))
admins.append(Admin("KimLinh","linh123"))
admins.append(Admin("TruongSơn","son123"))
print("Danh sách Admin:")
for admin in admins:
    print(admin)
jff=JsonFileFactory()
filename= "../../dataset/admin.json"
jff.write_data(admins,filename)