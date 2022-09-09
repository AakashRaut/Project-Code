import sqlite3


class DbConnection:

    def __init__(self):
        global con
        con = sqlite3.connect('mydatabase.db')

    def CreateDbAndInsertValues(self):
        cursorObj = con.cursor()
        cursorObj.execute("CREATE TABLE IF NOT EXISTS Student(id integer PRIMARY KEY AUTOINCREMENT,RollNumber integer "
                          "UNIQUE, First_Name text,Last_Name text, AdmissionYear text)")
        con.commit()
        """cursorObj.execute("Insert into Student(RollNumber, First_Name ,Last_Name , AdmissionYear) Values(123,'Firoz',"
                          "'Rangrez','2019')")
        cursorObj.execute("Insert into Student(RollNumber, First_Name ,Last_Name , AdmissionYear) Values(456,"
                          "'Sameer','Kodgire','2019')")
        cursorObj.execute("Insert into Student(RollNumber, First_Name ,Last_Name , AdmissionYear) Values(789,"
                          "'Anchita','Lokhande','2019')")
        con.commit()"""

        cursorObj.execute("CREATE TABLE IF NOT EXISTS Attendance(id integer PRIMARY KEY AUTOINCREMENT,RollNumber integer "
                          "UNIQUE, First_Name text,Last_Name text, Date text,Status text)")
        con.commit()
        con.close()

    def getlistofidsfromdb(self):
        cursorObj = con.cursor()
        cursorObj.execute("Select RollNumber from User")
        rows = cursorObj.fetchall()
        #print(rows)
        return rows

    def getnamefromrollno(self,rollNumber):
        cursorObj = con.cursor()
        cursorObj.execute(f"Select * from User where RollNumber= {rollNumber}")
        rows = cursorObj.fetchall()
        return rows

    def MarkAttendance(self,arrayOfVals):

        cursorObj = con.cursor()

        cursorObj.execute(f"Insert into Attendance(RollNumber ,First_Name, Last_Name, Date, Status) Values"
                          f"({arrayOfVals['RollNumber']},'{arrayOfVals['FirstName']}',"
                          f"'{arrayOfVals['LastName']}','{arrayOfVals['Date']}','{arrayOfVals['Status']}')")
        con.commit()

    def InsertValueIntoUserTable(self,dbValues):
        print("Value inserted into DB")
        cursorObj = con.cursor()

        cursorObj.execute(f"Insert into User(RollNumber, First_Name ,Last_Name , AdmissionYear,Branch,UserType) Values({dbValues['RollNumber']},'{dbValues['FirstName']}',"
                          f"'{dbValues['LastName']}','{dbValues['AdmissionYear']},'{dbValues['Branch']}''{dbValues['UserType']}')")
        con.commit()



db = DbConnection()
#db.CreateDbAndInsertValues()
