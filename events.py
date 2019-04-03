class Events:
    def __init__(self):
        self.hours = 0
        self.special_event = ""
        self.started = False

    def salary(self):
        return self.hours == int(self.hours) and self.hours % (30*24) == 0

    def update(self):
        self.hours += 0.2

    def get_day(self):
        return int(self.hours/24) + 1

    def get_hours(self):
        return int(self.hours)
