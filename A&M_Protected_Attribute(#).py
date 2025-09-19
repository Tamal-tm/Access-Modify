# Accessing and Modifying Data:
# 1. The traditional way: Make the data private and use getters and setters. 


class User:
    def __init__(self, username, email, password):
        self.username=username
        self.password=password
        self._email=email# Protected attribute (Communicated to Python)
                         # By prefixing an undercore in front of the attribute name. (_email)
                         # Indicates that something is intended for internal use within the class or module (Should not be used outside the class)
    
    def get_email(self):
      return self._email 
  
user1=User("Superman","sm@gmail.com","Clark Kent")
print(user1._email) # The protected/private attribute is accessible outside the class.
                     # Signals to developers that it's meant to be protected or internal to the class.  


