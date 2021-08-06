import random
DatRandomnumber=random.randint(1,100)
while True:
    Yourguess=int(input("Guess a number."))
    if Yourguess>DatRandomnumber:
        print("Your guess is bigger than the number ")
    elif Yourguess==DatRandomnumber:
        print("You are right with that guess!")
        break
    else:
        print("Your guess is smaller than the number ")