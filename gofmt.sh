#!/bin/bash

if [ "x$1" == "x" ]; then
    changed=$(git diff HEAD staging --name-only | grep '\.go$')
elif [ "x$1" == "xcached" ]; then
    changed=$(git diff --cached --name-only | grep '\.go$')
elif [ "x$1" == "xall" ]; then
    changed=$(git ls-files | grep '\.go$')
else
    changed="$1"
fi

for f in $changed; do
    goimports -w $f
    goimports-reviser -rm-unused -set-alias -format $f
done
