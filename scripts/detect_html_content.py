#!/usr/bin/env python

import glob
import subprocess
import re
import BeautifulSoup

out = subprocess.check_output(['find', '.', '-type', 'f']).split()
has_extension = re.compile(r'.*\.[^/]+$')
candidates = []

for l in out:
    l = l.strip()
    if l == '' or \
       l.startswith('./.git') or \
       '?' in l or \
       'Makefile' in l or \
       l.endswith('feed') or \
       l.startswith('./_site'):
        continue
    if not has_extension.match(l):
        candidates.append(l)

def guess_title(ls):
    title_line = [l for l in ls if l.startswith('<title>')]
    if len(title_line) == 0:
        return None
    return title_line[0].strip()[7:-19]

def guess_main_block(ls):
    def rough_guess():
        main_block_line = [(i, l.strip()) for (i, l) in enumerate(ls) if '"block-system-main"' in l]
        if len(main_block_line) == 0:
            return None
        l = main_block_line[0]
        div_content = ls[l[0] + 3].strip()
        if div_content != '<div class="content">':
            return None
        beginning_of_block = l[0] + 3
        for i in xrange(beginning_of_block+1, len(ls) - 2):
            if ls[i] == '</div>\n' and \
               ls[i+1] == '  </div>\n' and \
               ls[i+2] == '\t\t\t\t\t</div>\n':
                # Found end of block, now backtrack until you get an empty line
                for j in xrange(i, beginning_of_block, -1):
                    if ls[j].strip() == '':
                        # done!
                        return (beginning_of_block+2, j)
    r = rough_guess()
    if r is None:
        return r
    while ls[r[1]].strip() == '':
        r = (r[0], r[1] - 1)
    # make interval half-open
    print "Guessing main block is between lines %s and %s" % r
    return ls[r[0]:r[1]+1]

def guess_breadcrumbs(ls):
    candidates = [l for l in ls if l.strip().startswith('<div id="breadcrumbs">')]
    if len(candidates) == 0:
        return None
    soup = BeautifulSoup.BeautifulSoup(candidates[0].strip())
    list_items = soup.contents[0].findChildren(recursive=False)[0].findChildren(recursive=False)
    crumbs = []
    for item in list_items:
        anchors = item.findChildren("a", recursive=False)
        if len(anchors) == 0:
            continue
        t = anchors[0]
        url = dict(t.attrs).get('href', '')
        title = t.text
        crumbs.append((url, title))
    return crumbs
                  

for candidate in candidates:
    ls = open(candidate).readlines()
    if ls[0].strip() != '<!DOCTYPE html>':
        print "Skipping %s because it doesn't look like an HTML file" % candidate
        continue
    print "candidate: %s" % candidate
    title = guess_title(ls)
    main = guess_main_block(ls)
    crumbs = guess_breadcrumbs(ls)
    output = open("%s.html" % candidate, 'w')
    print >>output, "---"
    print >>output, "title: %s" % title
    print >>output, "layout: default"
    print >>output, "permalink: %s" % candidate[1:]
    print >>output, "breadcrumb:"
    for crumb in crumbs:
        print >>output, "  - ['%s', '%s']" % (crumb[1], crumb[0])
    print >>output, "---"
    print >>output, "\n".join(main)
    output.close()
    exit(0)
