from sklearn.mixture import GaussianMixture
import numpy as np
import scipy.io.wavfile as wav
from python_speech_features import mfcc


def myGmm(mfcc):
    model_gmm = {}
    for i in mfcc:
        gauss = GaussianMixture(n_components=13)
        model_gmm[i] = gauss.fit(mfcc[i])
        print("another one is finished")

    return model_gmm


def compare(gmm, file):
    rate, sig = wav.read(file["path"])
    tmp = mfcc(sig, rate)
    rate = {}
    for i in gmm:
        tmp2 = gmm[i]
        rate[i] = tmp2.score(tmp)
    return (keywithmaxval(rate))


def keywithmaxval(d):
    """ from https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
        a) create a list of the dict's keys and values;
        b) return the key with the max value"""
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))]

