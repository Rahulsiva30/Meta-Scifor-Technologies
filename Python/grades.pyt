# grades
grade = int(input("enter the percentage:"))
if grade >= 90:
    print("GRADE A")
elif grade >= 80 and grade <= 90:
    print("GRADE B")
elif 70 <= grade < 80:
    print("GRADE C")
else:
    print("MAKE PROGRESS")


# leapyear using function
input_year = int(input("enter the year:"))


def is_leap(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False


if is_leap(input_year):
    print("it is a leap year")
else:
    print("it is not a leap year")


# leapyear without function
year = int(input("enter the year:"))
if year % 400 == 0:
    print("it is a leap year")
elif year % 4 == 0 and year % 100 != 0:
    print("it is a leap year")
else:
    print("not a leap year")


# tables
num = int(input("enter the number:"))
for i in range(1, 10):
    print(num, "*", i, "=", num * i)

# tables using format
num = int(input("enter the number:"))
for i in range(1, 10):
    print("{}*{}={}".format(num, i, (num * i)))
