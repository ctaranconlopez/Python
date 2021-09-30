# Manejo de datos y optimización

# Slicing

    # El slicing es una capacidad de las cadenas que devuelve un subconjunto o subcadena 
    # utilizando dos índices [inicio:fin]:
        # El primer índice indica donde empieza la subcadena (se incluye el carácter).
        # El segundo índice indica donde acaba la subcadena (se excluye el carácter).

palabra = "Python"
print("Desde la 2º posicion hasta la última no incluida: " + palabra[2:-1])

# Listas - Se representan entre [] y es una ordenada (los objetos mantienen el orden en el que los introducimos)

numeros = [1,2,3,4]
datos = [4,"Una cadena",-15,3.14,"Otra cadena"]

numeros + [5,6,7,8] # Suma de listas
numeros.append(3) # Añadir valor al final de la lista

a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
r = [a,b,c]
print("Listas anidadas \n" + str(r))

# Para leer un valor por teclado usamos <<input()>>

# False y True se escriben la primera con mayusculas

# Operadores lógicos: not - and - or
not True
True and True
True or False

# Expresiones anidadas
a = 10
b = 5
a * b - 2**b >= 20 and not (a % b) != 0


# Colecciones de datos

