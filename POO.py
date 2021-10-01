# Programación orientada a objetos

class Cliente:
    
    def __init__(self, dni, nombre, apellidos):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        
    def __str__(self):
        return '{} {}'.format(self.nombre,self.apellidos)
    

class Empresa:
    
    def __init__(self, clientes=[]):
        self.clientes = clientes
        
    def mostrar_cliente(self, dni=None):
        for c in self.clientes:
            if c.dni == dni:
                print(c)
                return
        print("Cliente no encontrado")
    
    def borrar_cliente(self, dni=None):
        for i,c in enumerate(self.clientes):
            if c.dni == dni:
                del(self.clientes[i])
                print(str(c),"> BORRADO")
                return
        print("Cliente no encontrado")

# Funcion TYPE()
type(objeto) # Sirve para determinar la clase de un objeto

# Método INIT() Se llama automáticamente al crear una instancia de clase.
class Galleta():
    chocolate = False
    def __init__(self):
        print("Se acaba de crear una galleta.")
g = Galleta()

# Self sirve para hacer referencia a los métodos y atributos base de una clase dentro de sus propios métodos.

class Galleta():
    chocolate = False
    
    def __init__(self):
        print("Se acaba de crear una galleta.")
    
    def chocolatear(self):
        self.chocolate = True
        
    def tiene_chocolate(self):
        if (self.chocolate):
            print("Soy una galleta chocolateada :-D")
        else:
            print("Soy una galleta sin chocolate :-(")
    
g = Galleta()
g.tiene_chocolate()
g.chocolatear()
g.tiene_chocolate()

# CONSTRUCTOR Y DESTRUCTOR
class Pelicula:
    # Constructor de clase (al crear la instancia)
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la película",self.titulo)
        
    # Destructor de clase (al borrar la instancia)
    def __del__(self):
        print("Se está borrando la película", self.titulo)
        
p = Pelicula("El Padrino",175,1972)

# Redefinir métodos [len()]
class Pelicula:
    # Constructor de clase
    def __init__(self,titulo,duracion,lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print("Se ha creado la película",self.titulo)
        
    # Destructor de clase
    def __del__(self):
        print("Se está borrando la película", self.titulo)
        
    # Redefinimos el método string
    def __str__(self):
        return "{} lanzada en {} con una duración de {} minutos".format(self.titulo,self.lanzamiento,self.duracion)
    
    # Redefinimos el método length
    def __len__(self):
        return self.duracion
        
p = Pelicula("El Padrino",175,1972)
len(p)

# ENCAPSULACION
# Para hacer un atributo o metodo privado se indica con dos barras bajas al inicio
class Ejemplo:
    __atributo_privado = "Soy un atributo inalcanzable desde fuera"
    
    def __metodo_privado(self):
        print("Soy un método inalcanzable desde fuera")

# HERENCIA

# Superclase PRODUCTO
class Producto:
    def __init__(self,referencia,nombre,pvp,descripcion):
        self.referencia = referencia
        self.nombre = nombre
        self.pvp = pvp
        self.descripcion = descripcion
        
    def __str__(self):
        return """\
REFERENCIA\t{}
NOMBRE\t\t{}
PVP\t\t{}
DESCRIPCIÓN\t{}""".format(self.referencia,self.nombre,self.pvp,self.descripcion)

# Subclase ADORNO
class Adorno(Producto):
    pass

a = Adorno(2034,"Vaso adornado",15,"Vaso de porcelana adornado con árboles")
print(a)

































