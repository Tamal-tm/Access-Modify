# 1. The traditional way: Make the data private and use getters and setters. 

from datetime import datetime

class User:
    def __init__(self, username, email, password):
        self.username=username
        self.password=password
        self._email=email # Protected
    
    def get_email(self):# Method  #Use get to access #Provides control way of accessing objs (email address)
        print(f"Email accessed at {datetime.now()}")
        return self._email
    
    def set_email(self, new_email): # Use set to change/update
        if "@" in new_email: # Validation check
            self._email=new_email
        

    
user1=User("Superman","clarkkent@gmail.com","Clark Kent")
print(user1.get_email()) # Accessing outside class in correct way.

user1.set_email("superman@23gmail.com")
print(user1.get_email())

user1.set_email("gc hkjnobu") # Won't get printed (controlled modification by verification)
print(user1.get_email())
