import os

from CSDL.libs.JsonFileFactory import JsonFileFactory
from CSDL.models.Film import Film
from CSDL.models.User import User



class DataConnector:
    def __init__(self):
        self.filename = "../../dataset/user.json"
        self.ensure_file_exists()  # Đảm bảo tệp JSON tồn tại
    def ensure_file_exists(self):
        """Đảm bảo thư mục dataset và tệp user.json tồn tại"""
        directory = os.path.dirname(self.filename)

        if not os.path.exists(directory):
            os.makedirs(directory)  # Tạo thư mục nếu chưa tồn tại

        if not os.path.exists(self.filename):
            with open(self.filename, 'w', encoding='utf-8') as f:
                f.write('[]')  # Ghi một mả

    def get_all_users(self):
        jff = JsonFileFactory()
        filename = "../../dataset/user.json"
        users = jff.read_data(filename, User)
        return users

    def save_account(self,user):
        users = self.get_all_users()
        users.append(user)
        jff = JsonFileFactory()
        filename = "../../dataset/user.json"
        jff.write_data(users, filename)

    def save_film(self,film):
        films = self.get_all_films()
        films.append(film)
        jff = JsonFileFactory()
        filename = "../../dataset/film.json"
        jff.write_data(films, filename)

    def check_user_exist(self,Username):
        self.users = self.get_all_users()
        for i in range(len(self.users)):
            user = self.users[i]
            if user.Username == Username:  # found
                return i
        return -1

    def get_all_films(self):
        jff = JsonFileFactory()
        filename = "../../dataset/film.json"
        films = jff.read_data(filename, Film)
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

    def remove_film(self, films, filmTitle):

        # Chuẩn hóa tên phim cần tìm
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
            filename = "../../dataset/film.json"  # Đảm bảo đường dẫn đúng
            jff.write_data(films, filename)
            self.save_film(films)

            print(f'Phim "{filmTitle}" đã bị xóa.')
        else:
            print(f'Không tìm thấy phim "{filmTitle}" để xóa.')



