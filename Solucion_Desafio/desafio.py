nota1 = float(input("Ingresa la calificación 1: "))
nota2 = float(input("Ingresa la calificación 2: "))
nota3 = float(input("Ingresa la calificación 3: "))
nota4 = float(input("Ingresa la calificación 4: "))
nota5 = float(input("Ingresa la calificación 5: "))

promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

print("El promedio es:", promedio)

if promedio >= 60:
    print("Aprobado")
elif promedio >= 40 and promedio < 60:
    print("En recuperación")
else:
    print("Reprobado")


