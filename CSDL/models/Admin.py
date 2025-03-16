class Admin:
    def __init__(self,Username,Password):
        self.Username=Username
        self.Password=Password
    def __str__(self):
        return f'{self.Username}\t{self.Password}'