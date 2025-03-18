class Film:
    def __init__(self, filmId, filmTitle, Gerne, Duration, Country, Author, Description, Language, ReleaseDate, Rating, Showtimes, inventory, image="default.jpg"):
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
        self.image = image  # ✅ Thêm thuộc tính ảnh vào class

    def __str__(self):
        return f'{self.filmId}\t{self.filmTitle}\t{self.Gerne}\t{self.Duration}\t{self.Country}\t{self.Author}\t{self.Description}\t{self.Language}\t{self.ReleaseDate}\t{self.Rating}\t{self.Showtimes}\t{self.inventory}\t{self.image}'
