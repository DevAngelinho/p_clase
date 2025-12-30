from functools import reduce

print("Ingresa nombres y notas :")

datos = list(map(lambda x: (x.split(',')[0], float(x.split(',')[1])), 
        filter(lambda x: ',' in x, iter(input, 'fin'))))

estados = map(lambda x: 'APROBADO' if x[1] >= 70 else 'REPROBADO', datos)

print("\n--- Resultados ---")

datos_completos = zip(datos, estados)

print(*map(lambda x: f"{x[0][0]} tiene {int(x[0][1])} -> {x[1]}", datos_completos), sep="\n")

if datos:
    promedio = reduce(lambda a, b: a+b, map(lambda x: x[1], datos)) / len(datos)
    print(f"\nPromedio del curso: {promedio:.2f}")