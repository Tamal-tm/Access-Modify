# 2. Properties

class User:
    def __init__(self, username, email, password):
        self.username=username
        self.password=password
        self._email=email # Protected instance attribute
    
    @property # getter property # decorator
    def email(self): # same name as the attribute # With this, we can access an underscore email attribute using/calling user1.email
        print("Email accessed.") 
        return self._email
    
    @email.setter # setter property # decorator
    def email(self, new_email):
        if "@" in new_email:
            self._email=new_email


user1=User("Batman","batman47W@gmail.com","123")
user1.email="This is not an email"
print(user1.email) # Doesn't have to change (.email)