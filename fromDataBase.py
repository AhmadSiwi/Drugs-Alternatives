import sqlite3

conn = sqlite3.connect('drugsDataBase.sqlite')
cur = conn.cursor()

cur.executescript('''

CREATE TABLE IF NOT EXISTS Drug (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS Active_ingredient (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name  TEXT UNIQUE
);
CREATE TABLE IF NOT EXISTS Containment (

    drug_id     INTEGER,
    active_ingredient_id   INTEGER,
    PRIMARY KEY (drug_id, active_ingredient_id)
)
''')


def addDrug(name, ingredients):
    cur.execute('''INSERT OR IGNORE INTO Drug (name)
        VALUES ( ? )''', (name, ) )
    cur.execute('SELECT id FROM Drug WHERE name = ? ', (name, ))
    drug_id = cur.fetchone()[0]
    active_ingredient_id = 0
    for ingredient in ingredients:
        cur.execute('''INSERT OR IGNORE INTO Active_ingredient (name)
            VALUES ( ? )''', (ingredient, ) )

        cur.execute('SELECT id FROM Active_ingredient WHERE name = ? ', (ingredient, ))
        active_ingredient_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Containment (drug_id, active_ingredient_id)
            VALUES ( ?, ? )''', (drug_id, active_ingredient_id ) )


def findAlternatives(name):
    cur.execute('SELECT id FROM Drug WHERE name = ? ', (name, ))
    drug_id = cur.fetchone()[0]
    active_ingredient_ids = conn.execute('SELECT active_ingredient_id FROM Containment WHERE drug_id=?',(drug_id,))
    listOfLists = list()
    for ingredient in active_ingredient_ids:
        active_ingredient_ids = conn.execute('SELECT drug_id FROM Containment WHERE active_ingredient_id=?',(ingredient,))
        listOfLists.append(active_ingredient_ids)
        firstList = listOfLists[0]
    returnedList = list()
    for i in firstList:
        isFound = True
        for j in listOfLists:
            if not(i in j):
                isFound = False
        if isFound:
            returnedList.append(i)
    return returnedList
