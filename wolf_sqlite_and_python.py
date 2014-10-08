import sqlite3 as dbapi

con = dbapi.connect('portal_mammals.sqlite')

cur = con.cursor()

cur.execute('create table FieldNotes("mo" INTEGER, "dy" INTEGER, "yr" INTEGER, "Notes" VARCHAR)')

#record = cur.fetchone("SELECT * FROM PortalMammals_Main WHERE yr = '2002'")
#while record:
    #print record
    #record = cur.fetchone()
    
con.close()