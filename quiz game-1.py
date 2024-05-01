print("welcome to my computer quiz")
playing = input("Do you want to play?")

if playing != "yes":
    quit()

print("okay! Let's play: )")
score = 0

answer = input("What is the capital city of australia? ")
if answer == "Canberra":
    print("correct!")
    score +=1
else:
    print('incorrect!')


answer = input("what is the chemical symbol for gold? ")
if answer == "Au":
    print("correct!")
    score +=1
else:
    print('incorrect!')

answer = input("what is the national flower of England? ")
if answer == "Rose":
    print("correct!")
    score +=1
else:
    print('incorrect!')

answer = input("Andhra pradesh was separated from which state? ")
if answer == "Madras":
    print("correct!")
    score +=1
else:
    print('incorrect!')

print("you got" + str(score) +" questions correct!")




    