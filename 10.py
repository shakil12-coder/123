# 3,5,7,10,11
print("Enter the sides of a triangle : ")
a=int(input())
b=int(input())
c=int(input())
s=(a+b+c)/2
d=(s*(s-a)*(s-b)*(s-c))
area=d**0.5
print("Area of triangle is : ",area)

