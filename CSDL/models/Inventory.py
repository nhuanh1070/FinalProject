class Inventory:
    def __init__(self,filmId,availableSeats,totalSeats):
        self.filmId=filmId
        self.availableSeats=availableSeats
        self.totalSeats=totalSeats
    def __str__(self):
        return f'{self.filmId}\t{self.availableSeats}\t{self.totalSeats}'