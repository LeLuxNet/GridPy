import threading

from flask import Flask

from config import *
from lib import button
from system import view, main

app = Flask(__name__)


@app.route('/view', methods=['GET'])
def get_view():
    return str(view.current())


@app.route('/view/<int:id>', methods=['POST'])
def set_view(id):
    view.next_view(id)
    return ""


@app.route('/button/<int:id>/<int:type>', methods=['POST'])
def press_button(id, type):
    button.buttons[id].press(type)
    return ""


@app.route('/quit', methods=['DELETE'])
def quit():
    main.quit()
    return ""


def run():
    thread = threading.Thread(target=_start)
    thread.daemon = True
    thread.start()


def _start():
    app.run(host="0.0.0.0", port=80, debug=DEBUG, use_reloader=False)
