from CSDL.libs.DataConnector import DataConnector
from CSDL.models.User import User
from CSDL.libs.DataConnector import DataConnector

dc = DataConnector()

# Test lấy danh sách người dùng
users = dc.get_all_users()
print("List of Users in database:")
for user in users:
    print(user)

dc = DataConnector()

# Test lấy danh sách người dùng
users = dc.get_all_users()
print("List of Users in database:")
for user in users:
    print(user)

# Test kiểm tra người dùng có tồn tại không
username = "test_user"
user_index = dc.check_user_exist(username)
print(f"User '{username}' exists at index:", user_index)

# Test thêm tài khoản mới
new_user = User(Username="new_user", Password="password123")
dc.save_account(new_user)
print("New user added.")

# Test lấy danh sách phim
films = dc.get_all_films()
print("List of Films in database:")
for film in films:
    print(film)

# Test tìm phim theo tên
film_title = "Inception"
film_index = dc.find_index_filmName(film_title)
print(f"Film '{film_title}' exists at index:", film_index)

# Test xóa phim
film_to_remove = "Avatar"
dc.remove_film(film_to_remove)
print(f"Film '{film_to_remove}' removed if existed.")

# Test kiểm tra người dùng có tồn tại không
username = "test_user"
user_index = dc.check_user_exist(username)
print(f"User '{username}' exists at index:", user_index)

# Test thêm tài khoản mới
new_user = User(Username="new_user", Password="password123")
dc.save_account(new_user)
print("New user added.")

# Test lấy danh sách phim
films = dc.get_all_films()
print("List of Films in database:")
for film in films:
    print(film)

# Test tìm phim theo tên
film_title = "Inception"
film_index = dc.find_index_filmName(film_title)
print(f"Film '{film_title}' exists at index:", film_index)

# Test xóa phim
film_to_remove = "Avatar"
dc.remove_film(film_to_remove)
print(f"Film '{film_to_remove}' removed if existed.")