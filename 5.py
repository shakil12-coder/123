print("This is a program that convert second into hours minuts and second")

second = int(input("Enter Second: "))

minutes = int(second / 60)
hours = int(minutes / 60)
minutes = int(minutes%60)
second = int(second % 60)

print("Hours: ", hours,"\nminutes: ", minutes,"\nSecond: " ,second)
