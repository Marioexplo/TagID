#!/bin/bash
cd "$(dirname "$(realpath "$0")")"
if [[ -n $1 ]]; then
    ".venv/bin/python" "cli.py" "$@"
else
    setsid ".venv/bin/python" "gui.py" >/dev/null 2>&1 &
fi