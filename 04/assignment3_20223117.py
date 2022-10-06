import pickle

dbfilename = 'assignment3.dat'

def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []

    scdb = []
    try:
        scdb = pickle.load(fH)
    except:
        print("Empty DB: ", dbfilename)
    else:
        print("Open DB: ", dbfilename)
    fH.close()
    return scdb



def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()

def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr, "=", p[attr], end=' ')
        print()

def doScoreDB(scdb):
    while (True):
        Name_list = []
        for i in range(len(scdb)):
            Name_list.append(scdb[i].get('Name'))
        inputstr = (input("Score DB > "))
        if inputstr == "":
            continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            try:
                if parse[1].isalpha():
                    record = {'Name': parse[1], 'Age': parse[2], 'Score': parse[3]}
                    scdb += [record]
                else:
                    print("Error : Please enter a proper name.")
            except IndexError:
                print("Error: Please enter command in this format: (add {Name} {Age} {Score})")

        elif parse[0] == 'del':
            try:
                if parse[1].isalpha():
                    if parse[1] not in Name_list:
                        print("Error: name not found.")
                    for i, p in enumerate(scdb):
                        if p['Name'] == parse[1]:
                            scdb[i] = 'temp'

                    while 'temp' in scdb:
                        scdb.remove('temp')
                else:
                    print("Error: Please Enter a proper name.")
            except IndexError:
                print("Error: Enter a name to delete!")

        elif parse[0] == 'find':
            try:
                if parse[1].isalpha():
                    for p in filter(lambda human: human['Name'] == parse[1], scdb):
                        for info in sorted(p):
                            print(info, "=", p[info], end=' ')
                        print()
                    if parse[1] not in Name_list:
                        print("Error: name not found.")
                else:
                    print("Error: Please Enter a proper name.")
            except IndexError:
                print("Error: Enter a name to find!")

        elif parse[0] == 'show':
            sortKey = 'Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)

        elif parse[0] == 'inc':
            try:
                if len(parse) == 3 and parse[1] not in Name_list:
                    print("Error: name not found.")
                for p in filter(lambda human: human['Name'] == parse[1], scdb):
                    p['Score'] = int(p['Score']) + int(parse[2])
                    if p['Score'] > 100:
                        print("(Maximum score is 100)")
                        p['Score'] = '100'
                    elif p['Score'] < 0:
                        print("(Minimum score is 0)")
                        p['Score'] = '0'
            except IndexError:
                print("Error: Please enter command in this format: (inc {Name} {Score to add})")

        elif parse[0] == 'quit':
            break

        else:
            print("Invalid command: " + parse[0])


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)