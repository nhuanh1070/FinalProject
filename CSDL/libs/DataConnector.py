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
