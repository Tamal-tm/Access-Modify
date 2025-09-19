class User:
    def __init__(self, username, email, password):
        self.username=username
        self.password=password
        self._email=email
    
    def  clean_email(self):
        return self._email.lower().strip()
    
user1=User("Superman"," Clarkkent@gmail.com ","Clark Kent")

print(user1._email) # Not supposed to do this; just showing the difference.
# user1._email="sfsevsegsegs" # Not supposed to do this; just showing the difference.
print(user1.clean_email())
# Python trusts the developers to not use this convention, no misuse. 
# __email (Double underscore) (If we do this, then it's actially impossible to access this protected attribute outside the class)
# We change it in all and then, it will throw an error. (Name mangled--changed the name, therefore unable to access)

# Protected variable: _email
# Private variable: __email

# Both can be accessed within the class.
# Protected can be accessed outside the class but we shouldn't. 
# Private cannot be accessed outside the class. 
# Protected variable should be used within the class (internal use, since better readability and flexibility)
