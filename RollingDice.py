import random
print("This is a dice simulator")
x="y"
while x=="y":
    number = random.randint(1,6)
    if number==1:
        print("___________")
        print("|         |")
        print("|    O    |")
        print("|         |")
        print("___________")
    if number==2:
        print("___________")
        print("| O       |")
        print("|         |")
        print("|       O |")
        print("___________")
    if number==3:
        print("___________")
        print("| O       |")
        print("|    O    |")
        print("|       O |")
        print("___________")
    if number==4:
        print("___________")
        print("| O     O |")
        print("|         |")
        print("| O     O |")
        print("___________")
    if number==5:
        print("___________")
        print("| O     O |")
        print("|    0    |")
        print("| O     O |")
        print("___________")
    if number==6:
        print("___________")
        print("| O     O |")
        print("| O     O |")
        print("| O     O |")
        print("___________")
    x= input("Want to roll the dice? enter y \n or Done? enter n  ")
