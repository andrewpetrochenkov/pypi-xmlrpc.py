#!/usr/bin/env bash
{ set +x; } 2>/dev/null

! [ -x "${BASH_SOURCE[0]}" ] && ( set -x; chmod +x "${BASH_SOURCE[0]}" )
! [ -t 1 ] && ( set -x; open "${BASH_SOURCE[0]}" ) && exit

{ set -x; cd "${BASH_SOURCE[0]%/*/*}"; { set +x; } 2>/dev/null; }

tty -s && [ -e ~/.command.sh ] && {
	{ set -x;  . ~/.command.sh || exit; { set +x; } 2>/dev/null; }
}

( set -x; python setup.py register )
# customize:
# 1) python wrapper:  ~/.bin/python
# ~/.bashrc: export PATH=~/.bin:$PATH
# 2) bash function: python_setup_register
# ~/.bashrc: `export -f funcname` - export function to .command
