#!/usr/bin/env bash
{ set +x; } 2>/dev/null

[[ ${#BASH_SOURCE[@]} != 1 ]] && exit 0 # skip if sourced

[[ ${BASH_SOURCE[0]} == /* ]] && {
	{ set -x; cd "${BASH_SOURCE[0]%/*/*}" || exit; { set +x; } 2>/dev/null; }
} || { 
	{ set -x; cd "$PWD"; { set +x; } 2>/dev/null; }
}
{ set -x; . "${BASH_SOURCE[0]%/*}"/export.sh; { set +x; } 2>/dev/null; }

# by default scripts installed to /usr/local/bin/ (must be writable)
# vitualenv install scripts to  writable path
# travis uses vitualenv, some CI not
[[ -z $VIRTUAL_ENV ]] && ! [ -w /usr/local/bin ] && {
	( set -x; sudo chmod -R 777 /usr/local/bin ) || exit
}

# 1) .Tests/requirements.txt, requirements.txt
for txt in .Tests/requirements.txt requirements.txt; do
	[ -f "$txt" ] && [ -s "$txt" ] && {
		( set -x; cat "$txt" ) || exit
		( set -x; pip --version ) || exit
		( set -x; pip install -r "$txt" ) || exit
	}
done
# 2) .Tests/requirements.sh
IFS=;requirements="$(set -x; . "${BASH_SOURCE[0]%/*}"/requirements.sh | tee)" || exit
[[ -n "$requirements" ]] && {
	while IFS= read r; do
		[[ -n $r ]] && { ( set -x; pip install "$r" ) || exit; }
	done <<< "$requirements"
}
[ -e setup.py ] && { # python package
	( set -x; python setup.py install )	|| exit
}
# coverage
[ -e .coverage ] && { ( set -x; rm .coverage ) || exit; }
# coverage run path/to/file.py
# coverage -m report
:
