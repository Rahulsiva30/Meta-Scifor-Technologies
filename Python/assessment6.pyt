# print the highest value's name in the dictionary.
emp = {"jack": 75000, "jude": 85000, "jerry": 15000, "jill": 50000, "jenny": 55000}
val = max(emp, key=emp.get)
val1 = max(emp.keys(), key=(lambda k: emp[k]))
print(val, emp[val1])

# sort the dictionary with the value
d = {"key 1": "Apple", "key 2": "Mango", "key 3": "Pineapple", "key 4": "cherry"}
d1 = sorted(d.items(), key=lambda x: x[1])
print(d1)

# write a program to  removes duplicate characters from the string
a = "python programming language"
b = ""
for i in a:
    if i not in b:
        b += i
print(b)


""" a=[1,2,[3,[4,5,6,[9,8,10],88,99],[111,222,[3,344,[44,55],888],99],10010]]
 i) first 99 delete
 ii) instead of 8->8888
 iii) instead of 55--> your name
 iv) pop second 99 """

a = [
    1,
    2,
    [3, [4, 5, 6, [9, 8, 10], 88, 99], [111, 222, [3, 344, [44, 55], 888], 99], 10010],
]
del a[2][1][5]
a[2][1][3][1] = 8888
a[2][2][2][2][1] = "rahul"
a[2][2].pop(3)
print(a)
