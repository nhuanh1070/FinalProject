class Ticket:
   def __init__(self,username, filmTitle, Showtimes, room, seats, ticket_price, timestamp):
       self.username = username
       self.filmTitle = filmTitle
       self.Showtimes = Showtimes
       self.room = room
       self.seats = seats  # List of seat identifiers (e.g., ["A1", "A2"])
       self.ticket_price = ticket_price  # Total price for the selected seats
       self.timestamp = timestamp


   def __str__(self):
       return f'{self.username}\t{self.filmTitle}\t{self.Showtimes}\t{self.room}\t{self.seats},{self.ticket_price}\t{self.timestamp}'

