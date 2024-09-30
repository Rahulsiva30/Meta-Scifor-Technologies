# 1. Write a Python function to find the maximum of three numbers
def numbers(a, b, c):
    maximum = max(a, b, c)
    print(maximum)


numbers(20, 32, 14)


# 2. Write a Python program to reverse a string.
def reverse(a):
    b = a[::-1]
    print(b)


reverse(a="hello world!!")


# 3. Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30.
def squares(a):
    for i in range(1, a + 1):
        i = i**2
        print(i)
        i += 1


squares(a=30)


# 4. Write a Python program to solve the Fibonacci sequence using recursion.
def fib(n):
    a = 0
    b = 1
    print(a)
    print(b)
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
        print(c)

fib(10)


# 5. Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2500 (both included).
def div(a, b):
    for i in range(a, b + 1):
        if i % 7 == 0 and i % 5 == 0:
            print(i, end=",")
    print()


div(1500, 2500)


# 6. Write a Python program to count the number of even and odd numbers in a series of numbers
def numbers(a):
    ceven=0
    codd=0
    for i in range(1, a+1):
        if i%2==0:
            ceven+=1
        else:
            codd+=1
    print(f"even numbers: {ceven} odd numbers:{codd}")

numbers(10)



# 7. Write a Python program to sum two integers. However, if the sum is between 15 and 20 it will return 20.
def sum(a, b):
    c = a + b
    if c in range(15, 20):
        return 20


print(sum(13, 3))

# 8. Write a Python program that checks whether a string represents an integer or not.
string = "25"
print(string.isnumeric())

# 9. Write a Python program to create the multiplication table (from 1 to 10) of a number.
a = 2
for i in range(1, 11):
    print(i, "X", a, "=", i * 2)

# 10. Write a Python program to count the number of characters (character frequency) in a string.
st = "python programming"
charfrequency = {}.fromkeys(st, 0)
for i in st:
    charfrequency[i] += 1
print(charfrequency)
