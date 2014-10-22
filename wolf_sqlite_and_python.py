import sqlite3 as dbapi

#Assignment 6
#Q9

con = dbapi.connect('portal_mammals.sqlite')

cur = con.cursor()

cur.execute('DROP TABLE FieldNotes')

cur.execute('CREATE TABLE FieldNotes("mo" INTEGER, "dy" INTEGER, "yr" INTEGER, "Notes" VARCHAR)')

#Q10
cur.execute("INSERT INTO FieldNotes VALUES(4,1,1963,'Just completed the April 1963 census of the site. "
            "The region is teeming with Dipodomys spectabilis. Using the time machine to conduct trapping "
            "prior to the start of the study is working out great!');")
# triple quotes best way to deal with long lines

#Q11
cur.execute("INSERT INTO FieldNotes VALUES(10,1,2013,'Vegetation seems to have returned to normal for "
            "this time of year. The landscape isnt exactly green, but there is a decent amount of plant "
            "activity and there should be enough food for the rodents to the winter');")

cur.execute("UPDATE FieldNotes set yr = 2012 where rowid=1")# can also use other WHERE conditions



# to delete: DELETE FROM Fieldnotes WHERE yr = 2012


#Q12: 
# 1. copy new code and old code to list then new table (old_v_new_codes)
# 2. copy all but old code to list then new table (new_species_table)

cur.execute("DROP TABLE new_versus_old_codes")
cur.execute("CREATE TABLE new_versus_old_codes(newcode TEXT, oldcode TEXT)")

cur.execute("SELECT new_code, oldcode FROM PortalMammals_species_old")#note that table name now corrected
new_old = cur.fetchall()
#print new_old

for newcode, oldcode in new_old:
    if oldcode is None:
        oldcode = "Unknown"    
    oldcode = oldcode.split(',')
    for codes in oldcode:
        codes = codes.strip()
        cur.execute("INSERT INTO new_versus_old_codes VALUES(?, ?)", (newcode, codes))
        #print codes

#Next line already run so don't do this again (yet)
#cur.execute("ALTER TABLE PortalMammals_species RENAME TO PortalMammals_species_old")
 
#Next line already run so don't do this again (yet)       
#cur.execute("CREATE TABLE PortalMammals_species AS SELECT new_code, scientificname, taxa, commonname, unknown, rodent, shrubland_affiliated  FROM PortalMammals_species_old")



"""stuff and things"""  #highlight first then add quotes.

# cur.fetchall() if you want to see all the results together as list of lists
#record = cur.fetchone("SELECT * FROM PortalMammals_Main WHERE yr = '2002'")
#while record:
    #print record
    #record = cur.fetchone()
con.commit()# Not needed for creating table but IS NEEDED for INSERTing and UPDATing 
con.close()