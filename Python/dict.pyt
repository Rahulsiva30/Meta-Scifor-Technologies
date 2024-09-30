# dictionary
a = {"colour": "red", "name": "ramen", "quality": "good", "taste": "delicious"}
a = a.keys()
print(a)

# dictionary_add
a = {"colour": "red", "name": "ramen", "quality": "good", "taste": "delicious"}
a["price"] = "cheap"
print(a)

# dictionary_delete
a = {"colour": "red", "name": "ramen", "quality": "good", "taste": "delicious"}
del a["taste"]
print(a)

# dictionary_update
a = {"colour": "red", "name": "ramen", "quality": "good", "taste": "delicious"}
a.update({"colour": "blue", "name": "sushi", "quality": "ok", "taste": "normal"})
print(a)

# dictionary_key
a = {"name": "rahul", "age": "23", "course": "python"}
for key in a:
    print(key)

# dictionary_values
a = {"name": "rahul", "age": "23", "course": "python"}
for values in a:
    print(values)

# dictionary_key,values items()
a = {"name": "rahul", "age": "23", "course": "python"}
for key, values in a.items():
    print(key, values)

# dictionary_key,values and items in list
a = {"name": "rahul", "age": "23", "course": "python"}
b = []
for key in a.keys():
    b.append(key)
print(b)

a = {"name": "rahul", "age": "23", "course": "python"}
b = []
for values in a.values():
    b.append(values)
print(b)

a = {"name": "rahul", "age": "23", "course": "python"}
b = []
c = []
for key, values in a.items():
    b.append(key)
    c.append(values)
print(b)
print(c)


# dictinary present or not
a = {"name": "rahul", "age": 23, "course": "python"}
b = "name"
if b in a:
    print("present")
else:
    print("not present")

a = {"name": "rahul", "age": 23, "course": "python"}
b = 23
if b in a.values():
    print("present")
else:
    print("not present")

# dictionary sum of the values
a = {"d": 2, "e": 3, "f": 6, "g": 4, "h": 8}
sum = 0
for i in a.values():
    sum = sum + i
print(sum)


# dictionary first letter
a = {"rahul": 1000, "ram": 1500, "siva": 2000, "jack": 1000, "sam": 1250}
letter = input("enter the letter:")
for key, values in a.items():
    if key.startswith(letter):
        print("key:values", key, values)


# dictionary length
a = {"rahul": 1000, "ram": 1500, "siva": 2000, "jack": 1000, "sam": 1250}
length = int(input("enter the length:"))
for key in a.keys():
    if len(key) == length:
        print(key)

# mult dict
a = {b: b * b for b in range(1, 15)}
print(a)

# print the key values in upper()
a = {"a": 1, "b": 3, "c": 4, "d": 7, "e": 5}
result = {key.upper(): values for key, values in a.items() if values > 1}
print(result)

# print the upper() alphabets only
a = {"a": 1, "B": 3, "c": 4, "D": 7, "e": 5, "F": 8}
result = {key: values for key, values in a.items() if key.isupper()}
print(result)


# print only the numbers from the string
a = "he is 23 years old and his height is 6 , and the year of born is 2000"
result = [i for i in a.split() if i.isalnum()]
print(" ", result)
print(",".join(result))

# print the given string and length in dictionary
a = "python is a high level language"
result = {key: len(key) for key in a.split()}
print(result)

a = "python is a high level language"
result = {key: len(key) for key in a.split() if len(key) > 3}
print(result)

# print numbers in reverse using list
result = [i for i in range(15, 0, -1)]
print(result)

result = [i for i in range(15, 0, -1) if i % 2 != 0]
print(result)
