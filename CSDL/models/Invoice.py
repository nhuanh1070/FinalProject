class Invoice:
    def __init__(self,invoiceId,username,filmTitle,Seat):
        self.invoiceId=invoiceId
        self.username=username
        self.filmTitle=filmTitle
        self.Seat=Seat
    def __str__(self):
        return f'{self.invoiceId}\t{self.username}\t{self.filmTitle}\t{self.Seat}'
    