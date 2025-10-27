import sys

print(sys.getsizeof(int))
# # print(sys.path())

# # print(sys.platform())
# # print(sys.version())

# # print(sys.argv([0]))
# # print(sys.argv([1]))
# # print(sys.argv([2]))

# import os
# lst = os.listdir() #returns a list of all the files in the folder 
# print (lst)

# os.mkdir(r"C:\\Users\\ASUS\\OneDrive\\Desktop\\Study\\VS Code\\Python\\newDirr") #creates new folder, the last name is the name of the new folder, throws an error if any intermediate folder is not present 
# os.makedirs(r"newDirr\\mts\\man\\najmi")  #creates new folder at the given path, if any intermediate foder is not present it creates that folder

# os.rename("sample.txt" , r"C:\\Users\\ASUS\\OneDrive\\Desktop\\Study\\VS Code\\Python\\oldDir\\sample.txt")  #moves a file to another location
# os.rename("sample2.txt" , r"C:\\Users\\ASUS\\OneDrive\\Desktop\\Study\\VS Code\\Python\\oldDir\\renamed.txt")  #can also move file and change the name together
# os.rename('Smodule.py','SS_Module.py')  #changes the name 
# os.renames("sample3.txt" , r"C:\\Users\\ASUS\\OneDrive\\Desktop\\Study\\VS Code\\Python\\newDir\\renaamed.txt")  #changes the location of a file, can create intermediate folder if not found, can also rename the file while moving

# os.replace(r"C:\\Users\\ASUS\\OneDrive\\Desktop\\Study\\VS Code\\Python\\oldDir\\sample.txt" , r"C:\\Users\\ASUS\\OneDrive\\Desktop\\Study\\VS Code\\Python\\newDir\\renaamed.txt")  #the first file/dir replaces the second file/dir, the name of new file/dir will be same as the name of second file/dir  

# print(os.getcwd())  #returns the path of current working directory (folder)
# os.chdir(r"C:\\Users\\ASUS\\OneDrive\\Desktop\\Study\\VS Code\\Python\\newDir")  #changes the current working dir (folder) with the given path 

# print(os.path.exists(path))  #returns true if the given path/file/dir exists otherwise false

# print(os.path.isfile('newFile.txt'))  #returns true if the given path/file_name is a file, and false if it is dir/folder
# print(os.path.isdir('newDir'))  #returns true if the given path/file_name is dir/folder and false if it is a file

# print(os.path.getsize('newFile.txt'))  #returns the size of the file in bytes

# print(os.cpu_count())  #returns the number of CPUs/cores in the system/machine

# print(os.getlogin())  #returns the name of current user

# os.path.join(path, 'newFile.txt')  #returns a string of joined paths, it does not change the location just creates a string of joined paths


# print(os.path.abspath('new.txt')) # returns a strng of path for the given file/dir name, it does not really check for the file it just gives the string of path

# print(os.path.splitext("text.txt"))  #it splits the file name and the extension, it does not check for the existence of the file, if the file name has multiple extenstions only last one is splitted

# with os.scandir('newDir') as ent:  #it runs an iterator at the given path/dir, each iteration retuns a file/dir name at that path/dir. a loop has to be used to store the file/dir names or to print it
#     for i in ent:
#         print(i)

# for dir_path,DIRs,files in os.walk(path):  #traverses the given dir(path of given folder) from top to down, at each iteration it returns 3 tuples - dir path; dir names; file name, to store/print the tuples a loop has to be used 
#     print(dir_path, 'dir path')
#     print(DIRs, 'tuple for dir names')
#     print(files, '<-- tuple for file names')

# os.getpid()  #returns current process id
# os.getppid()  #returns parent process id
