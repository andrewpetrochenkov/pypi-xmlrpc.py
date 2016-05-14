#!/usr/bin/env bash
{ set +x; } 2>/dev/null

origin="git://github.com/russianidiot/curl-status.sh.cli.git"
# git@github.com:owner/repo.git
[[ $origin == "git@github.com:"* ]] && {
	IFS=':';set $origin;IFS=
	fullname="${2::${#2}-4}"
	IFS='/';set $fullname;IFS=
	owner="$1";repo="$2"
}
# git://github.com/owner/repo.git
# https://github.com/owner/repo.git
[[ $origin == *"://github.com/"* ]] && {
	IFS='/';set $origin;IFS=
	owner="$4";repo="${5::${#5}-4}"
}
[[ -z $owner ]] && { return 0 2> /dev/null; exit 0; }
unset IFS
for url in "https://github.com/$owner/.Tests.git" "https://github.com/$owner-dotfiles/.Tests.git"; do
	( set -x; git ls-remote "$url" HEAD &> /dev/null ) || continue
	TESTS_URL="$url"
done
:
