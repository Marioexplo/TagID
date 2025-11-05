# TagID
A simple ID3 audio tags viewer for Linux.

Most of what TagID does is displaying all audio tags (tile, artist and album) in a directory using [eyeD3](https://github.com/nicfit/eyeD3).

It can be used both via command line and graphical interface.

## Install
First of all clone this repository:
```
git clone github.com/Marioexplo/TagID
```
Make sure you've put it in the best directory for you as moving this after completing the installation will break the command links. To move the directory after the installation: move it and then reinstall TagID overriding the previous configuration.  
  
Now all you have to do is runnning the [install script](install/install.sh)
```
cd TagID/install
chmod +x install.sh
sudo ./install.sh
```
This will make [run.sh](run.sh) executable, link it in /bin to be available in the system and it will add a shortcut in your desktop.
## License
TagID is licensed under the MIT license.  
 
The [Logo icon](install/Logo.png) is an artwork of [public domain](https://creativecommons.org/publicdomain/zero/1.0) by [paomedia](https://www.paomedia.com)