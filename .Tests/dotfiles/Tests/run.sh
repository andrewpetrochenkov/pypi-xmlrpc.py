#!/usr/bin/env bash
{ set +x; } 2>/dev/null

[[ ${#BASH_SOURCE[@]} != 1 ]] && exit 0 # skip if sourced

[[ ${BASH_SOURCE[0]} == /* ]] && {
	{ set -x; cd "${BASH_SOURCE[0]%/*/*}" || exit; { set +x; } 2>/dev/null; }
} || { 
	{ set -x; cd "$PWD"; { set +x; } 2>/dev/null; }
}
{ set -x; . "${BASH_SOURCE[0]%/*}"/export.sh; { set +x; } 2>/dev/null; }

( set -x; test-scripts .Tests/default ) || exit

! [ -d Tests ] && echo "SKIP: Tests/ NOT EXISTS" || {
	( set -x; test-scripts Tests ) || exit
}
! [ -e .coverage ] && echo "SKIP: .coverage NOT EXISTS" || {
	[[ $TRAVIS == true ]] && ( set -x; codecov ) # travis
	# codecov --token=<token> # other ci
}
:
