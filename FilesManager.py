from os import *
import fnmatch
import scipy.io.wavfile as wav
from python_speech_features import mfcc, fbank, logfbank, ssc
from python_speech_features import delta
import numpy as np


def importFiles(Path, winlen=0.025, winstep=0.01, numcep=13, nfilt=26, nfft=512, lowfreq=0, highfreq=None, preemph=0.97, ceplifter=22, N=2, delta_window = 10, feature_type = "ssc", only_mfcc = True):
    tmp = {}
    digit = []
    type = {}
    try:
        for x in listdir(Path):
            if not (path.isfile(Path + "/" + x)):
                importFiles(Path + "/" + x)
            if Path.__contains__("lost+found"):
                None
            else:
                if only_mfcc:
                    if fnmatch.fnmatch(x, '*.wav') or fnmatch.fnmatch(x, '*.WAV'):
                        tmp[x] = {}
                        rate, sig = wav.read(Path + "/" + x)
                        if feature_type == "logfbank":
                            data_mfcc2 = logfbank(sig, rate, winlen=winlen, winstep=winstep, nfilt=nfilt,  nfft=nfft, lowfreq=lowfreq, highfreq=highfreq, preemph=preemph)
                        elif feature_type == "ssc":
                            data_mfcc2 = ssc(sig, rate, winlen=winlen, winstep=winstep, nfilt=nfilt,  nfft=nfft, lowfreq=lowfreq, highfreq=highfreq, preemph=preemph)
                        else:
                            data_mfcc2 = mfcc(sig, rate, winlen=winlen, winstep=winstep, numcep=numcep, nfilt=nfilt,  nfft=nfft, lowfreq=lowfreq, highfreq=highfreq, preemph=preemph, ceplifter=ceplifter)
                        for _ in range(N):
                            data_mfcc2 += delta(data_mfcc2, delta_window)


                        tmp[x]["mfcc"] = data_mfcc2

                else:
                    if fnmatch.fnmatch(x, '*.wav') or fnmatch.fnmatch(x, '*.WAV'):
                        tmp[x] = {}
                        tmp[x]["path"] = Path + "/" + x
                        tmp[x]["name"] = x
                        tmp[x]["lektor"], tmp[x]["typ"], tmp[x]["znak"] = parseName(x)
                        rate, sig = wav.read(Path + "/" + x)
                        data_mfcc = None

                        if feature_type == "logfbank":
                            data_mfcc = logfbank(sig, rate, winlen=winlen, winstep=winstep, nfilt=nfilt,  nfft=nfft, lowfreq=lowfreq, highfreq=highfreq, preemph=preemph)
                        elif feature_type == "ssc":
                            data_mfcc = ssc(sig, rate, winlen=winlen, winstep=winstep, nfilt=nfilt,  nfft=nfft, lowfreq=lowfreq, highfreq=highfreq, preemph=preemph)
                        else:
                            data_mfcc = mfcc(sig, rate, winlen=winlen, winstep=winstep, numcep=numcep, nfilt=nfilt,nfft=nfft, lowfreq=lowfreq, highfreq=highfreq, preemph=preemph,ceplifter=ceplifter)

                        for _ in range(N):
                            data_mfcc += delta(data_mfcc, delta_window)

                        tmp[x]["mfcc"] = data_mfcc

                        if tmp[x]["znak"] not in digit:
                            digit.append(tmp[x]["znak"])
                        if tmp[x]["typ"] not in type:
                            type[tmp[x]["typ"]] = []
                        if tmp[x]["lektor"] not in type[tmp[x]["typ"]]:
                            type[tmp[x]["typ"]].append(tmp[x]["lektor"])

    except:
        print("permission error in " + Path)
    if not only_mfcc:
        return tmp, digit, type
    else:
        return tmp


def parseName(str):
    return str[0:3], str[3:4], int(str[6])


def joinMfcc(files, excluded=None):
    dict = {}
    if excluded == None:
        for i in files:
            if i != files:
                if files[i]["znak"] not in dict:

                    dict[files[i]["znak"]] = files[i]["mfcc"]
                else:
                    dict[files[i]["znak"]] = np.concatenate((dict[files[i]["znak"]], files[i]["mfcc"]))
    else:
        for i in files:
            if i != files:
                if files[i]["lektor"] not in excluded:
                    if files[i]["znak"] not in dict:
                        dict[files[i]["znak"]] = files[i]["mfcc"]
                    else:
                        dict[files[i]["znak"]] = np.concatenate((dict[files[i]["znak"]], files[i]["mfcc"]))

    return dict
