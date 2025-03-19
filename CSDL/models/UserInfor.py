class UserInfor:
    def __init__(self, Username,Password, fullname, birthday, phone, email):
        self.Username = Username
        self.Password = Password
        self.fullname = fullname
        self.birthday = birthday
        self.phone = phone
        self.email = email

    def __str__(self):
        return f'{self.Username}\t{self.Password}\t{self.fullname}\t{self.birthday}\t{self.phone}\t{self.email}'
