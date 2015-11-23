#!/usr/bin/env bash
{ set +x; } 2>/dev/null

! [ -x "${BASH_SOURCE[0]}" ] && ( set -x; chmod +x "${BASH_SOURCE[0]}" )
! [ -t 1 ] && ( set -x; open "${BASH_SOURCE[0]}" ) && exit

if [ -t 1 ] && [ -e ~/.command/config.sh ]; then
	{ set -x;  . ~/.command/config.sh; { set +x; } 2>/dev/null; }
fi

{ set -x; cd "${BASH_SOURCE[0]%/*/*}" || exit $?; { set +x; } 2>/dev/null; }
! [ -e setup.py ] && echo "ERROR: setup.py NOT EXISTS" && exit 1

python_lib="$(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")"
log="$TMPDIR"$$
[ -e "$log" ] && rm -fr "$log"
set python ./setup.py sdist upload
! [ -w "$python_lib" ] && set sudo "$@"
( set -x; "$@" | tee "$log" ) || {
	# error: Upload failed (400): A file named "pkgname-z.y.z.tar.gz" already exists for pkgname-z.y.z. 
	# To fix problems with that file you should create a new release.
	grep -q "already exists" "$log" || exit 1 
}
! [ -w "$python_lib" ] && ( set -x; sudo chmod -R 777 . )

egg_info="$(find . -type d -name "*.egg-info")"
[[ -z $egg_info ]] && echo "ERROR: *.egg-info NOT EXISTS" && exit 1
function PKG-INFO.name() {
	IFS=:;set $(grep ^"Name: " "$1" | head -1);IFS=
	local name="${2// /}"
	local name="${name//-/_}"
	echo $name
}
name="$(PKG-INFO.name "$egg_info"/PKG-INFO)"
url="https://pypi.python.org/pypi/$name"
( set -x; open "$url" );:
