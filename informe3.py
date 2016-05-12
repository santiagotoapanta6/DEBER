import math
x= int(input("ingrese un numero de lados para identificar y calcular una figura geometrica : "))

if x == 2:
    print ('no hay figuras geometricas que esten formadas solo por dos lados')

elif x == 3:
	a = int(input("ingrese el primer lador del triangulo : "))
	b = int(input("ingrese el segundo lador del triangulo : "))
	c = int(input("ingrese el tercer lador del triangulo : "))
	
	def area_perim():
		s = (a + b + c)/2
		t = s * (s - a) * (s - b) * (s-c)
		v = math.sqrt(t)
		print (round(v,2))
	triangulo = area_perim()
	print (triangulo)

elif x == 4:
    l = int(input("ingrese el lado del cuadrado : "))

    def perim_area():
    	a = l * l
    	p = 4 * l
    	print (round(a,2))
    	print (round(p,2))
    cuadrado = perim_area()
    print (cuadrado)

elif x == 5:
	l = int(input("ingrese el valor del lado del pentagono : "))
	d = int(input("ingrese el valor del centro del pentagono a una de sus angulos : "))

	def perim_area():
		P = l * 5
		c = l / 2
		v = (d * d) - (c * c)
		a = math.sqrt(v)
		A = (P * a) / 2
		print (round(P,2))
		print (round(A,2))
	pentagono = perim_area()
	print (pentagono)