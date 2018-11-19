import FilesManager


files, digits, types = FilesManager.importFiles("train")

for i in types:
    print(types[i])

print("Kacper pipa")

FilesManager.joinMfcc(files)