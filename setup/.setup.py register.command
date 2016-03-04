#!/usr/bin/env bash
{ set +x; } 2>/dev/null

! [ -x "${BASH_SOURCE[0]}" ] && ( set -x; chmod +x "${BASH_SOURCE[0]}" )
! [ -t 1 ] && ( set -x; open "${BASH_SOURCE[0]}" ) && exit

{ set -x; cd "${BASH_SOURCE[0]%/*/*}"; { set +x; } 2>/dev/null; }

tty -s && [ -e ~/.command.sh ] && {
	{ set -x;  . ~/.command.sh || exit; { set +x; } 2>/dev/null; }
}

sp="$(python -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")"
! [ -e "$sp" ] && echo "ERROR: $sp NOT EXISTS" && exit 1
[ -L "$sp" ] && sp="$(cd "${sp%/*}" && cd `readlink "${sp##*/}"` && echo $PWD)"
set python ./setup.py register; ! [ -w "$sp" ] && set sudo "$@"
( set -x; "$@" ) && { ! [ -w "$sp" ] && ( set -x; chmod -R 777 . ); };:
