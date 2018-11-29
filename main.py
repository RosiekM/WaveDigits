import FilesManager
import test, gmm
from sklearn.model_selection import KFold

files, digits, types = FilesManager.importFiles("train")




train, test = test.split(types["M"])


mfcc = []
for i in test:
   mfcc.append(FilesManager.joinMfcc(files, excluded=i))

one = gmm.myGmm(mfcc[0])

for i in files:
   gmm.compare(one, files[i]["path"])


