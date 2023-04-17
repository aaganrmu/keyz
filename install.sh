#!/bin/sh

DEVICE="/media/elmarw/CIRCUITPY/"


echo "cleaning"
remotefiles=$(ls $DEVICE)
for file in $remotefiles; do
    if [ "$file" = "keyz" ]; then
        echo "found keyz install, removing"
        $(rm -rf $DEVICE/keyz)
    fi
    if [ "$file" = "adafruit_hid" ]; then
        echo "found adafruit_hid install, removing"
        $(rm -rf $DEVICE/adafruit_hid)
    fi
    if [ "$file" = "boot.py" ]; then
        echo "found boot.py, removing"
        $(rm $DEVICE/boot.py)
    fi
    if [ "$file" = "code.py" ]; then
        echo "found code.py, removing"
        $(rm $DEVICE/code.py)
    fi
done

echo "installing"
cd source
echo "transfering boot.py"
$(cp boot.py $DEVICE)
echo "transfering code.py"
$(cp code.py $DEVICE)
echo "creating folders"
$(mkdir $DEVICE/keyz)
$(mkdir $DEVICE/adafruit_hid)
cd keyz
localfiles=$(ls)
for file in $localfiles; do
    echo "transfering keyz/$file"
    $(cp $file $DEVICE/keyz)
done

cd ../adafruit_hid
localfiles=$(ls)
for file in $localfiles; do
    echo "transfering adafruit_hid/$file"
    $(cp $file $DEVICE/adafruit_hid)
done

