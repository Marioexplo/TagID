# TagID
A simple ID3 audio tags viewer for Linux.

Most of what TagID does is displaying all audio tags (title, artist and album) in a directory using [eyeD3](https://github.com/nicfit/eyeD3).

It can be used both via command line and graphical interface.

## Install
First of all, download the latest [release](https://github.com/Marioexplo/TagID/releases/latest); then, after extracting the tarball, run the *install.sh* script. It is as easy as that.
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
Now you can use a script I made to build the app's directory:
```
bash build.sh
```
However, you can't proceed as in the [installation](#install) paragraph, instead you have to prepare some files like the logo image:
```
cp install/Logo.png dist/TagID
```
It is also better if you make a temporary folder and proceed there:
```
mkdir /temp # Substitute /temp with the path to that folder
mv dist/TagID /temp
cp -t /temp install/install.sh install/TagID.desktop
```
Finally, you can run the [install.sh](install/install.sh) in `/temp`.
## Uninstall
To uninstall the software, just run `tagid --uninstall` in the terminal.
## License
TagID is licensed under the MIT license.  

This project uses [PySide6](https://doc.qt.io/qtforpython-6) for the graphical interface, [eyeD3](https://github.com/nicfit/eyeD3) to get the tags data and [PyInstaller](https://github.com/pyinstaller/pyinstaller) to build the app.  
 
The [Logo icon](install/Logo.png) is an artwork of [public domain](https://creativecommons.org/publicdomain/zero/1.0) by [paomedia](https://www.paomedia.com).