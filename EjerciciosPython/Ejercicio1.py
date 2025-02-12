
#Day 3 Exercises

age = 45
height = 1.88
complexNumber = 1 + 8j
base = int(input("Enter the base of the triangle: "));
height = int(input("Enter the height of the triangle: "));
area = (base * height) / 2;
print("The area of the triangle is: ", area);

a = int(input("Enter the side a: "))
b = int(input("Enter the side b: "))
c = int(input("Enter the side c: "))
perimeter = (a + b + c)
print("The perimeter of the triangle is: ", perimeter)

#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
area = length * width
perimeter = 2 * (length + width)
print("The area of the rectangle is: ", area)
print("The perimeter of the rectangle is: ", perimeter)


#Get the radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius = int(input("Enter the radius of the circle: "))
area = 3.14 * radius * radius
circumference = 2 * 3.14 * radius
print("The area of the circle is: ", area)
print("The circumference of the circle is: ", circumference)

#Calculate the slope, x-intercept and y-intercept of y = 2x -2
x = 0
y = 2*x - 2
print("The y-intercept is: ", y)
x = 1
y = 2*x - 2
print("The slope is: ", y)
y = 0
x = (y + 2) / 2
print("The x-intercept is: ", x)
    
