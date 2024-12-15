import re 
#imports the regex module in python and we have used tha to validate the emails
import os
#checks for the library befroe opening through an operating system
class EmailManager:
#EMailManager is put into class as class bundles data which have similar attributes
    def __init__(self,fname="emaillib.txt"):
#initializes objects
        self.fname=fname
#self refers to the current object we are working on
        self.emaillib={}
        self.loadlib()
    def addemail(self,email):
        pattern=r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
        if re.fullmatch(pattern,email):
        #of the email matches the patter ngiven in the regex then it will be added to library
            if email not in self.emaillib:
        #this if statement makes sure theres no duplicates in the library 
                return f"Email '{email}' has been added to the library"
            elif email in self.emaillib:
                return f"Email '{email}' is already in the library"
        else:
            print("EMail is invalid")
            #if the input doesnt mathc the regex then it will be rejected
    def displaylib(self):
        if self.emaillib:
            res="Email Library:\n"
            for idx, (email,info) in enumerate(self.emaillib.items(), start=1):
                #loop through every email in th elibrary and scans its data essentially 
                res+=f"{idx}. {email}\n"
            return res.strip()
        else:
            return "empty"
    def savelib(self):
        #method to save the email 
        with open(self.fname, "w") as file:
            #opens the wanted file in order to wrtie somethign 
            for email, info in self.emaillib.items():
                #goes over library and scans it as email being the key and info being the values
                file.write(f"{email}\n")
        return f"Library saved on '{self.fname}'."
    def loadlib(self):
        if os.path.exists(self.fname):
        #operating system checks if said file exists
            with open(self.fname, "r") as file :
                #opens the file to read
                for line in file:
                    email=line.strip().split(",")

            return f"Library loaded from '{self.fname}'."
        else:
            return" Error in loading library"
    def run(self):
        print("welcome to the email Manager")
        while True :
            print("\nMenu:")
            print("press 1 to add email")
            print("press 2 to display all emails")
            print("press 3 to save all emails")
            print("press 4 if you are finished with the manager")
            num = (input("enter number"))
            if num=="1":
                email=input("enter email")
                print(self.addemail(email))   
            elif num=="2":
                print(self.displaylib())
            elif num=="3":
                print(self.savelib())
            elif num=="4":
                print(self.savelib())
                print("Saved and Exit")
                break
            else:
                print("error")
#main part of the interface for the user
if __name__ == "__main__":
    manager = EmailManager()
    manager.run()

