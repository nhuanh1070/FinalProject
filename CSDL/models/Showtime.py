class Showtime:
    def __init__(self,showtimeId,filmId,datetime,room,availableSeats):
        self.showtimeId=showtimeId
        self.filmId=filmId
        self.datetime=datetime
        self.room=room
        self.availableSeats=availableSeats
    def __str__(self):
        return f'{self.showtimeId}\t{self.filmId}\t{self.datetime}\t{self.room}\t{self.availableSeats}'