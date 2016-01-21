import math

radius = float(input("Input radius in cm: "))

length = float(input("Input length in cm: "))

area = math.pi * radius * radius
volume = area * length

print(volume)
