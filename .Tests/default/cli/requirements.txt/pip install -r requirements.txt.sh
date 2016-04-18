#!/usr/bin/env bash
{ set +x; } 2>/dev/null 

IFS=
[[ -n ${#BASH_SOURCE[@]} ]] && [[ $((${#BASH_SOURCE[@]}*$SHLVL)) == 1 ]] && {
	{ set -x; cd "${BASH_SOURCE[0]%/*/*/*/*/*}"; { set +x; } 2>/dev/null; }
}

! [ -e setup.py ] && echo "ERROR: setup.py NOT EXISTS" && exit 0
! [ -e requirements.txt ] && echo "SKIP: requirements.txt NOT EXISTS" && exit 0
! [ -s requirements.txt ] && echo "SKIP: requirements.txt EMPTY" && exit 0

( set -x; pip install -r requirements.txt )
