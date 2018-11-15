from os import *
import fnmatch

def importFiles(Patch):
    try:
        for x in listdir(Patch):
            if not(path.isfile(Patch+"/"+x)):
                importFiles(Patch+"/"+x)
            if Patch.__contains__("lost+found"):
                None
            else:
                if fnmatch.fnmatch(x, '*.wav') or fnmatch.fnmatch(x, '*.WAV'):
                    print(x)
    except: print("permission error")
