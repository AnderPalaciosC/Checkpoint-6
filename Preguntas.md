# Preguntas

## ¿Para qué usamos Clases en Python?

Las clases en Python son una forma de organizar y estructurar código.  

Nos permiten definir un conjunto de atributos y métodos que representan un concepto o entidad. 

Las clases son fundamentales en la programación y nos permiten reutilizar código y reducir la complejidad.

### Ejemplo:

```python
class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print(f'Hola, {self.nombre} {self.apellido}')

# Crear Usuario
Usuario1 = Usuario('Ander', 'Palacios')
Usuario1.saludo()
```

## ¿Qué método se ejecuta automáticamente cuando se crea una instancia de una clase?

Cuando se crea una instancia de una clase en Python, el método `__init__` se ejecuta automáticamente. 

Este método se utiliza para inicializar los atributos de la instancia recién creada.

### Sintaxis del Método `__init__`:

```python
class clase:
    def __init__(self, parametro1, parametro2):
        self.parametro1 = parametro1
        self.parametro2 = parametro2
```

## ¿Cuáles son los tres verbos de API?

Los tres verbos principales de API son:

1. **GET**: Se utiliza para recuperar datos de un recurso específico.
2. **POST**: Se utiliza para enviar datos y crear un nuevo recurso.
3. **PUT**: Se utiliza para actualizar un recurso existente.

## ¿Es MongoDB una base de datos SQL o NoSQL?

MongoDB es una base de datos NoSQL. 

Se basa en documentos y utiliza un formato similar a JSON para almacenar datos.

### Características de MongoDB:

- **Estructura de Datos**: MongoDB almacena datos en documentos JSON-like (BSON) en lugar de en filas y columnas como las bases de datos SQL tradicionales.
- **Escalabilidad**: MongoDB es altamente escalable, lo que permite manejar grandes volúmenes de datos y cargas de trabajo distribuidas.
- **Flexibilidad**: No se requiere un esquema rígido en MongoDB, lo que significa que los documentos en una colección pueden tener diferentes estructuras y tipos de datos.

### Ejemplo de Uso de MongoDB:

```python
# Crear una colección
coleccion = db["mi_coleccion"]

# Insertar un documento
documento = {"nombre": "Ander", "edad": 23}
coleccion.insert_one(documento)
```

## ¿Qué es una API?

Una API es un conjunto de reglas y protocolos que permite que diferentes aplicaciones se comuniquen entre sí. 

Proporciona una forma estandarizada para que las aplicaciones accedan a funciones o datos de otras aplicaciones o servicios.

### Características de las APIs:

- **Interoperabilidad**: Las APIs permiten la comunicación entre diferentes sistemas, independientemente de las tecnologías subyacentes.
- **Reutilización de Código**: Las APIs permiten que el código y las funcionalidades se compartan y se reutilicen en diferentes contextos.
- **Abstracción**: Las APIs ocultan la complejidad interna de un sistema y proporcionan una interfaz simple y consistente para interactuar con él.

## ¿Qué es Postman?

Postman es una herramienta de colaboración para el desarrollo de API. 

Permite a los desarrolladores probar, documentar y compartir APIs de una manera fácil y eficiente.

### Características de Postman:

- **Interfaz Gráfica**: Postman proporciona una interfaz gráfica intuitiva que facilita la creación y el envío de solicitudes HTTP a APIs.
- **Pruebas Automatizadas**: Permite escribir y ejecutar pruebas automatizadas para verificar el comportamiento de una API.
- **Documentación**: Postman permite generar documentación interactiva para APIs, facilitando su comprensión y uso por parte de otros desarrolladores.
- **Colecciones**: Permite organizar solicitudes relacionadas en colecciones, lo que facilita la gestión y la colaboración en proyectos de desarrollo.

### Uso de Postman:

Postman se utiliza comúnmente en el desarrollo de software para interactuar con APIs durante el proceso de diseño, pruebas y depuración. 

Los desarrolladores pueden crear solicitudes HTTP personalizadas, probar diferentes escenarios de uso y colaborar con otros miembros del equipo para asegurarse de que la API funcione correctamente y cumpla con los requisitos del proyecto.

## ¿Qué es el polimorfismo?

El polimorfismo es un concepto de la programación orientada a objetos que permite que un objeto pueda comportarse de diferentes maneras según el contexto en el que se utiliza. 

Esto se logra mediante el uso de métodos con el mismo nombre pero diferentes implementaciones en clases diferentes.

### Características del Polimorfismo:

- **Mismo Nombre, Distintos Comportamientos**: En el polimorfismo, múltiples clases pueden definir métodos con el mismo nombre pero con comportamientos diferentes.
- **Flexibilidad**: Permite a las clases derivadas proporcionar implementaciones específicas de un método heredado de una clase base.
- **Abstracción**: Permite tratar objetos de diferentes clases de manera uniforme a través de una interfaz común.

## ¿Qué es un método dunder?

Los métodos dunder (double underscore) son métodos especiales en Python que tienen nombres que comienzan y terminan con doble guion bajo. 

Estos métodos son implementados por el lenguaje y tienen un significado especial en ciertos contextos.

### Características y ejemplos de los Métodos Dunder:

- **Nombre Especial**: Los métodos dunder tienen nombres que siguen el patrón `__nombre__`.
- **Comportamiento Especial**: Los métodos dunder son utilizados por Python para realizar ciertas operaciones especiales, como la inicialización de objetos (`__init__`), la representación de objetos (`__repr__`) y la sobrecarga de operadores (`__add__`, `__sub__`, etc.).
- **Implementación Implícita**: Los métodos dunder son llamados implícitamente por Python en ciertos contextos, como al crear, comparar o interactuar con objetos.

## ¿Qué es un decorador de Python?

Un decorador en Python es una función que toma otra función como argumento y devuelve una función modificada o extendida. 

Se utilizan para agregar funcionalidad a una función existente sin modificar su código.

### Características de los Decoradores:

- **Funciones de Orden Superior**: Los decoradores son funciones de orden superior, lo que significa que pueden aceptar otras funciones como argumentos y devolver funciones como resultado.
- **Sintaxis de Azúcar Sintáctica**: Python proporciona una sintaxis especial (`@decorador`) para aplicar un decorador a una función de forma más legible y concisa.
- **Reutilización de Código**: Los decoradores permiten encapsular y reutilizar la lógica común para agregar funcionalidad a múltiples funciones.

### Ejemplo de Uso de Decoradores:

```python
# Definir decorador
def decorador(funcion):
    def envoltura():
        print("Antes de la función")
        funcion()
        print("Después de la función")
    return envoltura

# Aplicar el decorador a una función
@decorador
def saludar():
    print("Hola")

# Llamar a la función decorada
saludar()