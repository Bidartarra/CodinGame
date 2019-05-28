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
    mimedict = {**mimedict, ext: mt}
    
print(mimedict)
for i in range(q):
    fname = input()  # One file name per line.
    fnameinv = fname[::-1] #inverting the string to find the last extension
    for k in range(0, len(fnameinv)):
        if fnameinv[k] == '.':
            extensioninv = fnameinv[0:k] #create a substring with the reversed extension
            extension = extensioninv[::-1]
    print(extension)
    #if extension == '':
        #print('UNKNOWN')
    #elif extension in mimedict:
        #print(mimedict[extension])
    #else:
        #print('UNKNOWN')
            
            
    #if ext in fname:
        #print(mt)
        #print(ext)
    #else:
        #print("unknown")
#print(mt)
#print(ext)


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
#print( mt)
