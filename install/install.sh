#!/bin/bash
echo Starting installation...
error() {
    echo "$@"
    exit 1
}
[[ $EUID == 0 ]] && error This script should be run with normal privileges

ask() {
    read -n 1 -p "$1? (Y/n) " ans
    echo
    [[ $ans =~ [Yy] ]]
    return $?
}
no_path() { # if path exists and answer is no, exit
    if [[ -e $1 ]]; then
        echo "$1 already exists" >/dev/tty
        ! ask "$2" && exit
        return 0
    fi
    return 1
}
cd "$(dirname "$(realpath "$0")")" || error There was an error when locating this script\'s path

echo You may be asked your password to access the necessary privileges

n=TagID
shr=/usr/share
d=$shr/$n
if no_path $d "Remove it"; then [[ -d $d ]] && sudo rm -rf $d || error $n was expected to be a directory; fi
sudo mv $n $shr || error There was an error while transfering the app\'s files
echo Files extracted

desk=$n.desktop
o_desk=$(pwd)/$desk
cd $d || error There was an error when locating the app directory

b=/bin/tagid
if [[ -e $b ]]; then
    echo A command named \'tagid\' was found
    ! ask "Override it" && exit
    sudo rm $b || error There was an error when overriding $b
fi
sudo ln -sf "$(pwd)/$n" $b

app=$shr/applications
echo "Icon=$(pwd)/Logo.png" >> "$o_desk"
new_desk=$app/$desk
if no_path $new_desk "Override it"; then [[ -f $n ]] && sudo rm $new_desk || error $desk was expected to be a file; fi
sudo mv "$o_desk" $app

echo $n is now available on the whole system, both via console and graphical interface