import FilesManager


files, digits, types = FilesManager.importFiles("train")




print(types["M"])


one = FilesManager.joinMfcc(files)

print(one[1][12])


from sklearn.model_selection import KFold



one = KFold(n_splits=5)
one.get_n_splits(types["M"])

for train_index, test_index in one.split(types["M"]):
    data = []
    for i in test_index:
        data.append(types["M"][i])
    print("Testowy:", data)
