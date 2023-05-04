valid_countries = ['Argentina', 'Brasil', 'France', 'Peru', 'España']


def validate_data(first_name, last_name, country, club):
    if first_name == '':
        raise TypeError('Invalid first_name')
    if last_name == '':
        raise TypeError('Invalid last_name')
    if country == '' or country not in valid_countries:
        raise TypeError('Invalid country')
    if club == '':
        raise TypeError('Invalid club')