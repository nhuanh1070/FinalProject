import json
import os

from CSDL.libs.JsonFileFactory import JsonFileFactory
from CSDL.models.Film import Film
from CSDL.models.User import User



class DataConnector:
    def __init__(self):
        # Xác định thư mục gốc của dự án (FinalProject/FinalProject/)
        base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

        # Sửa đường dẫn dataset để đảm bảo không bị lỗi
        self.dataset_path = os.path.join(base_path, "dataset")
        self.users_file = os.path.join(self.dataset_path, "users_data.json")
        self.films_file = os.path.join(self.dataset_path, "film.json")

        self.ensure_file_exists()

    def ensure_file_exists(self):
        """Đảm bảo thư mục dataset và các tệp JSON tồn tại"""
        for filename in [self.users_file, self.films_file]:
            directory = os.path.dirname(filename)
            if not os.path.exists(directory):
                os.makedirs(directory)  # Tạo thư mục nếu chưa tồn tại
            if not os.path.exists(filename):
                with open(filename, 'w', encoding="utf-8") as f:
                    json.dump([], f, indent=4, ensure_ascii=False)

    def get_all_users(self):
        jff = JsonFileFactory()
        print(f"📌 Debug - Đang đọc file {self.users_file}...")

        try:
            with open(self.users_file, "r", encoding="utf-8") as f:
                users = json.load(f)  # Không dùng jff.read_data()

            if not isinstance(users, list):
                print("❌ LỖI: Dữ liệu trong users_data.json không phải danh sách!")
                return []

            print(f"✅ Đọc thành công! Danh sách users: {users}")
            return users
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"❌ LỖI: Không thể đọc file users_data.json - {e}")
            return []

    def save_account(self,user):
        filename = self.users_file
        users = self.get_all_users()  # Đọc danh sách user từ JSON

        if users is None:
            users = []

        # Kiểm tra trùng lặp Username
        for u in users:
            if u.get("Username") == user.Username:
                print(f"❌ LỖI: Username {user.Username} đã tồn tại!")
                return False  # Username đã tồn tại

        # Tạo tài khoản mới
        new_user = {
            "Username": user.Username,
            "Password": user.Password,
            "fullname": "",
            "birthday": "",
            "phone": "",
            "email": ""
        }
        users.append(new_user)

        print(f"📌 Debug - Đang ghi dữ liệu vào {filename}...")

        try:
            with open(filename, "w", encoding="utf-8") as f:
                json.dump(users, f, indent=4, ensure_ascii=False)  # Ghi dữ liệu đúng định dạng
            print(f"✅ Tài khoản mới đã được lưu: {new_user}")
            return True
        except Exception as e:
            print(f"❌ LỖI KHI GHI FILE JSON: {str(e)}")
            return False

    def save_film(self,film):
        films = self.get_all_films()
        films.append(film)
        jff = JsonFileFactory()
        jff.write_data(films, self.films_file)

    def check_user_exist(self,Username):
        print(f"📌 Debug - Đang kiểm tra username: {Username}")

        users = self.get_all_users()

        if users is None:
            print("❌ LỖI: Không thể lấy danh sách users từ JSON!")
            return -1

        print(f"📌 Debug - Danh sách user hiện có: {users}")

        for i, user in enumerate(users):
            if user.get("Username") == Username:
                print(f"✅ Tìm thấy username: {Username} (index {i})")
                return i  # Username tồn tại

        print(f"❌ Không tìm thấy username: {Username}")
        return -1  # Username không tồn tại

    def get_all_films(self):
        jff = JsonFileFactory()
        films = jff.read_data(self.films_file, Film)
        if films is None:
            return []
        return films

    def find_index_filmName(self,a):
        self.films=self.get_all_films()
        for i in range(len(self.films)):
            film=self.films[i]
            if film.filmTitle==a:
                return i
        return -1

    '''def remove_film(self, filmTitle):
        # Lấy danh sách phim hiện tại
        films = self.get_all_films()

        # Tìm index của phim cần xóa
        index = self.find_index_filmName(filmTitle)

        if index != -1:
            films.pop(index)  # Xóa phim khỏi danh sách

            # Ghi danh sách mới vào file JSON
            jff = JsonFileFactory()
            filename = "../../dataset/film.json"  # Đảm bảo đường dẫn đúng
            jff.write_data(films, filename)

            print(f'Phim "{filmTitle}" đã bị xóa.')
        else:
            print(f'Không tìm thấy phim "{filmTitle}" để xóa.')'''

    def remove_film(self, filmTitle):
        """Xóa phim theo tên"""
        films = self.get_all_films()
        filmTitle = filmTitle.strip().lower()

        # Tìm index của phim cần xóa
        index = -1
        for i, film in enumerate(films):
            if film.filmTitle.strip().lower() == filmTitle:
                index = i
                break

        if index != -1:
            del films[index]  # Xóa phim khỏi danh sách

            # Ghi danh sách mới vào file JSON
            jff = JsonFileFactory()
            jff.write_data(films, self.films_file)  # Dùng đường dẫn động

            print(f'✅ Phim "{filmTitle}" đã bị xóa.')
        else:
            print(f'❌ Không tìm thấy phim "{filmTitle}" để xóa.')

    def update_user_info(self, Username, Fullname, Birthday, Phone, Email):
        print(f"📌 Debug - Đang tìm user {Username} trong JSON để cập nhật thông tin...")

        filename = self.users_file
        users = self.get_all_users()

        if users is None:
            print("❌ LỖI: Không thể lấy danh sách users từ JSON!")
            return False

        updated = False
        for user in users:
            if user["Username"] == Username:
                print(f"✅ Tìm thấy user {Username}, cập nhật thông tin...")
                user["fullname"] = Fullname
                user["birthday"] = Birthday
                user["phone"] = Phone
                user["email"] = Email
                updated = True
                break

        if updated:
            try:
                with open(filename, "w", encoding="utf-8") as f:
                    json.dump(users, f, indent=4, ensure_ascii=False)
                print(f"✅ Cập nhật thành công user {Username}!")
                return True
            except Exception as e:
                print(f"❌ LỖI KHI GHI FILE JSON: {e}")
                return False
        else:
            print(f"❌ Không tìm thấy user {Username} trong JSON!")
            return False


