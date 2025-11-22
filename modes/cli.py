from sys import argv, exit
from os import path, scandir
from eyed3 import load as load_tags, AudioFile

argv.pop(0)
argn = len(argv)
if argv[0] != "-h" and argv[0] != "--uninstall": argn -= 1
i = 0
all = False
name = True
title = True
artist = True
album = True
while i < argn:
    match argv[i]:
        case "-e":
            i += 1
            if i == argn:
                print("You have to specify the formats to exclude!")
                exit(1)
            exclude = argv[i].split(",")
        case "-a":
            all = True
        case "-i":
            i += 1
            if not (i == argn or argv[i + 1][0] == "-"):
                name = False
                title = False
                artist = False
                album = False
                for info in argv[i].split(","):
                    match info:
                        case "name":
                            name = True
                        case "title":
                            title = True
                        case "artist":
                            artist = True
                        case "album":
                            album = True
                        case _:
                            print(info + " is not a valid tag info")
                            exit(1)
        case "-h":
            print(open(path.dirname(path.realpath(__file__)) + "/Help.txt").read())
            exit()
        case "--uninstall":
            from subprocess import run
            exit(run(["sudo", "bash", path.dirname(path.realpath(__file__)) + "/uninstall.sh"]).returncode)
        case _:
            print(argv[i] + " is not a valid option")
            exit(1)
    i += 1
del i

dir = argv[-1]
if not path.isdir(dir):
    print(dir + " is not a valid directory")
    exit(1)
tags: list[AudioFile] = list()
for file in scandir(dir):
    if file.is_file():
        file = file.path
    else:
        continue
    audio = load_tags(file)
    if audio != None and audio.tag != None:
        tags.append(audio)
    elif all:
        tags.append(AudioFile(file))

names = list()
titles = list()
artists = list()
albums = list()
no_title = not title
no_artist = not artist
no_album = not album
def tag_exists(tag, checker)->tuple[str, bool]:
    checker = tag == None
    if checker:
        tag = ""
    return tag, checker
for tag in tags:
    if title:
        text = tag.tag.title
        text, no_title = tag_exists(text, no_title)
        titles.append(text)
    if artist:
        text = tag.tag.artist
        text, no_artist = tag_exists(text, no_artist)
        artists.append(text)
    if album:
        text = tag.tag.album
        text, no_album = tag_exists(text, no_album)
        albums.append(text)
    if all or not (no_title and no_artist and no_album):
        names.append(path.basename(tag.path))
    else:
        no_title = not title
        no_artist = not artist
        no_album = not album
del no_title, no_artist, no_album, tag_exists, tags

lists = list()
def to_dict(boo: bool, coll: list):
    if boo:
        lenghts = [0 if tag == None else len(tag) for tag in coll]
        lists.append((coll, max(max(lenghts), 15) if len(lenghts) != 0 else 15))
to_dict(name, names)
to_dict(title, titles)
to_dict(artist, artists)
to_dict(album, albums)
def incolumnate(word, width):
    return word + " " * (width - len(word)) + "\t"
printer = ""
headings = ["Name", "Title", "Artist", "Album"]
for i in range(4):
    word = f"\033[32m{headings[i]}\033[0m"
    printer += incolumnate(word, lists[i][1] + 9)
printer += "\n"
for i in range(len(names)):
    for list, width in lists:
        word = list[i]
        printer += incolumnate(word, width)
    printer += "\n"
print(printer)