#Imports os, used to change folder in this case
import os

#Change directory
os.chdir(r'stockholm files')

#Opens and reads the file. Gets all the lines
with open('file.sthlm','r') as f:
    file_contents = f.readlines()

#Create a list with the first element as an empty string
contents = ['']

#Removes all lines with hashes, // and empty lines
for i in file_contents:
    if ("#" in i) or ('//' in i) or (i == '\n'):
        pass
    else:
        #Append to content list if it does not have it
        contents.append(i)

#Takes the length of the list -1 (since the first element is the length)
contents[0] = str(len(contents) - 1) + '\n'

#Opens and writes to a new file
with open('file_fixed.sthlm','w') as f:
    for i in contents:
        f.write(str(i))
