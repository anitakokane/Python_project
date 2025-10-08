import os
from datetime import datetime
print("Welcome to Personal Journal Manager")
class JournalManager:
    def __init__(self,filename="text.txt"):
        self.filename=filename
    def add(self):
        data=input("Write your journal entry:")
        time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            
            with open(self.filename,"a") as f:
                f.write(f"{time} - {data}\n")
                print("Entry added Succesfully")
        except Exception as e:
            print("Error while adding Entry:",e)
    
    def show(self):
        print("All your Journal Enteries:")
        try:
            with open(self.filename,"r") as f:
                entries=f.readlines()
                f.close()
                if entries:
                    for line in entries:
                        print(line.strip())
                else:
                    print("Journal is empty")
        except Exception as e:
            print("Error:",e)
    
    def search(self):
        keyword=input("Enter a keyword or date to search:")
        try:
            with open(self.filename,"r") as f:
                entries=f.readlines()
                f.close()
                found=[e for e in entries if keyword.lower() in e.strip().lower()]
                if found:
                    print("Matching Entries:")
                    for entry in found:
                        print(entry.strip())
                else:
                    print("Matching entry not found")
        except Exception as e:
            print("Error:",e)
    
    def delete(self):
        choice=input("Are you sure you want to delete all entries?(yes/no) :")
        if choice.lower()=="yes":
            try:
                with open(self.filename,"w") as f:
                    f.close()
                    print("Entries deleted succesfully")
            except Exception as e:
                print("error:",e)
        else:
            print("Deletion is canceled")

obj=JournalManager()
while True:
    print("Please select an option:")
    print("1.Add a New Entry")
    print("2.View all Enteries")
    print("3.Search for an Entry")
    print("4.delete all Entries")
    print("Exit")

    option=int(input("User Input:"))
    match(option):
        case 1:
            obj.add()
        case 2:
            obj.show()
        case 3:
            obj.search()
        case 4:
            obj.delete()
        case 5:
            print("Exiting the system!Bye")
            break
        case _:
            print("Enter a valid choice!")



                    
                        

    
    
