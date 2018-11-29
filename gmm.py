from sklearn.mixture import GaussianMixture
import numpy as np
import scipy.io.wavfile as wav
from python_speech_features import mfcc

def myGmm(mfcc):
    tmp = {}
    for i in mfcc:
        tmp[i] = {}
        tmp3 = []
        for k in mfcc[i]:
            tmp3.append(mfcc[i][k])
        tmp2 = GaussianMixture(n_components=13, random_state=3)
        tmp[i] = tmp2.fit(tmp3)
        print("another one is finished")


    return tmp


def compare(gmm, file):
    rate, sig = wav.read(file)
    tmp  = mfcc(sig, rate)
    one = gmm[0].score(tmp[0])
    print(one)
