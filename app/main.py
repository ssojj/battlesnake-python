import bottle
import os
import random

def aStar (point, data):

@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.post('/start')
def start():
    data = bottle.request.json
    game_id = data['game_id']
    board_width = data['width']
    board_height = data['height']

    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    # TODO: Do things with data

    return {
        'color': '#990099',
        'taunt': '{} ({}x{})'.format(game_id, board_width, board_height),
        'head_type': 'fang',
		'tail_type': 'regular',
        'name': 'battlesnake-python'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json

    # TODO: Do things with data
    directions = ['up', 'down', 'left', 'right']
    final_dir = 2
    #if len(data['food'][0][0]) == 5:
    if len(data['food']) == 5:
        final_dir = 1

    

    return {
        #'move': random.choice(directions),
		'move': directions[final_dir],
        'taunt': 'WELP!'
    }


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
