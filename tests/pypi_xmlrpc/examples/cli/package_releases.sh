#!/usr/bin/env bash
{ set +x; } 2>/dev/null

name="requests"
( set -x; python -m pypi_xmlrpc.package_releases "$name" )
