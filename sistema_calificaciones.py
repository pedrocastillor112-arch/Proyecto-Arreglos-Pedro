
# Sistema de calificaciones de estudiantes
# Capitulo IX: Arreglos y vectores

# 1. Crear el vector de calificaciones
calificaciones = [85, 67, 92, 74, 58]

print("=== SISTEMA DE CALIFICACIONES ===")

# 2. Mostrar todas las calificaciones
print("\nCalificaciones originales:")

for nota in calificaciones:
    print(nota)

# 3. Consultar una calificacion mediante su indice
print("\nConsulta de una calificacion:")
print("Calificacion del tercer estudiante:", calificaciones[2])

# 4. Modificar una calificacion
calificaciones[4] = 80

print("\nSe modifico la calificacion del quinto estudiante.")

# 5. Calcular el promedio
suma = 0
aprobados = 0
reprobados = 0

for nota in calificaciones:
    suma += nota

    # 6. Verificar si el estudiante aprobo
    if nota >= 70:
        aprobados += 1
    else:
        reprobados += 1

promedio = suma / len(calificaciones)

# 7. Mostrar los resultados
print("\n=== RESULTADOS FINALES ===")

print("Calificaciones actualizadas:", calificaciones)
print("Promedio general:", round(promedio, 2))
print("Calificacion mas alta:", max(calificaciones))
print("Calificacion mas baja:", min(calificaciones))
print("Estudiantes aprobados:", aprobados)
print("Estudiantes reprobados:", reprobados)

print("\nPrograma finalizado.")
