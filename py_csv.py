
'''
            IMPLEMENTED DATE : 04/01/2018

            SCOPE OF IMPLEMENTATION :

                        This project developed for student record management based on python 
                        with csv file 

                        Operations are 
                            1. Registration
                            2. Get Specific Record
                            3. Display All record
                            4. Delete Specific record
                            5. Update Record

            DEVELOPER NAME : M.BALAVIGNESH
'''

import csv
import pandas as pd 
import os


#Class Declaration
class CSV_Master():

    #Constructor for csv file initialization
    def __init__(self):
        with open('record.csv','r') as read_csv:
            reader = csv.reader(read_csv)
            rows = list(reader)

            if rows == []:
                with open('record.csv','w') as csv_write:
                    writer = csv.writer(csv_write)
                    writer.writerow(['Name','Age','Gender','Address','Contact'])
            else:
                print("we can start")

    # Function for Record registration or creation
    def RegisRecord(self):
        print()
        name = str(input("Enter your name: "))
        age = str(input("Enter your age: "))
        gen = str(input("Enter your gender: "))
        add = str(input("Enter your address: "))
        con = str(input("Enter your contact: "))

        with open('record.csv','a') as append_csv:
            writer = csv.writer(append_csv)
            writer.writerow([name,age,gen,add,con])
            print("Successfully Recorded")

    #Function for Display All records
    @staticmethod
    def DisplayAllRecord():
        data = pd.read_csv('record.csv',index_col=0)
        print(data)

    #Function for DisplaySpecific Record
    def DisplaySpecificRec(self):
        tempd = pd.read_csv('record.csv')
        print()
        name = str(input("Enter the student name : "))
        wantD = tempd.loc[tempd["Name"] == name]
        if wantD.empty:
            print('Notfound')
        else:
            print(wantD)

    #Function for Delete Specific student Record
    def DeleteSpecIndex(self):
        with open('record.csv','r') as read_csv:
            reader = csv.reader(read_csv)
            rows = list(reader)
            print()
            name = str(input("Enter student name to delete Record :"))
            index = 0
            for n in range(0,len(rows)):
                if rows[index][0] == name:
                    rows.pop(index)
                    break
                index = index + 1
            print(rows)
            
        with open('temp.csv','w') as write_csv:
            writer = csv.writer(write_csv)
            for n in range(0,len(rows)):
                writer.writerow(rows[n])
            os.remove('record.csv')
            os.rename('temp.csv','record.csv')
            print("Successfully Deleted")
       


    # Function for Update the student Record
    def Updation(self):
        with open('record.csv','r') as read_csv:
            reader = csv.reader(read_csv)
            rows = list(reader)
            index = 0
            print()
            name = str(input("Enter the student name to update :"))
            for n in range(0,len(rows)):
                print(index)
                if rows[index][0] == name:
                    attr = str(input("Enter what field want to update : "))
                    if attr == "Name":
                        name = str(input("Enter the name : "))
                        rows[index][0] = name 
                    elif attr == "Age":
                        age = str(input("Enter the Age : "))
                        rows[index][1] = age 
                    elif attr == "Gender":
                        gen = str(input("Enter the Gender:"))
                        rows[index][2] = gen
                    elif attr == "Address":
                        add = str(input("Enter the Address: "))
                        rows[index][3] = add 
                    elif attr == "Contact":
                        con = str(input("Enter the contact : "))
                        rows[index][4] = con
                index = index + 1

        with open('temp.csv','w') as write_csv:
            writer = csv.writer(write_csv)
            for n in range(0,len(rows)):
                writer.writerow(rows[n])
            os.remove('record.csv')
            os.rename('temp.csv','record.csv')
            print("successfully updated")


    # Function for Terminate the program
    def Exit(self):
        quit()


#Object creation or intitialization
master = CSV_Master()

# Function for Call the user needed Function
def ActionDispatcher(choice):
    {
        1 : master.RegisRecord,
        2 : master.DeleteSpecIndex,
        3 : master.DisplaySpecificRec,
        4 : master.DisplayAllRecord,
        5 : master.Updation,
        6 : master.Exit
    }.get(choice)()

#Print Statement for Display the Operation choice to perform
print("Enter choice 1 for Registration")
print("Enter choice 2 for Delete Specific Record")
print("Enter choice 3 for Get student Record")
print("Enter choice 4 for Display All Records")
print("Enter choice 5 for Update the record")
print("Enter choice 6 for Quit")
print()

# loop for asking contineous user choice for operation
while True:
    choice = int(input("Enter your choice : "))
    ActionDispatcher(choice)




