"""
Sistema de calificaciones - Capítulo IX: Arreglos y Vectores
Asignatura: Introducción a la Programación
Usa un vector (lista de Python) para almacenar calificaciones y aplica
índices, ciclos, condiciones, cálculos y búsquedas sobre sus elementos.
"""
NOTA_MINIMA = 70 # calificación mínima para aprobar
def mostrar_calificaciones(calificaciones):
"""Recorre el vector con un ciclo for y muestra cada elemento."""
print("\n--- Calificaciones registradas ---")
for i in range(len(calificaciones)):
print(f"Estudiante {i + 1} (índice {i}): {calificaciones[i]}")
def calcular_promedio(calificaciones):
"""Suma todos los elementos con un ciclo y divide entre la cantidad."""
suma = 0
for nota in calificaciones:
suma += nota
return suma / len(calificaciones)
def buscar_mayor(calificaciones):
"""Búsqueda del valor máximo y de su posición."""
posicion = 0
for i in range(1, len(calificaciones)):
if calificaciones[i] > calificaciones[posicion]:
posicion = i
return calificaciones[posicion], posicion
Capítulo IX: Arreglos y Vectores | Página 6
def buscar_menor(calificaciones):
"""Búsqueda del valor mínimo y de su posición."""
posicion = 0
for i in range(1, len(calificaciones)):
if calificaciones[i] < calificaciones[posicion]:
posicion = i
return calificaciones[posicion], posicion
def contar_aprobados_reprobados(calificaciones):
"""Usa una condición if sobre cada elemento para clasificarlo."""
aprobados = 0
reprobados = 0
for nota in calificaciones:
if nota >= NOTA_MINIMA:
aprobados += 1
else:
reprobados += 1
return aprobados, reprobados
def pedir_entero(mensaje, minimo, maximo):
"""Pide un número entero y repite con while hasta que sea válido."""
while True:
texto = input(mensaje)
if texto.lstrip("-").isdigit():
valor = int(texto)
if minimo <= valor <= maximo:
return valor
print(f" Entrada no válida. Escriba un entero entre {minimo} y {maximo}.")
def main():
calificaciones = [85, 67, 92, 74, 58]
total = len(calificaciones)
print("=== SISTEMA DE CALIFICACIONES ===")
# 1. Mostrar todas las calificaciones
mostrar_calificaciones(calificaciones)
# 2. Mostrar una calificación mediante su índice
pos = pedir_entero(f"\nIngrese el número de estudiante a consultar (1-{total}): ", 1, total)
print(f"La calificación del estudiante {pos} es: {calificaciones[pos - 1]}")
# 3. Promedio
print(f"\nPromedio del grupo: {calcular_promedio(calificaciones):.2f}")
# 4 y 5. Mayor y menor
mayor, pos_mayor = buscar_mayor(calificaciones)
menor, pos_menor = buscar_menor(calificaciones)
print(f"Calificación más alta: {mayor} (estudiante {pos_mayor + 1})")
print(f"Calificación más baja: {menor} (estudiante {pos_menor + 1})")
# 6 y 7. Aprobados y reprobados
aprobados, reprobados = contar_aprobados_reprobados(calificaciones)
print(f"Aprobados (>= {NOTA_MINIMA}): {aprobados}")
print(f"Reprobados (< {NOTA_MINIMA}): {reprobados}")
# 8. Modificar una calificación
Capítulo IX: Arreglos y Vectores | Página 7
pos = pedir_entero(f"\nNúmero de estudiante a modificar (1-{total}): ", 1, total)
nueva = pedir_entero("Nueva calificación (0-100): ", 0, 100)
anterior = calificaciones[pos - 1]
calificaciones[pos - 1] = nueva
print(f"Estudiante {pos}: {anterior} -> {nueva}")
# 9. Mostrar el vector actualizado y recalcular
mostrar_calificaciones(calificaciones)
print(f"\nVector actualizado: {calificaciones}")
print(f"Nuevo promedio: {calcular_promedio(calificaciones):.2f}")
aprobados, reprobados = contar_aprobados_reprobados(calificaciones)
print(f"Aprobados: {aprobados} | Reprobados: {reprobados}")
if __name__ == "__main__":
main()
