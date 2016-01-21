sum = 0
number = input("Input number from 0 - 1000: ")

while int(number) <= 0 or int(number) >=1000:
    print("Invalid")
for i in range (len(number)):
    sum = int(number[i]) +sum

print (sum)
