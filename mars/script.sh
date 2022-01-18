#!/bin/bash
FILES=./originals/*
mkdir ./test
for f in $FILES
do 
    FILENAME=$(basename $f)
    y=${FILENAME%.png}
    z="$y.jpg"
    y="$y.tif"
    echo "processing $y"
    convert +append  "./originals/$FILENAME"  "./mask/$y" ./test/$z.jpg
done