class User: 

    def __init__(self): #a method that initializes the user object with an id and username
       self.id = user.id
       self.username = user.username
       self.followers = 0
       self.following = 0

    def follow(self, user): # a method that allows a user to follow another user where "self" is the user who is following and "user" is the user being followed
        user.followers += 1
        self.following += 1

user_1 = User("001", "lotanna") 

user_2 = User("002", "john") 