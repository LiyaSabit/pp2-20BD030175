import math
def converter(deg):
    rad = deg * math.pi/180
    return rad
deg = int(input("Input degree:"))
# print("Output radian:", format(converter(deg), '.6g'))
def trap(h, a , b):
    area = (a + b)/2 *h
    return area
h = int(input("Height:"))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))
print("Expected Output:", trap(h, a, b))
def polygon(side, lenth):
    apothem = lenth/(2* math.tan(180/side * math.pi /180))
    area = apothem*(side*lenth)/2
    area = int(area)
    return area
side = int(input("Input number of sides: "))
lenth = int(input("Input the length of a side: "))
# print("The area of the polygon is:", polygon(side, lenth))
def parallelogram(a,h):
    area = a*h 
    return area 
a = int(input("Length of base: "))
h = int(input("Height of parallelogram: "))
print("Expected Output: ", "{:.1f}".format(parallelogram(a, h)))