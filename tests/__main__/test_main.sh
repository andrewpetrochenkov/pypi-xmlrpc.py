#!/usr/bin/env bash
{ set +x; } 2>/dev/null 

while [[ $PWD == /*/* ]] && ! [ -d Tests ]; do cd "${PWD%/*}"; done

! [ -d Tests ] && echo "ERROR: Tests/ NOT EXISTS" && exit 1
! [ -e setup.py ] && echo "ERROR: setup.py NOT EXISTS" && exit 1
IFS=
py_files="$(find . -type f -name "*.py")"
[[ -z $py_files ]]  && echo "SKIP: *.py NOT FOUND" && exit 0
while IFS= read f; do
	[[ -z $f ]] && continue
	[[ $f == */dist/* ]] && continue
	[[ $f == */examples/* ]] && continue
	[[ $f == */Examples/* ]] && continue
	[[ $f == */tests/* ]] && continue
	[[ $f == */Tests/* ]] && continue
	[[ $f == */setup.py/* ]] && continue
	[[ ${f##*/} == .* ]] && continue # skip .hidden
	# if __name__=="__main__": required
	grep -q "__name__" "$f" || continue
	grep -q "__main__" "$f" || continue
	( set -x; python "$f" ) || exit $?
done <<< "$py_files";:
