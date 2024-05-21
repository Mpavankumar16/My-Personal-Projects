import os #For file reading

pathName  = "/Users/pavankumar.munganda/My Personal Projects/Python Tutorials/note.txt"

#File or not and path is crct or not check
if(os.path.exists(pathName)):
    print("File exists")
    if(os.path.isfile(pathName)):
        print("That is a file")

#Folder or not check
if(os.path.isdir("/Users/pavankumar.munganda/My Personal Projects/Python Tutorials/FileHandlingPract")):
    print("That is a Folder")

#With open will close the file automatically but won't caught exception
with open(pathName) as file:
    print(file.read())

print(file.closed) #will check file is closed or not print boolean

#Writing to file w - write r-read
#Below code will override the existing file if any or create a new one
with open('fileWrite.txt', 'w') as file:
    file.write("I'm new here\nCan you help me find the address")

#Appending text to existing file or create a new file if not available
with open('append.txt', 'a') as file:
    file.write("I'm new here \nCan you help me find the address")

#Replace will be used to move file or directory
os.replace("sourcePath" ,"Decitnationpath")

#Remove and remove empty dir
os.remove("Path")
os.rmdir("Path") #If dir is empty then only deletes or throws an error for that to u