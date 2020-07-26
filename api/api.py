import base64
import threading
from io import BytesIO
from urllib.request import urlopen

from config import *
from flask import Flask, request
from lib import button, led, char
from system import view, init

app = Flask(__name__)


@app.route('/view', methods=['GET'])
def get_view():
    return str(view.current())


@app.route('/view/<int:id>', methods=['POST'])
def set_view(id):
    view.next_view(id)
    press_button(0, 2)
    return ""


def free_view():
    view.next_view(0)
    press_button(0, 2)
    while view.current() != -1:
        pass


@app.route('/button/<int:id>/<int:type>', methods=['POST'])
def press_button(id, type):
    button.buttons[id].press(type)
    return ""


@app.route('/quit', methods=['DELETE'])
def quit():
    init.stop()
    return ""


@app.route('/image', methods=['POST'])
def show_img():
    free_view()
    body = request.data
    body_str = request.data.decode("utf-8")
    if body_str.startswith("https://"):
        led.show_image(urlopen(body_str))
    else:
        led.show_image(BytesIO(base64.b64decode(body)))
    return ""


@app.route('/text', methods=['POST'])
def show_text():
    free_view()
    led.clear()
    char.gliding_text(request.data.decode("utf-8"), (DISPLAY_ROWS - 5) // 2, fade_in=True, fade_out=True)
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
