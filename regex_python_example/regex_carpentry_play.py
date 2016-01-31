import re

def show_groups(pattern,text):
    m = re.search(pattern, text)
    if m is None:
        print "No match"
        return
    for i in range(1, 1 + len(m.groups())):
        print '%2d: %s' % (i, m.group(i))
        
show_groups('(.+)/(.+)/(.+)', 'Davidson/May 22, 2010/1721.3')