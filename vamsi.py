"""
This program is based on simple design on chatbot...
1.The Bot starts with greeting, self introduction   and ask for the name of the person
2.The bot will greet and welcome the person
3.Bot will ask the person want to do, it will offer a choice of things based upon the bot design
4.It will respond to users to input correctly
"""

import random
from datetime import datetime
def Greetings():
    #list of responses from Bot
    response=["Nice to meet you."  
    " It's Great to see you."
    " Iam a simple chatbot and having 2 features."
    " I can help you do some calulations and also asking some questions."]
    #selecting a response at random and returning
    return random.choice(response)


# Greets the person based upon time of day
def time_Of_The_Day():
    curr_time=datetime.now()
    Greetings_time="Good Morning"
    if curr_time.hour>=12 and curr_time.hour<=16:
        Greetings_time="Good AfterNoon"
    elif curr_time.hour>=17 and curr_time.hour<=19:
        Greetings_time="Good Evening"
    elif  curr_time.hour>=20:
        Greetings_time="Good Night"
    return Greetings_time



#bot welcomes the person with his name 
def welcome_Greetings():
    name=input("Enter your name:")
    print(f"{time_Of_The_Day()},{name} {Greetings()}")



def menu():
    print("1.Calculate an expression")
    print("2.Asking Question and Answering")
    print("3.End this chat")
    print("-----------------------------------------------------")
    try:
        return int(input("Enter your choice from [1-3]:"))
    except:
        print("Sorry,you have to enter a choice from [1-3]")



def evaluation():
    expr=input("Enter expression: ")
    try:
        print("Result of the expression: ",eval(expr))
    except Exception as e:
        print(e)



def Asking_Questions():
    print("Simple Question and Answer program")
    print(".........")
    print("You can ask any question from this:")
    print("Hi")
    print("How are you?")
    print("What did you do yesterday?")
    print("Shall we go for a movie?")
    print("Good bye")
    while True:
        Ques=input("Enter one question from above list:")
        Ques=Ques.lower()
        if Ques in ['hi']:
            print("Hello")
        elif Ques in ['how are you?']:
            print("I am fine")
        elif Ques in ['what did you do yesterday?']:
            print("Yesterday, I played cricket with my friends.")
        elif Ques in ['shall we go for a movie?']:
            print("Sure")
        elif Ques in ['good bye']:
            print("Good bye. We will meet you again.")
        elif Ques in ['quit']:
            break
        else:
            print("I don't understand what you are saying...")
        


def bot():
    welcome_Greetings()
    choice=menu()
    while choice!=3:
        if(choice==1):
            evaluation()
        elif(choice==2):
            Asking_Questions()
        else:
            print("Oops,I didnt get it!")
        choice=menu()

bot()