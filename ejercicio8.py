nombre = input ("¿Cual es tu nombre?")
edad = input ("¿Cual es tu edad?")
nota1 = float (input("ingrese la primera nota: "))
nota2 = float (input("ingrese la segunda nota: "))
nota3 = float (input("ingrese la tercera nota: "))
promedio = (nota1+nota2+nota3)/3
print ("tu promedio es:",promedio)
if promedio >=71:
    print("Aprobado")
else:
    print("Reprobado")