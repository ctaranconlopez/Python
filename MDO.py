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

print("\n---\n")
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

# Sentencia If
a = 5
b = 10
c = 12
d = 15
if a == 5:
    print("a vale",a)
    if b == 9 and c == 12:
        print("y b vale",b)
    elif d == 14:
        print("d vale",d)
    else:
        print("...")

print("\n---\n")

nota = float(input("Introduce una nota: ")) # Se realiza un cast a float debido a que por input siempre es string
if nota >= 9:
    print("Sobresaliente")
if nota >= 7 and nota < 9:
    print("Notable")
if nota >= 6 and nota < 7:
    print("Bien")
if nota >= 5 and nota < 6:
    print("Suficiente")
if nota < 5:
    print("Insuficiente")
    
if True: # Sirve para finalizar un bloque, se puede utilizar en un bloque vacío.
    pass

print("\n---\n")     
# Sentencia While

c = 0
while c <= 5:
    c+=1
    print("c vale",c)

print("\n---\n")

c = 0
while c <= 5:                   # - Sentencia Else en bucle While:
    c+=1                        # Se encadena al While para ejecutar un bloque de código una vez la condición
    print("c vale",c)           # ya no devuelve True (normalmente al final).
else:
    print("Se ha completado toda la iteración y c vale",c)
    
print("\n---\n")
    
c = 0
d = 5
while c <= 5:                       # - Sentencia Else en bucle While:
    c+=1                            # Se encadena al While para ejecutar un bloque de código una vez la condición
    if (c==4):                      # ya no devuelve True (normalmente al final).
        print("Rompemos el bucle cuando c vale",c) # - Instrucción Break:
        break                       # Sirve para "romper" la ejecución del While en cualquier momento. 
    elif d == 5:                    # No se ejecutará el Else, ya que éste sólo se llama al finalizar la iteración.
        continue                    # - Instrucción Continue:
    print("c vale",c)               # Sirve para "saltarse" la iteración actual sin romper el bucle.
else:
    print("Se ha completado toda la iteración y c vale",c)

print("\n---\n")

# Recorrer elementos de una lista con While
print("Recorremos elementos de una lista con while: ")
numeros = [1,2,3]
indice = 0
while indice < len(numeros):
    print (numeros[indice])
    indice += 1
    
# Recorrer elementos de una lista con for
print("Recorremos elementos de una lista con for: ")
for numero in numeros:  # Para [variable] en [lista]
    print(numero)
    
# Podemos utilizar la función enumerate() para conseguir el índice y el valor en cada iteración fácilmente

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for indice,numero in enumerate(numeros):
    numeros[indice] *= 10
    
# Las cadenas son inmutables, no pueden cambiar los elementos

cadena = "Hola"
for caracter in cadena:
    print(caracter)

# COLECCIONES DE DATOS

# ---- TUPLAS
# Son unas colecciones parecidas a las listas, con la peculiaridad de que son inmutables (no varían ni de tamaño ni de valor 
# de los elementos)

# LAS TUPLAS SE REPRESENTAN ENTRE PARENTESIS (LISTAS ENTRE CORCHETES [])

tupla = (100,"Hola",[1,2,3],-50)
print(tupla)

# INDEX() Sirve para buscar un elemento y saber su posición en la tupla. Da error si no se encuentra.

tupla.index(-50) # Devuelve un 3

# COUNT() Sirve para contar cuantas veces aparece un elemento en una tupla.

tupla.count(100) # Devuelve 1

# ---- CONJUNTOS
# Son colecciones desordenadas (Se dice que son desordenados porque gestionan automáticamente la posición de sus elementos,
# en lugar de conservarlos en la posición que nosotros los añadimos) de elementos únicos utilizados para hacer pruebas
# de pertenencia a grupos y eliminación de elementos duplicados.

# LOS CONJUNTOS SE REPRESENTAN ENTRE LLAVES {}
conjunto = {1,2,3}
conjunto.add(4) # Para añadir valores al conjunto

print(2 in conjunto)  # True

# PARA ELIMINAR ELEMENTOS DUPLICADOS DE UNA LISTA PODEMOS REALIZAR UN CAST A CONJUNTO Y VOLVER A LISTA

l = [1,2,3,3,2,1]
c = set(l)
l = list(c)

l = list( set( l ) ) # En una linea

# l = [1,2,3]

# ---- DICCIONARIOS

# Son junto a las listas las colecciones más utilizadas. Se basan en una estructura mapeada donde cada elemento de la colección
# se encuentra identificado con una clave única. Por tanto, no puede haber dos claves iguales.
# En otros lenguajes se conocen como arreglos asociativos.

# SE REPRESENTAN ENTRE LLAVES

colores = {'amarillo':'yellow','azul':'blue'}
print(colores['azul'])

numeros = {10:'diez',20:'veinte'}
print(numeros[10])

colores['amarillo'] = 'white' # MODIFICACION DE VALOR

del(colores['amarillo']) # BORRAR ELEMENTOS DEL DICCIONARIO

edades = {'Hector':27,'Juan':45,'Maria':34}
for clave in edades:
    print(clave,edades[clave])

# METODO .ITEMS() Nos facilita la lectura en clave y valor de los elementos porque devuelve ambos valores en cada
# iteración automáticamente:

for c,v in edades.items():
    print(c,v)
    
# ---- PILAS

# Son colecciones de elementos ordenados que únicamente permiten dos acciones:
#   - Añadir un elemento a la pila
#   - Sacar un elemento de la pila
# La peculiaridad es que el último elemento en entrar es el primero en salir.
# En inglés se conocen como estructuras LIFO (Last In First Out).

# Las podemos crear como listas normales y añadir elementos al final con el append()
# Para sacar los elementos utilizaremos el método .pop()

# ---- COLAS

# Son colecciones de elementos ordenados que únicamente permiten dos acciones:
#   - Añadir un elemento a la cola
#   - Sacar un elemento de la cola
# La peculiaridad es que el primer elemento en entrar es el primero en salir.
# En inglés se conocen como estructuras FIFO (First In First Out).

# Debemos importar la colección deque manualmente para crear una cola:
    
from collections import deque
cola = deque(['Hector','Juan','Miguel'])

# Podemos añadir elementos al final con el append()
# popleft() en lugar de pop() a la hora de sacar los elementos (de la parte izquierda de la cola)

# ---- SALIDA POR PANTALLA

# Método .FORMAT()
# Nos permite formatear información en una cadena cómodamente utilizando identificadores referenciados:
v = "otro texto"
n = 10
c = "Un texto '{}' y un número '{}'".format(v,n)
print(c)

# ---- FUNCIONES

def dibujar_tabla_del_5():
    for i in range(10):
        print("5 * {} = {}".format(i,i*5))
dibujar_tabla_del_5()

# Una variable declarada en una función no existe en la función principal:
# Sin embargo, una variable declarada fuera de la función (al mismo nivel), sí que es accesible desde la función.
# Siempre que declaremos la variable antes de la ejecución, podemos acceder a ella desde dentro.
# Por tanto no podemos modificar una variable externa dentro de una función.
# Para poder modificar una variable externa en la función, debemos indicar que es global de la siguiente forma:
def test():
    global o # variable que hace referencia a la o externa
    o = 5
    print(o)
test()

o=10
test()
print(o)

# Retorno múltiple
def test():
    return "Una cadena",20,[1,2,3]

test()

# Envío de valores
def suma(a,b): # valores que se reciben (parámetros)
    return a+b

r = suma(2,5)  # valores que se envían (argumentos)

# Parámetros por defecto

def resta(a=None,b=None):
    if a == None or b == None:
        print("Error, debes enviar dos números a la función")
        return
    return a-b
resta(1,5)

# Argumentos y parámetros indeterminados

# Por posición
def indeterminados_posicion(*args):
    for arg in args:
        print(arg)
    
indeterminados_posicion(5,"Hola",[1,2,3,4,5])

# Por nombre
def indeterminados_nombre(**kwargs):
    for kwarg in kwargs:
        print(kwarg," ", kwargs[kwarg])
indeterminados_nombre(n=5,c="Hola",l=[1,2,3,4,5])   

# Funciones recursivas
def factorial(num):
    print("Valor inicial ->",num)
    if num > 1:
        num = num * factorial(num -1)
    print("valor final ->",num)
    return num

factorial(5)

# EXCEPCIONES
while(True):
    try:
        n = float(input("Introduce un número: "))
        m = 4
        print("{}/{}={}".format(n,m,n/m))
    except:
        print("Ha ocurrido un error, introduce bien el número")
    else:
        print("Todo ha funcionado correctamente")
        break  # Importante romper la iteración si todo ha salido bien
    finally:
        print("Fin de la iteración") # Siempre se ejecuta


