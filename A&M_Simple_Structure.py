class User:
    def __init__(self, username, email, password):
        self.username=username
        self.password=password
        self.email=email
    
    def say_hi_to_user(self, user):
                       print(f"Sending message to {user.username}: Hi {user.username}, it's {self.username}")

user1=User("Superman","sm@gmail.com","Clark Kent")
user2=User("Batman","bm@gmail.com","Bruce Wayne")

user1.say_hi_to_user(user2) # Here user1 is self, user2 variable values will pass onto say_hi_to_user function.

user1.email="clarkkent@gmail.com"
print(user1.email)