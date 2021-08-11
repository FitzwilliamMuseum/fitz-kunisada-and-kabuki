import os
import sys
folder = '../_exhibition'
for filename in os.listdir(folder):
    infilename = os.path.join(folder,filename)
    if not os.path.isfile(infilename): continue
    oldbase = os.path.splitext(filename)
    newname = infilename.replace('.htm', '.md')
    output = os.rename(infilename, newname)
