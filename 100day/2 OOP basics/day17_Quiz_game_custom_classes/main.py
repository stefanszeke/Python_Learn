

class User:
    def __init__(self, age):
        self.age = age
        self.id = self.get_id()

    def get_id(self):
        return self.age * 2

user1 = User(20)
user2 = User(30)

print(user1.id)
print(user2.id)
        
        


