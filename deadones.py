start = '''
A zombie apocalypse has started in Massachusetts and your current location is in California
What will be your first reaction. Start preparing for it or wait for it to come.
'''

print(start)



print("Type 'prepare now' or Type 'wait' for your choice.")
user_input = input()
if user_input == "prepare now":
    print("You have gotten supplies to help you surivive the apacolypse.")
#add monicas code here













#this is my part of the code
elif user_input == "wait":
    print("Now you have another option.....you can wait it off like you said you would or move to another country and wait there. ")
    print("Type 'wait' again to stay where you are or type 'move' to go to another country.")
user_input = input()
if user_input =="wait":
    print("okay now your for sure stayign where you are")
# add tina's code here
elif user_input == "move":
    print("okay now you have moved to any country of your choice..remember you can only move once..you cant move again..its not an option. Sorry.")
    print("you have lived a care free life for only a few months....ohh gosh...they're already here..the time has come when they have arrived to your country..sadly you can move anymore..tears..")
print("But dont feel down...you have another option. you have a little bit of time. But only enough time to prepare for the invasion or you can wait for it again")
print("Type 'prepare now' to...well its pretty straight forward, and type 'wait' to wait for the zombies")

user_input = input()
if user_input == "wait":
    print("Now zombies have have attacked your home. You are unprepared..oops...definetly not the best choice since the zombie have eaten you alive. But you have turned into a zombie so its all good")
# add monicas code here with an elif also add the ending restart here
