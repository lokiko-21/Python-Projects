import os

file = os.listdir(path = 'C:\\Users\\Marco Antonio\\OneDrive\\Documents\\GitHub\\Python-Projects\\challenges\\scriptAssignment')
fileTime = os.path.getmtime('C:\\Users\\Marco Antonio\\OneDrive\\Documents\\GitHub\\Python-Projects\\challenges\\scriptAssignment')

for i in file:
    if ".txt" in i:
        iTime = os.path.getmtime(i)
        print('')
        print(i)
        print('')
        print(iTime)
