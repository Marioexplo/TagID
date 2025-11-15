#!/bin/bash
if [[ $EUID == 0 ]]; then
    echo This script should be run with normal privileges
    exit 1
fi
check_path() {
    if [[ -f $1 ]]; then
        echo It looks like $1 already exists.
        if [[ $(read -n 1 -p "Override it? ") =~ [Nn] ]]; then
            exit
        fi
        echo
    fi
}
runner=$(cd "$(dirname "$(realpath "$0")")/.." && pwd)/run.sh
desk=TagID.desktop
desk_path=$HOME/.local/share/applications/$desk
check_path /bin/tagid
check_path "$desk_path"
chmod +x "$runner"
echo Made executable
echo A password might be asked to link the executable in /bin
sudo ln -sf "$runner" /bin/tagid
echo Linked in /bin
desk=install/$desk
echo "Icon=$(pwd)/install/Logo.png" >> $desk
cp -f $desk "$desk_path"
echo Copied the .desktop in "$desk_path"
echo Installation completed!