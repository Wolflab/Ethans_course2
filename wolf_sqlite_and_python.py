import sqlite3 as dbapi

con = dbapi.connect('portal_mammals.sqlite')

cur = con.cursor()

cur.execute('DROP TABLE FieldNotes')

cur.execute('CREATE TABLE FieldNotes("mo" INTEGER, "dy" INTEGER, "yr" INTEGER, "Notes" VARCHAR)')

cur.execute("INSERT INTO FieldNotes VALUES(4,1,1963,'Just completed the April 1963 census of the site. "
            "The region is teeming with Dipodomys spectabilis. Using the time machine to conduct trapping "
            "prior to the start of the study is working out great!');")

cur.execute("INSERT INTO FieldNotes VALUES(10,1,2013,'Vegetation seems to have returned to normal for "
            "this time of year. The landscape isnt exactly green, but there is a decent amount of plant "
            "activity and there should be enough food for the rodents to the winter');")

cur.execute("UPDATE FieldNotes set yr = 2012 where rowid=1")

#record = cur.fetchone("SELECT * FROM PortalMammals_Main WHERE yr = '2002'")
#while record:
    #print record
    #record = cur.fetchone()
con.commit()    
con.close()