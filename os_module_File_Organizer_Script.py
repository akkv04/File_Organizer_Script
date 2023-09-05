import os
import shutil

#a script that organizes files in a given directory by moving them into subdirectories based on their file extensions
# testing path  C:\Akhil\python

print("Current path is" + "\t" +  os.getcwd())



#testing whether the path exists and is a directory
if (os.path.exists("C:\Akhil\python") & os.path.isdir("C:\Akhil\python")):
    print("directory exists")
else:
    print("directory doesnt exists")

#changing directory to testing path  C:\Akhil\python
os.chdir("C:\Akhil\python")
print("the new directory is"+ "\t" + os.getcwd())

current_path = os.getcwd()

files = os.listdir(os.getcwd())

#listing the files in the directory
print ("the files in the directory are")
print(os.listdir(os.getcwd()))

#copying the file into sub directory based on the file
for file in files:
    if (os.path.isfile(file)):
        #getting the extension of each file
        ext = os.path.splitext(file)
        #seperating the '.' from the extension file
        print(ext[1][1:])
        print( "file is getting moved from ")
        print(os.path.join(current_path,file))
        print( "to")
        print(os.path.join(os.path.join(current_path,ext[1][1:]),file))
        os.rename(os.path.join(current_path,file),os.path.join(os.path.join(current_path,ext[1][1:]),file))
        #shutil.move(os.path.join(current_path,file),os.path.join(os.path.join(current_path,ext[1][1:]),file))


