Yourname=input("What is your name?")
Yourage=int(input("What is your age?"))
Compage = int(input("What's the age you want to compare to?"))

if Yourage>Compage:
    print(f"You are {Yourage-Compage} years over {Compage}")
elif Yourage==Compage:
    print(f"You are exactly {Compage} years old")
else:
    print(f"You are {Compage-Yourage} years younger than {Compage}")
