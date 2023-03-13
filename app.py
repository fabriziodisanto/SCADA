from flask import Flask, abort, request

app = Flask(__name__)

players = [{
    'id': '1',
    'first_name': 'Lionel',
    'last_name': 'Messi',
    'country': 'Argentina',
    'club': 'PSG',
}, {
    'id': '2',
    'first_name': 'Kylian',
    'last_name': 'Mbappe',
    'country': 'France',
    'club': 'PSG',
}, {
    'id': '3',
    'first_name': 'Karim',
    'last_name': 'Benzema',
    'country': 'France',
    'club': 'Real Madrid',
},
]


@app.get('/players/club/<club>/')
def get_player_by_club(club):
    result = []
    for p in players:
        if p['club'] == club:
            result.append(p)
    return result


@app.get('/players/country/<country>/')
def get_player_by_country(country):
    result = []
    for p in players:
        if p['country'] == country:
            result.append(p)
    return result


@app.get('/players/<id>/')
def get_player_by_id(id):
    for p in players:
        if p['id'] == id:
            return p
    abort(404)


@app.get('/players')
def get_players():
    return players


@app.post('/players')
def post_player():
    data = request.get_json()
    # todo validate data
    players.append(data)
    return data


@app.put('/players/<id>/')
def update_club(id):
    player = get_player_by_id(id)
    data = request.get_json()
    # todo validate data
    player['club'] = data['club']
    delete_player_by_id(id)
    players.append(player)
    return player


@app.delete('/players/<id>/')
def delete_player_by_id(id):
    global players

    players = [p for p in players if p['id'] != id]
    return {}


@app.route('/ping')
def ping():
    return 'pong'


if __name__ == '__main__':
    app.run()
