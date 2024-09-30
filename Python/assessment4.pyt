# 1)Python program to concatenate following dictionaries to create a new one.

# update()
a = {"Name": "Ram", "Age": 23}
b = {"City": "Salem", "Gender": "Male"}
c = {}
c.update(a)
c.update(b)
print(c)

# unpacking operator
a = {"Name": "Ram", "Age": 23}
b = {"City": "Salem", "Gender": "Male"}
c = {**a, **b}
print(c)

# 2)Python program to iterate over dictionaries using for loops.
a = {"City": "Salem", "Gender": "Male"}
for key, values in a.items():
    print("keys:", key)
    print("values:", values)

# 3) minimum value from the following dictionary
# mininimum()
a = {"sam": 65, "ram": 75, "raju": 32}
print(min(a, key=a.get))


# 4)program to sort dictionary by values (Ascending/ Descending)
a = {"sam": 65, "ram": 75, "raju": 32}
a = dict(sorted(a.items(), key=lambda x: x[1]))
print(a)

# 5)program to count the number of items stored in a list
a = [15, 20, 56, 45, 62]
count = 0
for i in a:
    count += 1
print(count)

# 6)program to reverse a list in Python
a = [15, 20, 56, 45, 62]
print(a[::-1])


# 7)program to remove an empty element from a list
num = ["hello", 34, 45, "", 40]
num.remove("")
print(num)

# 8)program to display those items from a list that is divisible by 5
a = [15, 23, 78, 20, 25, 94, 35]
b = []
for i in a:
    if i % 5 == 0:
        b.append(i)
print(b)
