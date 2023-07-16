x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

c = abs(x1 - x2)
d = abs(y1 - y2)

area_one = c * d
perimeter_one = 2 *(c + d)

area = int(area_one)
perimeter = int(perimeter_one)

print(str(area))
print(str(perimeter))

