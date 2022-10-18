##!/bin/sh

echo "Input old text to be replaced : "
read oldtext

echo " you entered $oldtext as old text"

echo "Input new text : "
read newtext
echo " you entered $newtext as new text"

echo "Input Full path file name : "
read filename

echo " you entered $filename as Full path file name"

sed -i "s/$oldtext/$newtext/g" $filename


