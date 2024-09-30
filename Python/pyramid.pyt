# display "*" using for loop
for i in range(5):
    for j in range(6):
        print("*", end="")
    print()

# display "*" using for loop left downward pyramid
for i in range(6):
    for j in range(1, i + 1):
        print("*", end="")
    print()

# display "*" using for loop right downward pyramid
for i in range(5):
    for j in range(i, 5):
        print("*", end="")
    print()

# display "*" a pyramid
for i in range(6):
    for j in range(1, i + 1):
        print("*", end="")
    print()
for i in range(4, 0, -1):
    for j in range(1, i + 1):
        print("*", end="")
    print()
