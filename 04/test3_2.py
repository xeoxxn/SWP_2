dbfilename = 'test3_2.dat'

def readScoreDB():
    try:
        fH = open(dbfilename)
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []
    else:
        print("Open DB: ", dbfilename)
    scdb = []
    for line in fH:
        dat = line.strip()
        # 공백 제거
        person = dat.split(",")
        record = {}
        for attr in person:
            kv = attr.split(":")
            record[kv[0]] = kv[1]
        scdb += [record]
    fH.close()
    return scdb

def writeScoreDB(scdb):
    fH = open(dbfilename, 'w')
    for p in scdb:
        pinfo = []
        for attr in p:
            pinfo += [attr + ":" + p[attr]]
        line = ','.join(pinfo)
        fH.write(line + '\n')
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
        print(Name_list)
        inputstr = (input("Score DB > "))
        if inputstr == "":
            continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            record = {'Name': parse[1], 'Age': parse[2], 'Score': parse[3]}
            scdb += [record]

        elif parse[0] == 'del':
            for i, p in enumerate(scdb):
                if p['Name'] == parse[1]:
                    scdb[i] = 'temp'
            while 'temp' in scdb:
                scdb.remove('temp')

        elif parse[0] == 'find':
            for p in filter(lambda human: human['Name'] == parse[1], scdb):
                for attr in sorted(p):
                    print(attr, "=", p[attr], end=' ')
                print()

        elif parse[0] == 'show':
            sortKey = 'Name' if len(parse) == 1 else parse[1]
            showScoreDB(scdb, sortKey)

        elif parse[0] == 'inc':
            for p in filter(lambda human: human['Name'] == parse[1], scdb):
                p['Score'] = int(p['Score']) + int(parse[2])
                if p['Score'] > 100:
                    p['Score'] = '100'
                elif p['Score'] < 0:
                    p['Score'] = '0'

        elif parse[0] == 'quit':
            break

        else:
            print("Invalid command: " + parse[0])


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)