import logging

def disable():
    logging.getLogger("eyed3.mp3.headers").setLevel(logging.ERROR)