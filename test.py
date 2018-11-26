from sklearn.model_selection import KFold

def split(list):
    kf = KFold(n_splits=5)
    train_base = []
    test_base = []
    for train_idx, test_idx in kf.split(list):
        tmp = []
        for i in train_idx:
            tmp.append(list[i])
        train_base.append(tmp)
        tmp2 = []
        for i in test_idx:
            tmp2.append(list[i])
        test_base.append(tmp2)
    return train_base, test_base