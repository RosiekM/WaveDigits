import FilesManager
import test, gmm
from sklearn.model_selection import KFold


files, digits, types = FilesManager.importFiles("train")




train, test = test.split(types["M"])


mfcc = []
for i in test:
   mfcc.append(FilesManager.joinMfcc(files, excluded=i))


for k in range(len(train)):
   one = gmm.myGmm(mfcc[k])

   good = 0
   bad = 0
   for i in files:
      if files[i]['lektor'] in test[k]:
         if gmm.compare(one, files[i]) == files[i]["znak"]:
            good += 1
         else:
            bad +=1
   file = open("recognition_ratio", 'a')
   file.write("recognition ratio of: " + str(k) + " " )
   file.write(str(int(good/(good+bad)*100)) + "%\n" )
   file.close



