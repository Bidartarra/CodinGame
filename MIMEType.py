import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
mimedict = {}
extension = ''
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    mimedict = {**mimedict, '.' + ext.lower(): mt} #lower casing the extension to ease comparison
    
#print(mimedict)
for i in range(q):
    fname = input()  # One file name per line.
    fnameinv = fname[::-1].lower() #inverting the string to find the last extension and lower casing it
    for k in range(0, len(fnameinv)):
        if fnameinv[k] == '.':
            extensioninv = fnameinv[0:k+1] #create a substring with the reversed extension
            extension = extensioninv[::-1]
            break #exiting the loop after the first dot is found
        elif '.' not in fname:
            extension = ''
            
    #print(extension)
    if extension == '':
        print('UNKNOWN')
    elif extension == '.':
        print('UNKNOWN')
    elif extension in mimedict:
        print(mimedict[extension])
    else:
        print('UNKNOWN')
    extension == '' #emptying the variable
