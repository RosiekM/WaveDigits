import FilesManager


files, digits, types = FilesManager.importFiles("train")

for i in types.keys():
    print(i)