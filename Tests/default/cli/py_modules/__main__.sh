#!/usr/bin/env bash
{ set +x; } 2>/dev/null 

IFS=
[[ -n ${#BASH_SOURCE[@]} ]] && [[ $((${#BASH_SOURCE[@]}*$SHLVL)) == 1 ]] && {
	{ set -x; cd "${BASH_SOURCE[0]%/*/*/*/*/*}"; { set +x; } 2>/dev/null; }
}

! [ -e setup.py ] && echo "ERROR: setup.py NOT EXISTS" && exit 0

path="$PWD"/py_modules
! [ -d "$path" ] && echo "SKIP: $path NOT EXISTS" && exit 0

find="$(find "$path" -type f -name "*.py")"
[[ -z $find ]]  && echo "SKIP: $path/*.py NOT FOUND" && exit 0

while IFS= read f; do
	# if __name__=="__main__": required
	grep -q "__name__" "$f" || continue
	grep -q "__main__" "$f" || continue
	( set -x; python "$f" ) || exit
done <<< "$find";:
