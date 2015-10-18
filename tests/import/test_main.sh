#!/usr/bin/env bash
{ set +x; } 2>/dev/null 

while [[ $PWD == /*/* ]] && ! [ -d Tests ]; do cd "${PWD%/*}"; done

! [ -d Tests ] && echo "ERROR: Tests/ NOT EXISTS" && exit 1
! [ -e setup.py ] && echo "ERROR: setup.py NOT EXISTS" && exit 1
IFS=
egg_info="$(find . -type d ! -regex '.*/\..*' -name "*.egg-info")"
if [[ -z $egg_info ]]; then
	echo "SKIP: *.egg-info NOT EXISTS (install first)" && exit 0
fi
while IFS= read path; do
	[[ -z $path ]] && continue
	basename="${path##*/}"
	name="${basename::${#basename}-9}"
	name="${name//-/_}"
	( set -x; python -c "import $name" ) || exit $?
	# raise AttributeError if invalid __all__
	( set -x; python -c "from $name import *" ) || exit $?
done <<< $egg_info;:
