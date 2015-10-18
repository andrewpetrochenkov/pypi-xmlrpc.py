#!/usr/bin/env bash
{ set +x; } 2>/dev/null

! [ -x "${BASH_SOURCE[0]}" ] && ( set -x; chmod +x "${BASH_SOURCE[0]}" )

if [ -t 1 ] && [ -e ~/.command/config.sh ]; then
	{ set -x;  . ~/.command/config.sh; { set +x; } 2>/dev/null; }
fi

{ set -x; cd "${BASH_SOURCE[0]%/*/*}" || exit $?; { set +x; } 2>/dev/null; }
! [ -e setup.py ] && echo "ERROR: setup.py NOT EXISTS" && exit 1

IFS=
set "$(find . -type f -name PKG-INFO)"
if [[ -n $1 ]] && [[ $1 != *"
"* ]]; then
	l="$(grep "Name: " "$1" | head -1)" || exit $?
	IFS=:;set $l;IFS=
	name=${2/ /}
else
	name="$(python setup.py --name)" || exit $?
fi
( set -x; open https://pypi.python.org/"$name" )
