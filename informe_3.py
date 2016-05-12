import math
x= int(input("ingrese un numero de lados para identificar y calcular una figura geometrica : "))

def area_perim_triangulo():
    s = (a + b + c)/2
    t = s * (s - a) * (s - b) * (s-c)
    v1 = math.sqrt(t)
    print (round(v1,2))

def perim_area_cuadrado():
    A = l * l
    p = 4 * l
    print (A)
    print (p)

def perim_area_pentagono():
    P = l * 5
    c = l / 2
    v = (d * d) - (c * c)
    a = math.sqrt(v)
    A = (P * a) / 2
    print (round(P,2))
    print (round(A,2))

if x == 2:
    print('no hay figuras de solo dos lados')

elif x == 3:
    a = int(input("ingrese el primer lador del triangulo : "))
    b = int(input("ingrese el segundo lador del triangulo : "))
    c = int(input("ingrese el tercer lador del triangulo : "))
    triangulo = area_perim_triangulo()
    print (triangulo)

elif x == 4:
    l = int(input("ingrese el lado del cuadrado : "))
    cuadrado = perim_area_cuadrado()
    print (cuadrado)

elif x == 5:
    l = int(input("ingrese el valor del lado del pentagono : "))
    d = int(input("ingrese el valor del centro del pentagono a una de sus angulos : "))
    pentagono = perim_area_pentagono()
    print (pentagono)