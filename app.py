from flask import Flask, abort, request, jsonify
import database as db_connection
from models.players import Player
from bson.objectid import ObjectId


app = Flask(__name__)
db = db_connection.db_connection()


@app.get('/players/club/<club>/')
def get_player_by_club(club):
    players = list(db['players'].find({'club': club}))
    for player in players:
        player['_id'] = str(player['_id'])

    return players


@app.get('/players/country/<country>/')
def get_player_by_country(country):
    players = list(db['players'].find({'country': country}))
    for player in players:
        player['_id'] = str(player['_id'])

    return players


@app.get('/players/<id>/')
def get_player_by_id(id):
    player = db['players'].find_one({'_id': ObjectId(id)})
    if player is None:
        abort(404)
    player['_id'] = str(player['_id'])
    return player


@app.get('/players')
def get_players():
    players = list(db['players'].find())
    for player in players:
        player['_id'] = str(player['_id'])

    return players


@app.post('/players')
def post_player():
    data = request.get_json()
    try:
        player = Player(**data)
        result = db['players'].insert_one(player.to_db_collection())
        response = {
            **player.to_db_collection(),
            'id': str(result.inserted_id),
        }
        return jsonify(response)
    except TypeError:
        abort(400)


@app.put('/players/<id>/')
def update_club(id):
    data = request.get_json()
    if 'club' not in data or data['club'] == '':
        abort(400)
    db['players'].update_one({'_id': ObjectId(id)}, {'$set': {'club': data['club']}})
    return {}


@app.delete('/players/<id>/')
def delete_player_by_id(id):
    db['players'].delete_one({'_id': ObjectId(id)})
    return {}


@app.route('/ping')
def ping():
    return 'pong'


if __name__ == '__main__':
    app.run()
