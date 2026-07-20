import random
'''
1 for snake
0 for gun
-1 for water
'''
computer = random.choice([1,-1,0])
youstr =input("Enter you choice: ")
youDict = { "s":1, "g":0, "w":-1}
reverseDict = { 1: "Snake", 0:" Gun", -1: "Water"}

you = youDict[youstr]

#by now we have two numbers(variables), you and computer

print (f"You choose {reverseDict[you]}\n Computer choose {reverseDict[computer]}")

if (computer == you):
    print("It's a Draw. ")

else:
    if(computer == -1 and you == 0):
        print("You Loss!")

    elif(computer == 1 and you == 0):
        print("You Loss!")

    elif(computer == -1 and you == 1):
        print("You Win!")

    elif(computer ==1 and you == -1):
        print("You Loss!")

    elif(computer == 0 and you == 1):
        print("You Win!")
    
    elif(computer ==0 and you == -1):
        print("You Win!")

    else:
        print("Something went wrong")
