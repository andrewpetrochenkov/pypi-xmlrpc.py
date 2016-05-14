#!/usr/bin/env bash
{ set +x; } 2>/dev/null

[ -e ~/.Tests ] && echo "SKIP: ~/.Tests/ EXISTS, continue" && exit 0
echo "DEBUG: ~/.Tests/ NOT EXISTS, continue"
[[ -z "$TESTS_URL" ]] && {
	echo "DEBUG: \$TESTS_URL NOT DEFINED"
	origin="$(git config remote.origin.url)" || exit
	[[ -z $origin ]] && {
		( set -x; git config remote.origin.url )
		echo "ERROR: remote UNKNOWN"
		exit 1
	}

	clone="${BASH_SOURCE[0]%/*}"/clone
	[[ "$origin" == *"github.com:"* ]] || [[ "$origin" == *"github.com/"* ]] && {
		{ set -x; . "$clone"/github.sh || exit; { set +x; } 2>/dev/null; }
	}
	# todo: bitbucket, gitlab, etc
	[[ -z "$TESTS_URL" ]] && {
		echo "$origin NOT SUPPORTED"
		{ set -x; . "${BASH_SOURCE[0]%/*}"/config.sh; { set +x; } 2>/dev/null; }
	}
}

( set -x; git clone --depth 1 "$TESTS_URL" ~/.Tests ) || exit
