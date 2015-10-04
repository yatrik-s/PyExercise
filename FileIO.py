# Sample program to demo File IO in Python


def OpenFile(filename, mode):
    try:
        fHandle = open(filename, mode)
    except IOError as err:
        print 'Error[%d]: File: %s: %s' % (err.errno, filename, err.strerror)
        return None
    return fHandle

f = OpenFile('readme.txt', 'r')
if f is None:
    exit()
text = f.read()
print text
f.close()

# Create a new file and write to it.
f = OpenFile('NewReadme.txt', 'w')
if f is None:
    exit()
f.write('# Sampple readme file created by FileIO.py\n')
f.write('This is another readme file.\n')
f.close()
