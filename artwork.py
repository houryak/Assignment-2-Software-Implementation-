class Artwork:
    def __init__(self, title, artist, date, significance, location):
        self.title = title
        self.artist = artist
        self.date = date
        self.significance = significance
        self.location = location

    def get_info(self):
        return f"{self.title} by {self.artist} created on {self.date}. Significance: {self.significance} at {self.location}"