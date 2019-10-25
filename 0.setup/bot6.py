print("Please enter 3 numbers to calculate the number of even and odd numbers")
print("First number:")
firstnum = int(input())
print("Second Number:")
secondnum = int(input())
print("Third number:")
thirdnum = int(input())

even_number = 0
odd_number = 0

if (firstnum % 2 == 0):
    even_number = even_number + 1
else: odd_number = odd_number + 1
if (secondnum % 2 == 0):
    even_number = even_number + 1
else: odd_number = odd_number + 1
if (thirdnum % 2 == 0):
    even_number = even_number + 1
else: odd_number = odd_number + 1

print ("There are",even_number,"even numbers and",odd_number,"odd numbers")
