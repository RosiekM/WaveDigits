from sklearn.mixture import GaussianMixture
import numpy as np
import scipy.io.wavfile as wav
from python_speech_features import mfcc


def myGmm(mfcc):
    model_gmm = {}
    for i in mfcc:
<<<<<<< HEAD
        gauss = GaussianMixture(n_components=13)
        model_gmm[i] = gauss.fit(mfcc[i])
=======
        tmp[i] = {}
        tmp3 = []
        for k in mfcc[i]:
            tmp3.append(mfcc[i][k])
        tmp2 = GaussianMixture(n_components=13, random_state=3)
        tmp[i] = tmp2.fit(tmp3)
>>>>>>> dbc5e585d119643e0b64e288f245d13db458fdca
        print("another one is finished")

    return model_gmm


def compare(gmm, file):
    rate, sig = wav.read(file)
    tmp = mfcc(sig, rate)
    LLHlist = {}
    for i in gmm:
        tmp2 = gmm[i]
        print(np.array(tmp2.score(tmp)))

