class Film:
    def __init__(self, filmId=None,
        filmTitle=None,Gerne=None, Duration=None, Country=None, Author=None, Description=None, Language=None, ReleaseDate=None, Rating=None, Showtimes=None, inventory=None, image=None):
        self.filmId = filmId
        self.filmTitle = filmTitle
        self.Gerne = Gerne
        self.Duration = Duration
        self.Country = Country
        self.Author = Author
        self.Language = Language
        self.Description = Description
        self.ReleaseDate = ReleaseDate
        self.Rating = Rating
        self.Showtimes = Showtimes
        self.inventory = inventory
        self.image = image

    def __str__(self):
        return f'{self.filmId}\t{self.filmTitle}\t{self.Gerne}\t{self.Duration}\t{self.Country}\t{self.Author}\t{self.Description}\t{self.Language}\t{self.ReleaseDate}\t{self.Rating}\t{self.Showtimes}\t{self.inventory}\t{self.image}'
