import os, shutil, string
badfiles = []
def walk(directory):
  if directory[-1:] == '\\': directory = directory[:-1]
  for e in [directory+'\\'+x for x in os.listdir(directory)]:
    if os.path.isfile(e):
      print e
      try:
        shutil.copyfile(e, "NUL")
      except:
        badfiles.append(e)
        print "Error reading "+e
    elif os.path.isdir(e):
      walk(e)
walk("d:\\")
if badfiles != []: print "bad files: \n   " + string.join(badfiles,"\n   ")



