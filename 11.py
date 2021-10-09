
print("This is program to calculate compound interest")

p = float(input("Enter principle: "))
r = float(input("Enter rate: "))
t = float(input("Enter time: "))

compound_interest = (p * (1 + (r/100))** t )- p

print("compound interest is ", compound_interest)
