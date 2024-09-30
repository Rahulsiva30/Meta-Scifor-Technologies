a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
d = int(input("d:"))
e = int(input("e:"))
avg = a + b + c + d + e
if avg <= 35:
    print("additonal class is required:", avg / 5)
else:
    print("you are good:", avg / 5)

# or

a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
d = int(input("d:"))
e = int(input("e:"))
avg = (a + b + c + d + e) / 5
if avg <= 35:
    print("additonal class is required:", avg)
else:
    print("you are good:", avg)

a = []
print("enter the 5 numbers:")
for i in range(5):
    print("enter the number" + str(i + 1))
    num = int(input())
    a.append(num)
print(a)

sum = 0
for i in a:
    sum = sum + i
print(sum)

print("average of the numbers:")
avg = sum // 5
print(avg)


sum = 0
for i in range(1, 8):
    sum = sum + i
    print(i)
print(sum)


def mul():
    a = int(input("enter the num1:"))
    b = int(input("enter the num2:"))
    print(a * b)


mul()


def div():
    a = int(input("enter the num1:"))
    b = int(input("enter the num2:"))
    print(a % b)


div()


def painter(msg):
    print("painter:", msg)


painter("hello sir")


def hello(a):
    if a >= 50:
        print("pass")
    else:
        print("fail")


a = int(input("enter the num:"))
hello(a)


def printrange(r1, r2):
    for i in range(r1, r2):
        print(i)


a = 10
b = 15
printrange(a, b)


a = [i for i in range(1, 40) if i % 2 == 0 and i % 5 == 0]
print(a)


def painter():
    return "im a good painter"


print(painter())


def painter():
    return "hello painter"


a = painter()
print(a)


s_username = "rahul"
s_password = 12345

name = input("enter the name:")
password = int(input("enter the password:"))


def validate():
    if s_username == name and s_password == password:
        return True
    else:
        return False


a = validate()
print(a)


def add(n1, n2):
    return n1 + n2


a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))

added = add(a, b)
result = added * c

print(result)


class chennai:
    age = 23
    name = ""

    def beach(self):
        print("welcome to chennai beach")

    def museum(self):
        print("welcome to the museum")


rahul = chennai()
siva = chennai()

rahul.museum()
rahul.age
siva.beach()
siva.name = "SIVA"
print(rahul)
print(siva)
print(rahul.age)
print(siva.name)


class laptop:
    price = ""
    processor = ""
    battery = ""


lenovo = laptop()
dell = laptop()

lenovo.price = 45000
lenovo.processor = "i7"
lenovo.battery = "10000mah"

dell.price = 50000
dell.processor = "i7"
dell.battery = "12000mah"

print(lenovo.price)
print(dell.battery)


class student:
    def __init__(self):
        self.name = "rahul"
        self.regno = 221706592

    def display(self):
        print("name:", self.name)
        print("regno:", self.regno)


stud1 = student()
stud2 = student()
stud1.name = "rahul"
stud1.regno = 221706593
stud2.name = "siva"
stud2.regno = 221706594
stud1.display()
stud2.display()


class fruit:
    def __init__(self, col):
        self.color = col


apple = fruit("red")
print(apple.color)


class teacher:
    def __init__(self, na, reg):
        self.name = na
        self.regno = reg

    def display(self):
        print(t1.name)
        print(t1.regno)
        print(t2.name)
        print(t2.regno)


t1 = teacher("rahul", 221706592)
t2 = teacher("siva", 221706593)
t1.display()


class teacher:
    def __init__(self, na, reg):
        self.name = na
        self.regno = reg

    def display(self):
        print("name:", self.name)
        print("regno:", self.regno)


t1 = teacher("rahul", 221706592)
t2 = teacher("siva", 221706593)
t1.display()
t2.display()


class mobile:
    screen = "amoled"

    def __init__(self, br, ch, ca):
        self.brand = br
        self.charger = ch
        self.camera = ca

    def display(self):
        print("BRAND:", self.brand)
        print("CHARGER:", self.charger)
        print("CAMERA:", self.camera)
        print("SCREEN:", self.screen)


realme = mobile("realme", "4500mah", "64mp")
redmi = mobile("redmi", "4000mah", "13mp")

realme.display()
redmi.display()


# inheritance
class dad:
    def phone(self):
        print("dad's phone")


class mom:
    def food(self):
        print("mom's food")


class son(dad, mom):
    def laptop(self):
        print("son's laptop")


rahul = son()
rahul.laptop()
rahul.phone()
rahul.food()


class dad:
    def money(self):
        print("dad's money")


class mom(dad):
    def sweet(self):
        print("mom's sweet")


class son(mom):
    def mobile(self):
        print("son's mobile")


rahul = son()
m1 = mom()
rahul.mobile()
m1.money()
rahul.money


# super keyword
class a:
    def __init__(self):
        print("A")

    def display1(self):
        print("hello a")


class b(a):
    def __init__(self):
        super().__init__()
        print("B")

    def display2(self):
        print("hello b")


class c(b):
    def __init__(self):
        super().__init__()
        print("C")


obj1 = c()


class animal:
    def sound(self):
        print("animal makes a sound")


class dog(animal):
    def sound(self):
        print("dog barks")


class bird(animal):
    def sound(self):
        print("birds sing")


obj1 = bird()
obj1.sound()


# private encapsulation(__)
class company:
    def __init__(self):
        self.__hello = "google"

    def display(self):
        print(self.__hello)


obj1 = company()
obj1.display()


# protected (_)
class company:
    def __init__(self):
        self._hello = "apple"


class company2(company):
    pass


ob2 = company2()
print(ob2._hello)


# exception handling
try:
    a = int(input())
    b = int(input())
    print(a + b)

except Exception:
    print("only numbers allowed")

# different types of error
try:
    a = int(input())
    b = int(input())
    print(a + b)


except TypeError:
    print("typeerror")

except ValueError:
    print("valueerror")

except Exception as e:
    print("only numbers allowed", e)


# finally
try:
    a = int(input())
    b = int(input())
    print(a + b)


except TypeError:
    print("typeerror")

except ValueError:
    print("valueerror")

except Exception as e:
    print("only numbers allowed", e)

finally:
    print("done")
