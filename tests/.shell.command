#!/usr/bin/env bash
{ set +x; } 2>/dev/null

! [ -x "${BASH_SOURCE[0]}" ] && ( set -x; chmod +x "${BASH_SOURCE[0]}" )

if [ -t 1 ] && [ -e ~/.command/config.sh ]; then
	{ set -x;  . ~/.command/config.sh; { set +x; } 2>/dev/null; }
fi

sh_files="$(find . -type f -name "test_*.sh")"
[[ -z $sh_files ]] && exit
while IFS= read sh; do
	( set -x; . "$sh" ) || exit $?
	echo
done <<< "$sh_files";:
