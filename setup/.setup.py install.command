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
if [ -w "$python_lib" ]; then
	( set -x; python ./setup.py install ) || exit $?
	( set -x; chmod -R 777 . )
else
	( set -x; sudo python ./setup.py install ) || exit $?
	( set -x; sudo chmod -R 777 . )
fi
