import math

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

part_1 = math.sqrt(-b + (b ** 2) - 4 * (a * c))
part_2 = 2 * a
part_3 = part_1 / part_2

part_4 = math.sqrt(-b - (b ** 2) - 4 * (a * c))
part_2 = 2 * a
part_5 = part_4 / part_2

print(part_3)
print(part_5)



