#!/bin/bash
error() {
    err=$?
    echo "$@"
    exit $err
}
cd "$(dirname "$(realpath "$0")")" || error There was an error when accessing the project\'s path
l=BuildLogs.txt
echo BUILD > $l
".venv/bin/pyinstaller" TagID.spec --noconfirm >>$l 2>&1 || error There was an error in the building process
if [[ -n $1 ]] && [[ $1 == -p || $1 == --package ]]; then
    i=install
    t=TagID
    I=$(pwd)/$i
    ln -s "$I/Logo.png" dist/$t
    {
        echo
        echo PACKAGE
        tar -hvcjf $t.tar.xz -C dist --strip-components=0 $t -C ../$i $i.sh $t.desktop
    } >>$l 2>&1 || error There was an error in the packaging process
fi