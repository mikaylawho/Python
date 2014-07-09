from random import choice

name = raw_input("What is your name? ")
age = raw_input("What is your age? ")

adjectives = ["wet", "big", "stinky", "dumb", "whiny"]
nouns = ["turnip","dog","lump"]


def printHelloUser (username):
    print ("Hello " + username + ",") 

def printInsult (username, age):
    print ()
    if (age < 35):
        ageAdjective = "young"
    else:
        ageAdjective = "old"
        adjective = choice(adjectives)
        
    print (username + ", you are a " + ageAdjective + " " + adjective + " " + choice(nouns))


#for count in (range(10)):
#    printInsult(name, age)

userAnswer = ""

while (userAnswer != "no"):
    printInsult(name,age)
    userAnswer = raw_input("Can you take any more? Type 'no' to end. ")

