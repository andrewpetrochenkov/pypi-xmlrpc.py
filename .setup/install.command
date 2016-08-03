#!/usr/bin/env bash
{ set +x; } 2>/dev/null

{ set -x; cd "${BASH_SOURCE[0]%/*/*}"; { set +x; } 2>/dev/null; }

[ -f "requirements.txt" ] && {
	( set -x; pip install -r "requirements.txt" ) || exit
}

( set -x; python setup.py -q install )
# customize:
# 1) python wrapper:  ~/.bin/python
# ~/.bashrc: export PATH=~/.bin:$PATH
# 2) bash function: python_setup_install
# ~/.bashrc: `export -f funcname` - export function to .command
