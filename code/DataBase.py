import sqlite3
# from main import packet_list
allKind=['TCP','UDP','ICMP','ARP','OTHER','BAD']
conn=None
c=None
def init_data_base():
    global conn
    global c
    conn = sqlite3.connect('netPackets.db')
    c = conn.cursor()
    c = conn.cursor()
    for t in allKind:
        c.execute('CREATE TABLE IF NOT EXISTS '+t+'''DATA 
           (ID INT PRIMARY KEY     NOT NULL,
           ALLDATA      TEXT        NOT NULL);''')

    conn.commit()

def insertDataBase(list,type):
    inserStr="INSERT INTO {TYPE}DATA VALUES ({ID},'{ALLDATA}')".format(
            TYPE=type,ID=list[0],ALLDATA=list[1]
        )
    c.execute(inserStr)
    conn.commit()

def drop_table():
    for t in allKind:
        c.execute("delete  from "+t+"DATA")
    conn.commit()

def getInfo(index,type):
    res=''
    cursor=c.execute("select ALLDATA from "+type+"DATA where ID="+str(index))
    for row in cursor:
        res=row[0]
    return res

if __name__ =="__main__":
    init_data_base()
    drop_table()
    plist=[]
    for i in range(10):
        list=[10,'2a3f4b562345655432345675432d']
        list[0]=i
        plist.append(list)
    insertDataBase(plist,'TCP')
    print(getInfo(2,"TCP"))
    # drop_rable()



