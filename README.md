# TagID
A simple ID3 audio tags viewer for Linux.

Most of what TagID does is displaying all audio tags (title, artist and album) in a directory using [eyeD3](https://github.com/nicfit/eyeD3).

It can be used both via command line and graphical interface.

## Install
First of all, clone download the latest [release](https://github.com/Marioexplo/TagID/releases/latest); then, after extracting the tarball, run the *install.sh* script. It is as easy as that.
## Build
If you prefer building from source, here's what you have to do:  
after cloning this repository,
```
git clone https://github.com/Marioexplo/TagID.git
cd TagID
```
build the virtual environment for Python; you'll need version 3.13
```
python3.13 -m venv .venv
source .venv/bin/activate
pip install pyside6 eyeD3 pyinstaller
```
Now you can use a script I made:
```
bash build.sh -p  # -p is for packaging into a tarball
```
With the new tarball you can proceed with the [installation](#install).
## License
TagID is licensed under the MIT license.  

This project uses [PySide6](https://doc.qt.io/qtforpython-6) for the graphical interface, [eyeD3](https://github.com/nicfit/eyeD3) to get the tags data and [PyInstaller](https://github.com/pyinstaller/pyinstaller) to build the app.  
 
The [Logo icon](install/Logo.png) is an artwork of [public domain](https://creativecommons.org/publicdomain/zero/1.0) by [paomedia](https://www.paomedia.com).