# reverse the word
str = input()
print(str[::-1])

# count the num of even and odd in series
list = [2, 5, 8, 24, 28, 53, 84, 71]
even = 0
odd = 0
for i in list:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print("even  numbers:", even)
print("odd numbers:", odd)

# check the validity of the password
password = input("Enter the password:")
locase = upcase = num = spc = False
specialcharacter = "!@#$^&"
if len(password) > 8:
    for i in password:
        if i.isupper():
            upcase = True
        elif i.islower():
            locase = True
        elif i.isnumeric():
            num = True
        elif i in specialcharacter:
            spc = True
    if locase and upcase and num and spc:
        print("Valid password")
    else:
        print("Try another password")
else:
    print("Password too short")


# natural numbers in descending order
num = 10
while num:
    print(num, end=" ")
    num -= 1


# positive and negative numbers from a list
list = [1, 2, 3, 4, -7, -9, -5, -3]
p_num = []
n_num = []
for i in list:
    if i > 0:
        p_num.append(i)
    else:
        n_num.append(i)

print(f"positive num{p_num},negative num{n_num}")

# factorial of a number using while loop
i = 5
fact = 1
while i > 0:
    fact = fact * i
    i -= 1
print(fact)

# unique values in list
list = [10, 20, 30, 40, 10, 20, 40, 30, 50]
unique_list = []
for a in list:
    if a not in unique_list:
        unique_list.append(a)
print(unique_list)

# length and breadth of a rectangle from user and check if it is square or not
length = int(input())
breadth = int(input())
if length == breadth:
    print("length is equal to breath it is a square")
else:
    print("it is not a square")


# oldest and youngest in list
list = []
for i in range(3):
    list.append(int(input("enter the age:")))
print(max(list))
print(min(list))

# count vowels and consonants in a string
name = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
vowels = 0
const = 0
word = input("enter the word:")
for i in word:
    if i in name:
        vowels += 1
    else:
        const += 1
print(f"vowels:{vowels}\tconsonants:{const}")

# remove duplicates in a string
s = "aabcddeeuioo"
output = ""
for ch in s:
    if ch not in output:
        output += ch
print(output)

# count lower, upper, numeric and special characters in a string
word = input("enter the word:")
special_char = "!@#$%^&*_-"
lower, upper, numeric, spl = 0, 0, 0, 0
for i in word:
    if i.isnumeric():
        numeric += 1
    elif i.islower():
        lower += 1
    elif i.isupper():
        upper += 1
    elif i in special_char:
        spl += 1
print(f"lower:{lower} upper:{upper} numeric:{numeric} special:{spl}")
