#!/bin/sh

# for i in `find _site/archives _site/about_us _site/about-us _site/content -name "*.html"`; do
for i in `find _site -name "*.html"`; do
    mv $i `echo $i | sed s/.html$//`;
done

# Move straggling pages

# FILELIST="annual-meeting
# calendar
# executive-committee
# membership
# sitemap
# virtual-reality-technical-achievement-award
# visualization-career-award
# visualization-technical-achievement-award"

# for file in $FILELIST; do
#     mv _site/${file}.html _site/${file}
# done

