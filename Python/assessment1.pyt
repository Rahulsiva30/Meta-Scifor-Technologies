# 1) write a program 
for a in range(1, 51):
    if a % 3 == 0 and a % 5 == 0:
        print("fizzbuzz")
    elif a % 3 == 0:
        print("fizz")
    elif a % 5 == 0:
        print("buzz")
    else:
        print(a)

# 2) write a program
num = int(input("enter your number:"))
if num % 6 == 0:
    print("the num is div by 6")
else:
    print("the num is not div by 6")

# 3) write a program
num = int(input("enter the number from 1-7:"))
if num == 1:
    print("SUNDAY")
elif num == 2:
    print("MONDAY")
elif num == 3:
    print("TUESDAY")
elif num == 4:
    print("WEDNESDAY")
elif num == 5:
    print("THURSDAY")
elif num == 6:
    print("FRIDAY")
elif num == 7:
    print("SATURDAY")
else:
    print("enter the number between 1-7 or your entry is not found!")

# 4) write a program
signal_color = str(input("what is the color of the signal:"))
signal_color = signal_color.lower()
if signal_color == "green":
    print("you are allowed to go")
elif signal_color == "yellow":
    print("you need to wait")
elif signal_color == "red":
    print("you need to stop")
else:
    print("unrecognised color!")

# 5) write a program
grade = str(input("enter your grade:"))
grade = grade.upper()
if grade == "A":
    print("outstanding")
elif grade == "B":
    print("excellent")
elif grade == "C":
    print("very good")
elif grade == "D":
    print("good")
elif grade == "E":
    print("need to improve")
else:
    print("unregonised")
