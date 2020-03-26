# import time
# import bottle
#
#
# @bottle.route('/words')
# def word_spammer():
#     words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
#     for word in words:
#         yield word
#         time.sleep(2)
#
#
# if __name__ == "__main__":
#     # bottle.run(server='gunicorn')
#     bottle.run(port=9999)

import time
import bottle


@bottle.route('/words')
def word_spammer():
    bottle.response.content_type = "text/event-stream"
    bottle.response.cache_control = "no-cache"
    bottle.response.headers['Access-Control-Allow-Origin'] = '*'

    words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven']
    for word in words:
        yield 'data: %s\n\n' % word
        time.sleep(2)


if __name__ == "__main__":
    bottle.run(server='gunicorn')

# terminal
# sudo snap install http
# http --stream localhost:8080/words
