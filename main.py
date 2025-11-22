import logging
logging.getLogger("eyed3.mp3.headers").setLevel(logging.ERROR)
del logging

from sys import argv
from runpy import run_module
run_module("modes." + ("gui" if len(argv) == 1 else "cli"))