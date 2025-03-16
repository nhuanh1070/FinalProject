from CSDL.libs.DataConnector import DataConnector
from CSDL.models.User import User

# Khởi tạo đối tượng DataConnector
dc = DataConnector()
users=dc.get_all_users()
print("danh sách người dùng:")














# 📌 Lấy toàn bộ người dùng
users = dc.get_all_users()
print("Danh sách tài khoản người dùng:")
for u in users:
    print(f"- Username: {u.Username}, Password: {u.Password}")

# 📌 Thêm tài khoản mới
new_user = User("test_user", "password123")
dc.save_account(new_user)
print(f"Tài khoản '{new_user.Username}' đã được thêm.")

# 📌 Kiểm tra danh sách người dùng sau khi thêm
users = dc.get_all_users()
print("Danh sách tài khoản sau khi thêm:")
for u in users:
    print(f"- Username: {u.Username}, Password: {u.Password}")

# 📌 Kiểm tra tài khoản đã tồn tại
username_check = "test_user"
index = dc.check_user_exist(username_check)
if index != -1:
    print(f"Tài khoản '{username_check}' đã tồn tại trong hệ thống.")
else:
    print(f"Tài khoản '{username_check}' không tồn tại trong hệ thống.")

# 📌 Kiểm tra tài khoản không tồn tại
username_check = "not_existing_user"
index = dc.check_user_exist(username_check)
if index != -1:
    print(f"Tài khoản '{username_check}' đã tồn tại trong hệ thống.")
else:
    print(f"Tài khoản '{username_check}' không tồn tại trong hệ thống.")

# 📌 Test đăng nhập hệ thống
test_uid = "test_user"
test_pwd = "password123"

found_index = dc.check_user_exist(test_uid)
if found_index != -1:
    print("Đăng nhập thành công!")
else:
    print("Đăng nhập thất bại!")

