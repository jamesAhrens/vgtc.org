#!/bin/sh

# for i in `find _site/year/{2016,2017} -name "*.html"`; do
#     mv $i `echo $i | sed s/.html$//`;
# done

# Move straggling pages

FILELIST="annual-meeting
calendar
executive-committee
membership
sitemap
virtual-reality-technical-achievement-award
visualization-career-award"

for file in $FILELIST; do
    mv _site/${file}.html _site/${file}
done

