#!/usr/bin/env bash
{ set +x; } 2>/dev/null

[ -e ~/.Tests ] && echo "SKIP: ~/.Tests/ EXISTS, continue" && exit 0
echo "DEBUG: ~/.Tests/ NOT EXISTS, continue"
[[ -z "$TESTS_URL" ]] && {
	echo "DEBUG: \$TESTS_URL NOT DEFINED"
	txt="${BASH_SOURCE[0]%/*}/url.txt"
	TESTS_URL="$(set -x; cat "$txt")" || exit
}

( set -x; git clone --depth 1 "$TESTS_URL" ~/.Tests ) || exit
