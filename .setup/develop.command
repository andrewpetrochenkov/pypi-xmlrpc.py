#!/usr/bin/env bash
{ set +x; } 2>/dev/null

{ set -x; cd "${BASH_SOURCE[0]%/*/*}"; { set +x; } 2>/dev/null; }

( set -x; python setup.py -q develop )
# customize:
# 1) python wrapper:  ~/.bin/python
# ~/.bashrc: export PATH=~/.bin:$PATH
# 2) bash function: python_setup_develop
# ~/.bashrc: `export -f funcname` - export function to .command
