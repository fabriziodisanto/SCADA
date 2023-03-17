from models.players_validator import validate_data


class Player:

    def __init__(self, first_name: str, last_name: str, country: str, club: str):
        validate_data(first_name, last_name, country, club)
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.club = club

    def to_db_collection(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'country': self.country,
            'club': self.club,
        }
