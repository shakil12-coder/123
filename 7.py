print("This is a program that swap value of two numbers without using 3rd ")
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

print("before swaping a = ", a, " and b = ", b)

a = a+b
b = a-b
a = a-b

print("after swaping a = ", a, " and b = ", b)
