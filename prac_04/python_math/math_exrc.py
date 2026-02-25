#Convert degree to radian
import math

degree = 15
radian = degree * (math.pi / 180)

print("Output radian:", round(radian, 6))



#Area of a trapezoid
height = 5
base1 = 5
base2 = 6

area = 0.5 * height * (base1 + base2)

print("Expected Output:", area)



#Area of a regular polygon
import math

n = 4
s = 25

area = (n * s**2) / (4 * math.tan(math.pi / n))

print("The area of the polygon is:", round(area))



#Area of a parallelogram
base = 5
height = 6

area = base * height

print("Expected Output:", float(area))


