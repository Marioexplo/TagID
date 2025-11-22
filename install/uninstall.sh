#!/bin/bash
rm /bin/tagid
rm /usr/share/applications/TagID.desktop
rm -rf "$(dirname "$(realpath "$0")")"
echo Removal completed