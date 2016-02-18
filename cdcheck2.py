import os
bad = []
for path, dirs, files in os.walk("d:\\"):
  for file in files:
    fn = os.path.join(path, file)
    print fn
    f = open(fn, "rb")
    f.seek(0, 2)
    end = f.tell()



    for place in range(0, end+65535, 65536):


      print place

      try:
        f.read(65536)
      except:
        print "  Error"
        bad += fn
        break
print "Bad: "
for x in bad: print "  " + x



      
  
