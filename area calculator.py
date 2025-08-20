import math


def area_square():
    side = float(input("Give the length of the side of the sqaure: "))
    area = float(side * side)
    print(f'The area of the sqaure with given side {side} is {area} ')

def area_rectangle():
    length = float(input("Give the length of the rectangle: "))
    breath = float(input("Give the breath of the rectangle: "))
    area = length * breath
    print(f'The area of the rectangle with given length {length} and breath {breath} is {area} ')

def area_triangle():
    height = float(input("give height of the triangle"))
    base = float(input("Give base length of the triangle"))
    area = (height * base) / 2
    print(f'The area of the triangle with given dimension is {area} ')

def area_circle():
    radius = float(input("give radius of the circle: "))
    area = float(math.pi * radius * radius)
    print(f'Area of the given radius {radius} is {area}')

def area_calc():
    print("===============")
    print("Area Calculator")
    print("===============")
    print("              ")
    print("1) Triangle")
    print("2) Rectangle")
    print("3) Sqaure")
    print("4) Circle")

    shape = int(input("Which shape: "))

    if shape == 1 :
        area_triangle()
    elif shape == 2:
        area_rectangle()
    elif shape == 3:
        area_square
    elif shape == 4:
        area_circle()
    else:
        print("Wring input")
    
area_calc()



