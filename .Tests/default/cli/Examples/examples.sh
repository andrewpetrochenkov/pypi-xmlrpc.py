#!/usr/bin/env bash
{ set +x; } 2>/dev/null

IFS=
[[ -n ${#BASH_SOURCE[@]} ]] && [[ $((${#BASH_SOURCE[@]}*$SHLVL)) == 1 ]] && {
	{ set -x; cd "${BASH_SOURCE[0]%/*/*/*/*/*}"; { set +x; } 2>/dev/null; }
}

! [ -d Examples ] && echo "SKIP: Examples/ NOT EXISTS" && exit 0

( set -x; test-scripts ./Examples )
