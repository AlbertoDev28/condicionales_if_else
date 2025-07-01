
#calcular promedio
print("Calcular el promedio de un alumno \n")

nombre = input("escriba su nombre completo: ").capitalize()
matematica = int(input("Escriba la nota de matematica: "))
quimica = int(input("Escriba la nota de quimica: "))
biologia = int(input("Escriba la nota de biologia: "))

promedio = (biologia+matematica+quimica) / 3

print(f"\nNotas del alumno: {nombre}")

if matematica >= 5:
    print("APROBASTE MATEMATICAS")
else:
    print("REPROBASTE MATEMATICAS")

if quimica >= 5:
    print("APROBASTE QUIMICA")
else:
    print("REPROBASTE QUIMICA")

if biologia >= 5:
    print("APROBASTE BIOLOGIA")
else:
    print("REPROBASTE BIOLOGIA")

print(f"\nTu promedio es: ", round(promedio, 2))  # metodo round coloca los ultimos 2 decimales del numero