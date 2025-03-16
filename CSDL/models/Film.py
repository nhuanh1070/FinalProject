class Film:
    def __init__(self,filmId,filmTitle,Gerne,Duration,Language,ReleaseDate,Rating,Showtimes,inventory):
        self.filmId=filmId
        self.filmTitle=filmTitle
        self.Gerne=Gerne
        self.Duration=Duration
        self.Language=Language
        self.ReleaseDate=ReleaseDate
        self.Rating=Rating
        self.Showtimes=Showtimes
        self.inventory=inventory
    def __str__(self):
        return f'{self.filmId}\t{self.filmTitle}\t{self.Gerne}\t{self.Duration}\t{self.Language}\t{self.ReleaseDate}\t{self.Rating}\t{self.Showtimes}\t{self.inventory}'



