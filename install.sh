#!/bin/sh

DEVICE="/media/elmarw/KEYZ/"

echo "installing"
cd source
localfiles=$(ls)
for file in $localfiles; do
    echo "transfering $file"
    $(cp -r $file $DEVICE/)
done