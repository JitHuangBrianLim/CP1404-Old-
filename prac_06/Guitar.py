CURRENT_DATE = 2022
VALID_VINTAGE = 50


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        return CURRENT_DATE - self.year

    def is_vintage(self):
        return self.get_age() >= VALID_VINTAGE

    def __lt__(self, other):
        return self.year < other.year