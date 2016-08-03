#!/usr/bin/env bash
{ set +x; } 2>/dev/null

{ set -x; cd "${BASH_SOURCE[0]%/*/*/*}"; { set +x; } 2>/dev/null; }

! [ -e setup.py ] && echo "ERROR: setup.py NOT EXISTS" && exit 1

name="$(python setup.py --name)" || exit
url="https://testpypi.python.org/pypi/$name"
( set -x; open "$url" )
