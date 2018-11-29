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
    rate, sig = wav.read(file)
    tmp = mfcc(sig, rate)
    rate = {}
    for i in gmm:
        tmp2 = gmm[i]
        rate[i] = tmp2.score(tmp)
    print(file)
    print(rate)

