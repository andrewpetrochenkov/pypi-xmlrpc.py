#!/usr/bin/env bash
{ set +x; } 2>/dev/null

bin="${BASH_SOURCE[0]%/*}"/bin
[ -d "$bin" ] && { # Tests/bin/
	PATH=$bin:"$PATH"
	{ set -x; export PATH="$PATH"; { set +x; } 2>/dev/null; }
}
