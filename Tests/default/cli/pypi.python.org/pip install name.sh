#!/usr/bin/env bash
{ set +x; } 2>/dev/null 

IFS=
[[ -n ${#BASH_SOURCE[@]} ]] && [[ $((${#BASH_SOURCE[@]}*$SHLVL)) == 1 ]] && {
	{ set -x; cd "${BASH_SOURCE[0]%/*/*/*/*/*}"; { set +x; } 2>/dev/null; }
}

! [ -e setup.py ] && echo "ERROR: setup.py NOT EXISTS" && exit 0

name="${PWD##*/}"
name="${name/.py/}"

url="https://pypi.python.org/pypi/$name/json"

json=$(curl -s "$url") || exit 0 # no connection?
[[ "$json" != "{"* ]] && { # html 404
	echo "SKIP: pypi.python.org/pypi/$name NOT EXISTS"
	exit 0
}
( set -x; pip install -U "$name" )
