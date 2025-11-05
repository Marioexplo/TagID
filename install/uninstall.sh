#!/bin/bash
if [[ $EUID != 0 ]]; then
    echo You have to run this with sudo to work
    exit 1
fi
rm -f /bin/tagid
desk=TagID.desktop
rm -f $desk "$(eval echo "~$SUDO_USER")/.local/share/applications/$desk"
echo Removal completed