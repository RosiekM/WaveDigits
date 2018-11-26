import FilesManager
import test
from sklearn.model_selection import KFold

files, digits, types = FilesManager.importFiles("train")

for i in types:
    print(types[i])

print("Kacper pipa")

train, test = test.split(types["M"])
print(test)

mfcc = []
for i in test:
   mfcc.append(FilesManager.joinMfcc(files, excluded=i))



print(mfcc)