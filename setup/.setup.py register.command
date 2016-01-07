#!/usr/bin/env bash
{ set +x; } 2>/dev/null

! [ -x "${BASH_SOURCE[0]}" ] && ( set -x; chmod +x "${BASH_SOURCE[0]}" )
! [ -t 1 ] && ( set -x; open "${BASH_SOURCE[0]}" ) && exit

{ set -x; cd "${BASH_SOURCE[0]%/*/*}"; { set +x; } 2>/dev/null; }

if [ -e ~/.command/trap.sh ]; then
	{ set -x;  . ~/.command/trap.sh || exit; { set +x; } 2>/dev/null; }
fi
if [ -e ~/.command/config.sh ]; then
	{ set -x;  . ~/.command/config.sh || exit; { set +x; } 2>/dev/null; }
fi

sp="$(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")"
[ -L "$sp" ] && sp="$(cd "${sp%/*}" && cd `readlink "${sp##*/}"` && echo $PWD)"
set python ./setup.py register; ! [ -w "$sp" ] && set sudo "$@"
( set -x; "$@" ) && { ! [ -w "$sp" ] && ( set -x; chmod -R 777 . ); };:
