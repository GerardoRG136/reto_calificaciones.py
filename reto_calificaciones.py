#Programa que calcula calificaciones
print("Este es un programa que te ayudara a calcular tus calificaciones.")
examen = float(input("Ingresa tu calificación del examen: "))
asignaciones = float(input("Ingresa tu numero de asignaciones: "))
participacion = (input("¿Cuentas con participación? Si/No: "))
if examen >= 70:
  if asignaciones >= 5:
    print("Estas aprobado")
  else:
    print("Estas reprobado")
elif examen< 70:
  if participacion == "Si":
    print("Estas aprobado")
  else:
    print("Estas reprobado")
else:
  print("Estas reprobado")
