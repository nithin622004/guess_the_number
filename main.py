import random

print("2Guess the Number Game")
print("Guess between 1 and 100")

n= random.randint(1,100)
a = -1
guesses = 1
while (a != n):
    a = int(input("guess the number: "))
    if(a >n):
        print("Lower number please")
        guesses +=1
    elif(a<n):
        print("Higher number please")
        guesses +=1
        
print(f"You have guesseda it right number was {n}") 
print(f" Attempts: {guesses}")