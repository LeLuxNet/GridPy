import base64
import threading
from io import BytesIO

from flask import Flask, request

from config import *
from lib import button, led
from system import view, main

app = Flask(__name__)


@app.route('/view', methods=['GET'])
def get_view():
    return str(view.current())


@app.route('/view/<int:id>', methods=['POST'])
def set_view(id):
    view.next_view(id)
    press_button(0, 2)
    return ""


@app.route('/button/<int:id>/<int:type>', methods=['POST'])
def press_button(id, type):
    button.buttons[id].press(type)
    return ""


@app.route('/quit', methods=['DELETE'])
def quit():
    main.quit()
    return ""


@app.route('/image', methods=['POST'])
def show_img():
    set_view(0)
    body = request.data
    led.show_image(BytesIO(base64.b64decode(body)))
    return ""


@app.after_request
def apply_caching(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return response


def run():
    thread = threading.Thread(target=_start)
    thread.daemon = True
    thread.start()


def _start():
    app.run(host="0.0.0.0", port=80, debug=DEBUG, use_reloader=False)
