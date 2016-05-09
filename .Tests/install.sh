#!/usr/bin/env bash
{ set +x; } 2>/dev/null

[[ ${#BASH_SOURCE[@]} != 1 ]] && exit 0 # skip if sourced

[[ ${BASH_SOURCE[0]} == /* ]] && {
	{ set -x; cd "${BASH_SOURCE[0]%/*/*}" || exit; { set +x; } 2>/dev/null; }
} || { 
	{ set -x; cd "$PWD"; { set +x; } 2>/dev/null; }
}
# `which -s` OS X only
[[ -z "$(which python)" ]] && echo "SKIP: python NOT INSTALLED" && exit 0


{ set -x; . "${BASH_SOURCE[0]%/*}"/export.sh || exit; { set +x; } 2>/dev/null; }

# by default scripts installed to /usr/local/bin/ (must be writable)
# vitualenv install scripts to  writable path
# travis uses vitualenv, some CI not
[[ -z $VIRTUAL_ENV ]] && ! [ -w /usr/local/bin ] && {
	( set -x; sudo chmod -R 777 /usr/local/bin ) || exit
}
( set -x; . "${BASH_SOURCE[0]%/*}"/install/python.sh ) || exit
