#!/usr/bin/env bash
{ set +x; } 2>/dev/null 

IFS=
[[ -n ${#BASH_SOURCE[@]} ]] && [[ $((${#BASH_SOURCE[@]}*$SHLVL)) == 1 ]] && {
	{ set -x; cd "${BASH_SOURCE[0]%/*/*/*/*/*}"; { set +x; } 2>/dev/null; }
}

! [ -e setup.py ] && echo "ERROR: setup.py NOT EXISTS" && exit 0

! [ -d Tests ] && { echo "SKIP: Tests/ NOT EXISTS" && exit 0; }
[[ -z "$(ls Tests)" ]] && { echo "SKIP: Tests/ EMPTY" && exit 0; }

find="$(find "$PWD"/Tests -type f ! -regex '.*/\..*' | while read path; do
	cat "$path" | head -1 | grep -q python && echo "$path"
done)"
[[ -z "$find" ]] && { echo "SKIP: Tests/ 0 Python files" && exit 0; }
count="$(echo "$find" | wc -l | tr -d ' ')"
echo "Tests/ $count Python files"
while IFS= read f; do
	((i++))
	[[ $count != 1 ]] && echo "$i/$count ${f/$HOME/~}"
	( set -x; python "$f" ) || exit
done <<< "$find";:
