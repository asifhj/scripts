#!/bin/bash
i=0;
for f in *.txt;
do
    set -- $f
    i=$((i+1));
    mv "$f" "2_7Cluster"$i".txt"
done
