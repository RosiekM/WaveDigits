import FilesManager


files, digits, types = FilesManager.importFiles("train")

for i in types:
    print(types[i])



FilesManager.joinMfcc(files)
