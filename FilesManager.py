from os import *
import fnmatch
import scipy.io.wavfile as wav
from python_speech_features import mfcc
import numpy as np

def importFiles(Path):
    tmp = {}
    digit = []
    type =  {}
    try:
        for x in listdir(Path):
            if not(path.isfile(Path+"/"+x)):
                importFiles(Path+"/"+x)
            if Path.__contains__("lost+found"):
                None
            else:
                if fnmatch.fnmatch(x, '*.wav') or fnmatch.fnmatch(x, '*.WAV'):
                    tmp[x] = {}
                    tmp[x]["path"] = Path+"/"+x
                    tmp[x]["name"] = x
                    tmp[x]["lektor"], tmp[x]["typ"], tmp[x]["znak"] = parseName(x)
                    rate, sig = wav.read(Path+"/"+x)
                    tmp[x]["mfcc"] = mfcc(sig, rate)
                    if tmp[x]["znak"]  not in digit:
                        digit.append(tmp[x]["znak"])
                    if tmp[x]["typ"] not in type:
                        type[tmp[x]["typ"]] = []
                    if tmp[x]["lektor"] not in type[tmp[x]["typ"]]:
                        type[tmp[x]["typ"]].append(tmp[x]["lektor"])

    except: print("permission error in " + Path)
    return tmp, digit, type


def parseName(str):
    return str[0:3], str[3:4], int(str[6])


def joinMfcc(files, excluded=None):
    dict = {}
    for i in files:
        if i != files:
            if files[i]["znak"] not in dict:
                dict[files[i]["znak"]]={}
            for k in range(0, len(np.transpose(files[i]["mfcc"]))):
                if k not in dict[files[i]["znak"]]:
                    dict[files[i]["znak"]][k] = []
                dict[files[i]["znak"]][k].append(np.transpose(files[i]["mfcc"])[k,:])


    for k in dict:
        for i in dict[k]:
            dict[k][i] = np.concatenate(dict[k][i], axis=None)

    return dict