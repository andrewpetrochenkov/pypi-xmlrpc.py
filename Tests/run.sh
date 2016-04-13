#!/usr/bin/env bash
{ set +x; } 2>/dev/null

[[ ${#BASH_SOURCE[@]} != 1 ]] && exit 0 # skip if sourced

[[ ${BASH_SOURCE[0]} == /* ]] && {
	{ set -x; cd "${BASH_SOURCE[0]%/*/*}" || exit; { set +x; } 2>/dev/null; }
} || { 
	{ set -x; cd "$PWD"; { set +x; } 2>/dev/null; }
}

# 1) .sh
find="$(find Tests -type f -name "*.sh" ! -regex '.*/\..*' | grep -v "${BASH_SOURCE[0]}")"
[[ -n $find ]] && {
	count="$(echo "$find" | wc -l | tr -d ' ')"
	echo "Tests/*.sh ($count)"

	[[ -n "$find" ]] && while IFS= read path; do
		( set -x; . "$path" ) || exit
	done <<< "$find";:
}
# 2) .py
find="$(find Tests -type f -name "*.py" ! -regex '.*/\..*')"
[[ -n $find ]] && {
	count="$(echo "$find" | wc -l | tr -d ' ')"
	echo "Tests/*.py ($count)"

	[[ -n "$find" ]] && while IFS= read path; do
		( set -x; python "$path" ) || exit
	done <<< "$find";:
}
# python3.2 coverage has syntax error
# '[[ $TRAVIS_PYTHON_VERSION != 3.2 ]] && coverage run --source=$(python setup.py --name) setup.py test;:'
#
:
