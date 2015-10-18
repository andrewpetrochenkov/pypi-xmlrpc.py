#!/usr/bin/env bash
{ set +x; } 2>/dev/null 

while [[ $PWD == /*/* ]] && ! [ -d Tests ]; do cd "${PWD%/*}"; done

! [ -d Tests ] && echo "ERROR: Tests/ NOT EXISTS" && exit 1
! [ -e setup.py ] && echo "ERROR: setup.py NOT EXISTS" && exit 1
examples="${PWD}"/examples
! [ -e "$examples" ] && echo "ERROR: $examples/ NOT EXISTS" && exit 1
example_files="$(find "$examples" -type f)"
[[ -z $example_files ]] && exit 0
while IFS= read f; do
	[[ $f == */.DS_Store ]] && continue
	[[ $f == */$'Icon\r' ]] && continue
	[[ $f == *.pyc ]] && continue
	# python shebang?
	[[ "$f" != *.py ]] && cat "$f" | head -1 | grep -q "python" || continue
	( set -x; python "$f" ) || exit $?
done <<< "$example_files";:
