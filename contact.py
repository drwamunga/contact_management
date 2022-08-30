from prettytable import PrettyTable
import sqlite3
import os

os.chdir('/home/user/Desktop/project')

my_database = sqlite3.connect('connect.db')
try:
    my_database.execute('SELECT * from contact')
except:
    my_database.execute('''CREATE TABLE CONTACT
        (NAME       char(30) primary key NOT NULL,
        Phone_no    INT   NOT NULL,
        ADDRESS     CHAR(50),
        EMAIL_ID    CHAR(50));''')

class contacts:
    Name = str()
    Mobile_no = str()
    Address = str()
    Email = str()

    def __init__(self):
        self.Name = ''
        self.Mobile_no = ''
        self.Address = ''
        self.Email = ''

    def showTable(self,contact_details):
        display = PrettyTable(['Name','Mobile_no','Address','Email'])
        data = []
        for i in contact_details:
            data.append(i)
        if (not data):
            print('Data not found')
            return
        display.add_rows(data)
        print(display)
        return

    def addContact(self):
        self.Name = input('Enter the name: ')
        self.Mobile_no = input('Enter the mobile_no: ')
        self.Address = input('Enter the address: ')
        self.Email = input('Enter the email ')

        my_database.execute('insert into contact values("{}","{}","{}","{}")'.format(self.Name,self.Mobile_no,self.Address,self.Email))
        my_database.commit()
        print('Data saved successfully')

    def showContact(self):
        contact_details = my_database.execute('select * from contact')
        self.showTable(contact_details)

    def editContact(self):
        self.delete()
        self.addContact()
    
    def delete(self):
        delete_name = input('Enter name of contact to delete: ')

        my_database.execute('Delete from contact where NAME = "{}" COLLATE NOCASE'.format(delete_name))
        my_database.commit()
        print('Data deleted successfully')

    def searchContact(self):
        search_name = input('Enter name of contact to search: ')
        data = my_database.execute('select * from contact where name = "{}" COLLATE NOCASE'.format(search_name))
        self.showTable(data)

def start():
    print(' '*15,'1. Press a to add new contact...')
    print(' '*15,'2. Press s to add show contact...')
    print(' '*15,'3. Press e to add edit contact...')
    print(' '*15,'4. Press d to add delete contact...')
    print(' '*15,'5. Press g to add search contact...')
    print(' '*15,'6. Press q to exit application...')

if __name__ == "__main__":
    person = contacts()
    print(':Welcome to contact management system:')

    answer = 'y'
    while answer in ['y','Y']:
        start()
        choice = input('Enter your choice:\t')
        if choice in ['a','Y']:
            person.addContact()
        elif choice in ['s','S']:
            person.showContact()
        elif choice in ['e','E']:
            person.editContact()
        elif choice in ['d','D']:
            person.delete()
        elif choice in ['g','G']:
            person.searchContact()
        elif choice in ['q', 'Q']:
            exit()
        else:
            print('Invaild input!!!...')
        answer = input('Want to perform more operations y/n:\t')
        print('Application closed')