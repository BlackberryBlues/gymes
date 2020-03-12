with open('chat.txt', 'r') as f:
    db = {}
    for line in f.readlines():
        time, name = line.split()
        if name not in db.keys():
            db[name] = int(time)
        else:
            db[name] += int(time)
    dbs = sorted(db.items(), key=lambda x: x[1], reverse=True)
    for name, time in dbs:
        print(f'{time}\t{name}')