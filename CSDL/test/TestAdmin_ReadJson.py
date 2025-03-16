from CSDL.libs.JsonFileFactory import JsonFileFactory
from CSDL.models.Admin import Admin

jff=JsonFileFactory()
filename="../dataset/admin.json"
admins=jff.read_data(filename,Admin)
print("Danh sach Admin sau khi doc file:")
for admin in admins:
    print(admin)
