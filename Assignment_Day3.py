
# 1. Factorial using Recursion
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
n = int(input("Enter the number : "))
print("Factorial is:",fact(n))


# 2. Factorail
a = int(input("Enter a number : "))
fact = 1
while a>=1:
    fact = fact*a
    a = a-1
print("The factorail of number is : ",fact)



# 3.Area of triangle,rectangle and square
def triangle(b,h):
    c = 0.5*b*h
    print("The area of Triangle is:",c)
def rectangle(l,br):
    a = l*br
    print("The area of Rectangle is:",a)
def square(x):
    d = x*x
    print("The area of Square is:",d)
b = int(input("Enter the base of triangle:"))
h = int(input("Enter the height of triangle:"))
triangle(b, h)
l = int(input("Enter the length of rectangle:"))
br = int(input("Enter the width of rectangle:"))
rectangle(l, br)
x = int(input("Enter the side of a square:"))
square(x)



# 4. Multi-level Inheritance
class Animal:
    def name(self):
        print("Animal name is Dog")
class Breed(Animal):
    def breed(self):
        print("Dog breed is Pomeranian")
class Color(Breed):
    def color(self):
        print("Dog color is orange")
class Cost(Color):
    def price(self):
        print("Dog price is 25000 Rupees")
d = Cost()
d.name()
d.breed()
d.color()
d.price()

# Multipule Inheritance
class Person:
    def name(self,name):
        self.name=name
        print(self.name)
class Age:
    def person_age(self,age):
        self.age = age
        print(self.age)
class Address(Person,Age):
    def address(self,address):
        self.address = address
        print(self.address)
d = Address()
d.name("Teju")
d.person_age(21)
d.address("Bellary")



# 5.Sum of Natural Numbers
x = int(input("Enter the number:"))
sum = 0
if x<=0:
    print("Enter a positive integer")
else:
    while x>0:
        sum = sum+x
        x = x-1
    print("sum of natural number is:",sum)

