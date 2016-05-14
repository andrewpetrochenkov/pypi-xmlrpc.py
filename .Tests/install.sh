#!/usr/bin/env bash
{ set +x; } 2>/dev/null

( set -x; . "${BASH_SOURCE[0]%/*}"/clone.sh ) || exit
( set -x; $SHELL ~/.Tests/install.sh )
