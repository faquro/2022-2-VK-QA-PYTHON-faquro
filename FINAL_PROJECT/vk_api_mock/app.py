import threading

from flask import Flask, jsonify, request

app = Flask(__name__)

LOGIN_ID = {'qa_admin': 88005553535}

MOCK_HOST = '0.0.0.0'
MOCK_PORT = 5000


@app.route('/vk_id/<username>', methods=['GET'])
def get_user_vk_id(username):
    if username in LOGIN_ID:
        return {"vk_id": LOGIN_ID[username]}, 200
    else:
        return {}, 404


def run_mock():
    server = threading.Thread(target=app.run, kwargs={
        'host': MOCK_HOST,
        'port': MOCK_PORT
    })    
    server.start()
    return server


def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()
    else:
        raise RuntimeError('Not running with the Werkzeug Server')


@app.route('/shutdown')
def shutdown():
    shutdown_mock()
    return jsonify(f'Ok, exiting'), 200
