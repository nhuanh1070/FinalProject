class UserInfor:
    def __init__(self, Username, fullname, birthday, phone, email):
        self.Username = Username
        self.fullname = fullname
        self.birthday = birthday
        self.phone = phone
        self.email = email

    def __str__(self):
        return f'{self.Username}\n{self.fullname}\n{self.birthday}\n{self.phone}\n{self.email}'
