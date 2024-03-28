class Exhibition:
    def __init__(self, location, duration):
        self.location = location
        self.duration = duration

    def get_details(self):
        return f"Location: {self.location}, Duration: {self.duration}"