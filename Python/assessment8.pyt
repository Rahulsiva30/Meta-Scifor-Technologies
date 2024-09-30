# 1. Write a python program generate a function to filter out the repeated string in a given list
a = [8, 2, 3, 4, 5, 6, 6, 4, 5]


def filter(b):
    b = set(a)
    print(b)


filter(a)


# 2. Write a python program to generate a function to accept an input string therefore count the number of lowercase and uppercase respectively.
name = input("enter the string:")


def count(name):
    ucount = lcount = 0
    for i in name:
        if i.isupper():
            ucount += 1
        elif i.islower():
            lcount += 1
    print("uppercae:", ucount)
    print("lowercase:", lcount)


ucount = lcount = count(name)


# 3. Write a python program to generate a function to combine different integer into one integer without undergoing normal mathematics operation.
a = [2, 8, 32, 6, 5]
a = "".join(map(str, a))
print(a)

# 4. Write a python function to check whether the given list a and list b consist any repeated items.
list_a = ["python", "exercise", "tutorial", "practice"]
list_b = ["python", "exercise", "tutorial", "practice", "tutorial"]


def displaY(a):
    i = list(set(a))
    if len(a) == len(i):
        return True
    else:
        return False


print("repeated items:", displaY(list_a))
print("repeated items:", displaY(list_b))
