fH = open('test17.dat', 'r')
lines = fH.readlines()
fH.close()
fH = open('test17.out', 'w')
for line in lines:
    words = line.split(' ')
    fH.write(words[0] + '\n')
fH.close()
