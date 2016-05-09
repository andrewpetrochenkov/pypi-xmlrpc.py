#!/usr/bin/env bash
{ set +x; } 2>/dev/null

! [ -e setup.py ] && echo "SKIP: setup.py not EXISTS" && exit 0
# todo: separate node, php, python
command="from distutils.sysconfig import get_python_lib; print(get_python_lib())"
sp="$(python -c "$command")" || exit
[[ -z $sp ]] && echo "ERROR: site-packages/ UNKNOWN" && exit 1

# 1) .Tests/requirements.txt, requirements.txt
for txt in .Tests/requirements.txt requirements.txt; do
	[ -f "$txt" ] && {
		! [ -s "$txt" ] && echo "SKIP: $txt EMPTY" && continue
		cat="$(cat "$txt" | sed '/^\s*$/d')" || exit
		[ -z "$cat" ] && echo "SKIP: $txt EMPTY" && continue
		( set -x; cat "$txt" ) || exit
		( set -x; pip --version ) || exit
		# site-packages must be writable or use sudo
		set -- pip install -r "$txt"
		! [ -w "$sp" ] && set -- sudo -H "$@"
		( set -x; "$@" ) || exit
	}
done
# 2) .Tests/requirements.sh
IFS=;requirements="$(set -x; . "${BASH_SOURCE[0]%/*/*}"/requirements.sh | tee)" || exit
[[ -n "$requirements" ]] && {
	[[ -n "$requirements" ]] && while IFS= read r; do
		[[ -n $r ]] && {
			set -- pip install "$r"
			! [ -w "$sp" ] && set -- sudo -H "$@"
			( set -x; "$@" ) || exit; 
		}
	done <<< "$requirements"
}
[ -e setup.py ] && { # python package
	set -- python setup.py install
	! [ -w "$sp" ] && set -- sudo -H "$@"
	( set -x; "$@" ) || exit
}
# coverage
[ -e .coverage ] && { ( set -x; rm .coverage ) || exit; }
# coverage run path/to/file.py
# coverage -m report
:


