#!/usr/bin/env bash
{ set +x; } 2>/dev/null 

IFS=
[[ -n ${#BASH_SOURCE[@]} ]] && [[ $((${#BASH_SOURCE[@]}*$SHLVL)) == 1 ]] && {
	{ set -x; cd "${BASH_SOURCE[0]%/*/*/*/*/*}"; { set +x; } 2>/dev/null; }
}

! [ -e setup.py ] && echo "ERROR: setup.py NOT EXISTS" && exit 0

# folder name must be same as original repo name
# wercker.com set folder to /pipeline/source/
IFS=.;set -- ${PWD##*/};IFS=
name="$1"

url="https://pypi.python.org/pypi/$name/json"

json=$(curl -s "$url") || exit 0 # no connection?
[[ "$json" != "{"* ]] && { # html 404
	echo "SKIP: pypi.python.org/pypi/$name NOT EXISTS"
	exit 0
}
# ( set -x; pip install -U "$name" )
# setuptools upgrade produce errors if installed from binary
# https://pip.pypa.io/en/stable/news/
pip="$(pip --version)" || exit
IFS=' ';set $pip;IFS=
version=$2
IFS=.;set $version;IFS=
major=$1;minor=$2;patch=$3

set -- pip install -U "$name"
# pip 6+, --no-use-wheel
[[ $major -ge 6 ]] && set -- pip install --no-use-wheel -U "$name"
# pip 7+, --no-binary
[[ $major -ge 7 ]] && set -- pip install --no-binary -U "$name"

( set -x; "$@" )

