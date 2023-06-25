#!/bin/sh

DEVICE="/media/elmarw/KEYZ/"

echo "cleaning"
remotefiles=$(ls $DEVICE)
for file in $remotefiles; do
    if [ "$file" = "keyz" ]; then
        echo "found keyz install, removing"
        $(rm -rf $DEVICE/keyz)
    fi
done

echo "installing"
cd source
echo "transfering boot.py"
$(cp boot.py $DEVICE)
echo "transfering code.py"
$(cp code.py $DEVICE)
echo "transfering config"
$(cp config $DEVICE)
echo "creating folders"
$(mkdir $DEVICE/keyz)
cd keyz
localfiles=$(ls)
for file in $localfiles; do
    echo "transfering keyz/$file"
    $(cp $file $DEVICE/keyz)
done