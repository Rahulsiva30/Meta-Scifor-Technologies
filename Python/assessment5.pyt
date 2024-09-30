# 1. Write a program to create a function that takes two arguments
def display(name, age):
    print("your name: " + name)
    print("your age: " + str(age))


display("Sam", 23)


# 2. Write a program to create a function show_employee()
def show_employee(name, salary=9000):
    print("your name:" + name)
    print("your salary:" + str(salary))


show_employee("sam")


# 3.Generate a Python list of all the even numbers between 4 to 30.
a = [i for i in range(4, 30 + 1) if i % 2 == 0]
print(a)


# 4. Define a function that accepts roll number and returns
def student(roll):
    return roll

print(student(roll=22170))
print("student is present")


# 5. Define a function in python that accepts 3 values
def numbers(a, b, c):
    print(max(a, b, c))


numbers(24, 32, 54)


# 6. Define a function which counts vowels in a word.
def vowels(word):
    str = "aeiou"
    count = 0
    for i in word.lower():
        if i in str:
            count += 1
    print(count)


vowels("hello world")


# 7. Define a function that accepts lowercase words
def words(name):
    return name.lower()


a = words("HELLO WORLD")
print(a)

# 8. Write a program to check whether a given key exists in a dictionary or not
name = {"a": "1", "b": "2", "c": "3", "d": "5"}
for key, values in name.items():
    if key == "c":
        print(f"{key} key exists")
        break
else:
    print("key does not exist")


# 9. Write a program to concatenate two dictionaries
dict1 = {"a": "1", "b": "2"}
dict2 = {"c": "3", "d": "5"}

result = {k: v for d in (dict1, dict2) for (k, v) in d.items()}
print(result)

# 10. Write a program to sum of all the values of a dictionary.
name = {"a": 1, "b": 2, "c": 3, "d": 5}
sum = 0
for i in name.values():
    sum += i

print(sum)
