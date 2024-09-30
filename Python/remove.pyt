# remove
a = {"css", "java", "python"}
a.remove("css")
print(a)

# pop
s = {"python", "css"}
s.pop()
print(s)

# union
a = {1, 2, 3}
b = {4, 5, 6}
print(a.union(b))

# difference
a = {1, 2, 3, 4, 5, 6}
b = {1, 2, 3, 4, 5, 6, 7, 8}
print(a.difference(b))

# symmetric difference
a = {1, 2, 3, 4, 5, 6}
b = {1, 2, 3, 4, 5, 6, 7, 8}
print(a.symmetric_difference(b))

# issubset
a = {1, 2, 3, 4, 5}
b = {1, 2, 3, 4, 5, 6, 7, 8}
print(a.issubset(b))

# issupset
a = {1, 2, 3, 4, 5, 6}
b = {1, 2, 3, 4, 5, 6, 7, 8}
print(a.issuperset(b))
