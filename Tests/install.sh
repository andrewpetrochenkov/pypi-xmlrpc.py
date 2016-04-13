#!/usr/bin/env bash
{ set +x; } 2>/dev/null

[[ ${#BASH_SOURCE[@]} != 1 ]] && exit 0 # skip if sourced

[[ ${BASH_SOURCE[0]} == /* ]] && {
	{ set -x; cd "${BASH_SOURCE[0]%/*/*}" || exit; { set +x; } 2>/dev/null; }
} || { 
	{ set -x; cd "$PWD"; { set +x; } 2>/dev/null; }
}

[ -f requirements.txt ] && [ -s requirements.txt ] && {
	( set -x; cat requirements.txt ) || exit
	( set -x; pip --version ) || exit
	( set -x; pip install -r requirements.txt ) || exit
}
( set -x; python setup.py install )
