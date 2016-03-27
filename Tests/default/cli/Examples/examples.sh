#!/usr/bin/env bash
{ set +x; } 2>/dev/null

IFS=
[[ -n ${#BASH_SOURCE[@]} ]] && [[ $((${#BASH_SOURCE[@]}*$SHLVL)) == 1 ]] && {
	{ set -x; cd "${BASH_SOURCE[0]%/*/*/*/*/*}"; { set +x; } 2>/dev/null; }
}

! [ -e setup.py ] && echo "ERROR: setup.py NOT EXISTS" && exit 0

! [ -d Examples ] && echo "SKIP: Examples/ NOT EXISTS" && exit 0

find="$(find "$PWD"/Examples -type f ! -name .DS_Store ! -name $'Icon\r' ! -name "*.pyc")"
[[ -z $find ]] && echo "SKIP: Examples/ 0 files" && exit 0

count="$(echo "$find" | wc -l | tr -d ' ')"
echo "Examples/ $count files"

find="$(echo "$find" | while read f; do
	# file output:
	# OS X: python script text, bash script text, ...
	# linux: python script, bash script
	[[ "${f##*/}" != .* ]] && file "$f" | grep -q "script" && echo "$f"
done)"
[[ -z $find ]] && echo "SKIP: Examples/ 0 script files" && exit 0

count="$(echo "$find" | wc -l | tr -d ' ')"
echo "Examples/ $count visible script files"

[[ -n "$find" ]] && while IFS= read f; do
	! [ -x "$f" ] && ( set -x; chmod +x "$f" )
	( set -x; "$f" ) || exit
done <<< "$find";:
