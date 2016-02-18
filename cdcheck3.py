import os, sys
badfiles = []
error=0
def visit(arg, dir, files):
  for file in files:
     path = dir + "\\" + file
     if os.path.isfile(path):
       print path
       try: 
          x = open(path)
          while x.read(1000000): pass
       except:
         badfiles.append(path)
         print "  Failed."

z = "blah"
os.path.walk("f:\\", visit, z)
if len(badfiles) > 0: print "Bad: \n   " + "\n   ".join(badfiles)
