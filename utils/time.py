from time import sleep


def to_ms(time):
    return time.seconds * 1000 + time.microseconds // 1000


def sleep_ms(ms):
    sleep(ms / 1000)
