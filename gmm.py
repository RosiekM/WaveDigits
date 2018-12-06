from sklearn.mixture import GaussianMixture


def myGmm(mfcc, n_components=1, covariance_type='full', tol=0.001, reg_covar=1e-06, max_iter=100, n_init=1,
          init_params='kmeans', weights_init=None, means_init=None, precisions_init=None, random_state=3,
          warm_start=False, verbose=0, verbose_interval=10):
    model_gmm = {}
    for i in mfcc:
        gauss = GaussianMixture(n_components=n_components, covariance_type=covariance_type, tol=tol,
                                reg_covar=reg_covar, max_iter=max_iter, n_init=n_init,
                                init_params=init_params, weights_init=weights_init, means_init=means_init,
                                precisions_init=precisions_init, random_state=random_state,
                                warm_start=warm_start, verbose=verbose, verbose_interval=verbose_interval)
        model_gmm[i] = gauss.fit(mfcc[i])
        #print("another one is finished")

    return model_gmm


def compare(gmm, mfcc):
    rate = {}
    for i in gmm:
        tmp2 = gmm[i]
        rate[i] = tmp2.score(mfcc)
    return (keywithmaxval(rate))


def keywithmaxval(d):
    """ from https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
        a) create a list of the dict's keys and values;
        b) return the key with the max value"""
    v = list(d.values())
    k = list(d.keys())
    return k[v.index(max(v))], max(v)
