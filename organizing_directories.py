import os
from pathlib import Path
subdirectories = {
    'documents':['.pdf' , '.docs' , '.txt'],
    'audio': ['.m4a' ,'a4b', '.mp3'],
    'video':['.mp4' , '.mov' , 'avi'],
    'image':['.jpg' , '.png' , 'jpeg']
}

def pickdirectory(value):
    for category , sufixes in subdirectories.items():
        for sufix in sufixes:
            if sufix==value:
                return category
    return value+" folder" #If filetype doesn't exist in our dictionary
            

getdirectory = input("Enter Directory path")

directorytoorganize = Path(getdirectory)

for item in directorytoorganize.iterdir():
    filepath = Path(item)
    print(filepath)
    filename = os.path.basename(filepath)

    filetype = filepath.suffix.lower()

    directory = pickdirectory(filetype)
    directoryPath = Path(directory)
    # directory = pickdirectory(filetype)
    # directorypath = Path(directory)

    print(directory)
    print("####directory path" , directoryPath)

    newdirectory = os.path.join(directorytoorganize, directory)
    newdirectorypath = Path(newdirectory)

    if newdirectorypath.is_dir() != True:
             newdirectorypath.mkdir()
    filepath.rename(newdirectorypath.joinpath(filename))


gc = pickdirectory('.jpg')
print(gc)



# import os
# from pathlib import Path
# SUBDIRECTORIES = {
#     "DOCUMENTS": ['.pdf','.rtf','.txt'],
#     "AUDIO":['.m4a','.m4b','.mp3'],
#     "VIDEOS": ['.mov','.avi','.mp4'],
#     "IMAGES": ['.jpg','.jpeg','.png']
# }
# def pickDirectory(value):
#     for category, suffixes in SUBDIRECTORIES.items():
#         for suffix in suffixes:
#             if suffix == value:
#                 return category
#     return 'MISC' #If filetype doesn't exist in our dictionary

# def organizeDirectory():
#     for item in os.scandir():
#         if item.is_dir():
#             continue
#         filePath = Path(item)
#         print(filePath)
#         filetype = filePath.suffix.lower()
#         directory = pickDirectory(filetype)
#         directoryPath = Path(directory)
#         if directoryPath.is_dir() != True:
#             directoryPath.mkdir()
#         filePath.rename(directoryPath.joinpath(filePath))

# organizeDirectory()