class Event:
    def __init__(self, type, location, duration):
        self.type = type
        self.location = location
        self.duration = duration

    def get_event_info(self):
        return f"{self.type} at {self.location} for {self.duration}"