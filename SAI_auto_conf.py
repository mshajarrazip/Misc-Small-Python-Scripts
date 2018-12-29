# -*- coding: utf-8 -*-
"""
Creates .conf entries for brushes and textures.
"""

from os import listdir
from os.path import join


# TODO: Specify the sources of you brushes/textures 
bfsrc = ["blotmap", "elemap"]
btexsrc = ["brushtex"]
ptexsrc = ["papertex"]

# Builts the list of brushes and textures
bfset = []
for src in bfsrc:
    bfset.append(listdir(src))
btexset = []
for src in btexsrc:
    btexset.extend(listdir(src))
ptexset = []
for src in ptexsrc:
    ptexset.extend(listdir(src))

# Reads config file and lists settings that are already there
bfconf = "brushform.conf"
btexconf = "brushtex.conf"
ptexconf = "papertex.conf"

# append settings to .conf files
with open(bfconf) as f:
    content = f.readlines()
bfconflines = [x.strip() for x in content]
bfsettings = ["1,%s" % join(bfsrc[0], x) for x in bfset[0]]
bfsettings.extend(["2,%s" % join(bfsrc[1], x) for x in bfset[1]])
with open(bfconf, 'a') as f:
    if (len(bfconflines) > 0):
        f.write('\n')
    for setting in bfsettings:
        if not setting in bfconflines:
            f.write("%s\n" % setting)

with open(btexconf) as f:
    content = f.readlines()
btexconflines = [x.strip() for x in content]
btexsettings = ["1,%s" % join(btexsrc[0], x) for x in btexset]
with open(btexconf, 'a') as f:
    if (len(btexconflines) > 0):
        f.write('\n')
    for setting in btexsettings:
        if not setting in btexconflines:
            f.write("%s\n" % setting)
            
with open(ptexconf) as f:
    content = f.readlines()
ptexconflines = [x.strip() for x in content]
ptexsettings = ["1,%s" % join(ptexsrc[0], x) for x in ptexset]
with open(ptexconf, 'a') as f:
    if (len(ptexconflines) > 0):
        f.write('\n')
    for setting in ptexsettings:
        if not setting in ptexconflines:
            f.write("%s\n" % setting)
