#!/usr/bin/env bash
{ set +x; } 2>/dev/null
# standalone .command version of files.cp.sh.dir (not optimized)

! [ -x "${BASH_SOURCE[0]}" ] && ( set -x; chmod +x "${BASH_SOURCE[0]}" )
#! [ -t 1 ] && ( set -x; open "${BASH_SOURCE[0]}" ) && exit

[[ ${BASH_SOURCE[0]} == /* ]] && {
    { set -x; cd "${BASH_SOURCE[0]%/*/*}"; { set +x; } 2>/dev/null; }
}

tty -s && [ -e ~/.command.sh ] && {
    { set -x;  . ~/.command.sh || exit; { set +x; } 2>/dev/null; }
}


IFS=
NL=$'\n'
dirname="$(cd "${BASH_SOURCE[0]%/*}";echo ${PWD##*/})"
files=
changes=false
touch=

if [[ ${BASH_SOURCE[0]%/*} != *files ]]; then
    echo "ERROR: ${BASH_SOURCE[0]##*/} must be executed only from 
dotfiles/, publicfiles/, rootfiles/"; exit 1
fi
sources="$(find "$PWD"/"$dirname" -type f ! -name .DS_Store ! -name $'Icon\r' ! -path "${BASH_SOURCE[0]}" | sort)"
[[ -z $sources ]] && echo "SKIP: 0 files" && exit 0

while IFS= read src; do
    r="${src:${#PWD}+${#dirname}+2}" # relpath
    [[ $src == */dotfiles/* ]] && {
        [[ $r != */* ]] && [[ $r != .* ]] && continue # skip dotfiles/file 
        [[ "$r" != .* ]] && r=."$r"
        dst=~/"$r"
    }
    [[ $src == */publicfiles/* ]] && {
        [[ $r != */* ]] && continue; dst=~/"$r"
    }
    [[ $src == */rootfiles/* ]] && {
        [[ $r != */* ]] && continue
        dst=/"$r"
    }
    files="$files${NL}$dst"
    ! [ "$src" -nt "$dst" ] && continue
    
    changes=true
    ! [ -e "${dst%/*}" ] && { ( set -x; mkdir -p "${dst%/*}" ) || exit; } # mkdir

    # cp
    ( set -x; cp "$src" "$dst" ) || exit

    # touch parent folders (skip if folder was created)
    while [[ "${dst%/*}" != "$HOME" ]]; do
        if [ "$src" -nt "${dst%/*}" ]; then
            if [[ "$touch" != *"${NL}${dst%/*}${NL}"*  ]]; then
                touch="${NL}$touch${NL}${dst%/*}${NL}"
            fi
        fi
        dst="${dst%/*}"
    done
done <<< "$sources"
[[ $changes == false ]] && echo "up-to-date" && exit 0

echo "$files" | grep -v ^$ | sed "s/${HOME//\//\\/}/\~/g" >> ~/.files.txt || exit
echo "$sources" | grep -v ^$ | sed "s/${HOME//\//\\/}/\~/g" >> ~/.sources.txt || exit

[[ -n "$touch" ]] && {
    set --;while IFS= read path; do
        [[ -n $path ]] && set "$@" "$path"
    done <<< "$touch"
    echo; ( set -x; touch "$@" ) || exit
}
# ~/.files.txt
count="$(wc -l < ~/.files.txt | tr -d ' ')"
size="$(du -smh ~/.files.txt | awk '{print $1}')"
echo "~/.files.txt ($count), $size"
# ~/.sources.txt
count="$(wc -l < ~/.sources.txt | tr -d ' ')"
size="$(du -smh ~/.sources.txt | awk '{print $1}')"
echo "~/.sources.txt ($count), $size"
( set -x; sort -u ~/.files.txt -o ~/.files.txt ) || exit
( set -x; sort -u ~/.sources.txt -o ~/.sources.txt ) || exit

[ -e ~/.files.sh ] && { ( set -x; $SHELL ~/.files.sh ) || exit; };:

