#!/bin/sh

# for i in `find _site/year/{2016,2017} -name "*.html"`; do
#     mv $i `echo $i | sed s/.html$//`;
# done

# Move straggling pages

FILELIST="annual-meeting
executive-committee
calendar
membership"

for file in $FILELIST; do
    mv _site/${file}.html _site/${file}
done

