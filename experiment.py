class User:

    def __init__(self, username, postcode):
        self.username = username
        self.postcode = postcode
        self.followers = 0


user1 = User("Angela", "1234")

print(user1.__dict__)
