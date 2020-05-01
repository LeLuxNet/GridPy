from lib import button


def _init():
    pass


def _quit():
    button.cleanup()


_init()

print("Wait for press")

button.buttonA.wait()

print("Finished")

_quit()
