#!/usr/bin/env bash
{ set +x; } 2>/dev/null

user="kennethreitz"
( set -x; python -m pypi_xmlrpc.user_packages "$user" )
