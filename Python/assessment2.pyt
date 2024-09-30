# while loop in python
# ex-1 print even numbers from 2 to 20
num = 2
while num <= 20:
    print(num)
    num += 2

# ex-2 sum of the numbers from 1 to 100
sum = 0
num = 1
while num <= 100:
    sum += num
    num += 1
print(sum)

# ex-3 print num from 10 to 1
i = 10
while i > 0:
    print(i)
    i-=1

# ex-4 calc the factorial of a number
num = int(input("enter a number:"))
fact = 1
while num > 0:
    fact *= num
    num -= 1
print(fact)

# ex-5 find the largest number in a list
Num = [12, 45, 78, 34, 56, 89]
l = 0
max = Num[0]
while l < len(Num):
    if max < Num[l]:
        max = Num[l]
    l += 1
print(max)

# ex-6 reverse a string
name = "hello,world!"
output = ""
i = len(name) - 1
while i >= 0:
    output = output + name[i]
    i -= 1
print(output)

# ex-7 sum of a given numbers
num = int(input("enter the number:"))
sum = 0
while num > 0:
    temp = num % 10
    sum += temp
    num = num // 10
print(sum)

# ex-8 count of even and odd numbers in a list
num = [12, 45, 78, 34, 56, 89]
l = 0
even = 0
odd = 0
while l < len(num):
    if num[l] % 2 == 0:
        even += 1
    else:
        odd += 1
    l = l + 1
print(f"even numbers:{even} \nodd numbers:{odd}")

# ex-9 calc the average of numbers in a list
Numbers = [12, 45, 78, 34, 56, 89]
i = 0
total = 0
while i < len(Numbers):
    total += Numbers[i]
    average = total/len(Numbers)
    i += 1
print("average of the numbers:", average)

# ex-10 count the num of vowels
text = "apple pie"
vowels = "AEIOUaeiou"
l = 0
count = 0
while l < len(text):
    if text[l] in vowels:
        count += 1
    l += 1
print(count)
