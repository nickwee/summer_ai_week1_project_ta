# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list
        
    ## For more challenge try this
    def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass

    ## For more challenge try this
    def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        pass

    def  create_account(self):
        #implement function that creates account here
        username = input("Please enter your username: ")
        age = input("Enter your age: ")
        user = Person(username, age)
        self.list_of_people.append(user)
        print("Account successfully created: " + "\nUsername: " + username + "\nAge: " + age)
        pass

    def getCurrentUser(self, username):
        for user in self.list_of_people:
            if user.username == username:
                return user


class Person:
    def __init__(self, name, age):
        self.username = name
        self.age = age
        self.friendlist = []
        self.inbox = []

    def setName(self, name):
        self.username = name
    
    def setAge(self, age):
        self.age = age
    
    def editProfile(self, editDetailsChoice):
        while True:
            if editDetailsChoice == "1":
                newUsername = input("Please enter your new username: ")
                self.setName(newUsername)
            elif editDetailsChoice == "2":
                newAge = input("Please enter your new age: ")
                self.setAge(newAge)

    def add_friend(self, friendName, ai_social_network):
        #implement adding friend. Hint add to self.friendlist
        friend = None
        if any(user.username == friendName for user in ai_social_network.list_of_people):
            friend = ai_social_network.getCurrentUser(friendName)
            if (friend not in self.friendlist):
                self.friendlist.append(friend)
                print("You have added " + friendName + " as a friend! ")
            else:
                print(friendName + " is already on your friend list! ")
        else:
            print("User does not exist. ")
    
    def viewFriendList(self):
        print("*********** " + self.username + "'s Friend List ***********")
        for friend in self.friendlist:
            username = friend.username
            print(username)

    def blockFriend(self, blockedFriendName, ai_social_network):
        if any(user.username == blockedFriendName for user in self.friendlist):
            blockedFriend = ai_social_network.getCurrentUser(blockedFriendName)
            self.friendlist.remove(blockedFriend)
            print("You have blocked " + blockedFriendName)
        else:
            print("User is not on your friend list. ")

    def sendMessage(self, friendName, ai_social_network):
        if any(user.username == friendName for user in self.friendlist):
            friend = ai_social_network.getCurrentUser(friendName)
            message = input("Type your message: ")
            friend.inbox.append(message)
            print("You have sent " + message + " to " + friendName)
        else:
            print("User is not on your friend list. ")
    
    def viewMessages(self):
        print("*********** " + self.username + "'s Message Inbox ***********")
        print(*self.inbox, sep = "\n")
