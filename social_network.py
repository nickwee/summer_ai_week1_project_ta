#Various import Statements can go here
from  social_network_classes import SocialNetwork,Person
import social_network_ui



#Create instance of main social network object
ai_social_network = SocialNetwork()

#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            ai_social_network.create_account()

        elif choice == "2":
            currentUser = None
            username = input("Please sign in with your username: ")
            while all(user.username != username for user in ai_social_network.list_of_people):
                username = input("Username does not exist, please try again: ")
            currentUser = ai_social_network.getCurrentUser(username)
            inner_menu_choice = social_network_ui.manageAccountMenu()
            #Handle inner menu here
            while True:
                if inner_menu_choice == "1":
                    editDetailsChoice = social_network_ui.editDetailsMenu()
                    while True:
                        if editDetailsChoice == "1":
                            newUsername = input("Please enter your new username: ")
                            currentUser.setName(newUsername)
                        elif editDetailsChoice == "2":
                            newAge = input("Please enter your new age: ")
                            currentUser.setAge(newAge)
                        elif editDetailsChoice == "3":
                            break
                        else:
                            print("Your input is invalid. Try Again! ")
                        #restart menu
                        editDetailsChoice = social_network_ui.editDetailsMenu()
                elif inner_menu_choice == "2":
                    friend = input("Who would you like to add as a friend? ")
                    currentUser.add_friend(friend, ai_social_network)
                elif inner_menu_choice == "3":
                    currentUser.viewFriendList()
                elif inner_menu_choice == "4":
                    currentUser.viewFriendList()
                    blockedFriendName = input("Who would you like to block? ")
                    currentUser.blockFriend(blockedFriendName, ai_social_network)
                elif inner_menu_choice == "5":
                    currentUser.viewFriendList()
                    friendName = input("Who would you like to send a message to? ")
                    currentUser.sendMessage(friendName, ai_social_network)
                elif inner_menu_choice == "6":
                    currentUser.viewMessages()
                elif inner_menu_choice == "7":
                    break
                else:
                    print("Your input is invalid. Try Again! ")

                #restart menu
                inner_menu_choice = social_network_ui.manageAccountMenu()

        elif choice == "3":
            print("Thank you for visiting. Goodbye!")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()



        
