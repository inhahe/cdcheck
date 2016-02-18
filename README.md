This is a python program that checks the integrity of all the files on a CD/DVD/BR/whatever. 

There are three versions of the program here that do more-or-less the same thing. The best version is probably cdcheck.py, it works by calling an OS function to copy the files to "NUL". For linux I guess you'd have to change "NUL" to "dev/nul" or something (I don't know a whole lot about linux) and also change one or two \\'s to /'s and/or use os.path.join instead.

The other versions just open the files and read them and throw away the data. I think cdcheck3.py is a later version over cdcheck2.py. 

One improvement that would be nice for someone to push would be the ability to take the drive letter/directory as a command-line parameter. Currently they're just hard-coded to use whatever drive letters that suited my purposes at the times of writing.

