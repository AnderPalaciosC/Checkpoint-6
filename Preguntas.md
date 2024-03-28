# Preguntas

## ¿Clases en Python?

En Python, las clases son una característica fundamental de la programación orientada a objetos que nos permite modelar y organizar nuestro código de manera más efectiva, definiendo un conjunto de atributos y métodos que representan un concepto o entidad.

Las clases son fundamentales en la programación y nos permiten reutilizar código y reducir la complejidad.

Nos permiten definir un conjunto de atributos (variables) y métodos (funciones) que representan un tipo de objeto específico.

### Razones para usar Clases en Python:

1. **Abstracción**: Las clases nos permiten representar entidades del mundo real o conceptos abstractos en nuestro código de manera más fiel. Por ejemplo, podemos crear una clase Coche para representar características comunes de los coches, como modelo, color y velocidad.

2. **Encapsulación**: Las clases nos permiten agrupar datos y funciones relacionadas en un solo lugar, lo que facilita su gestión y evita posibles conflictos de nombres. Esto nos ayuda a mantener nuestro código organizado y modular.

3. **Reutilización de Código**: Una vez definida una clase, podemos crear múltiples instancias de esa clase (objetos) en diferentes partes de nuestro programa. Esto nos permite reutilizar la funcionalidad de la clase en diferentes contextos sin tener que volver a escribir el código.

4. **Herencia**: Python soporta la herencia, lo que significa que una clase puede heredar atributos y métodos de otra clase. Esto nos permite construir jerarquías de clases donde las clases más específicas (subclases) heredan comportamientos de clases más generales (superclases).

### Resumen:

Utilizamos clases en Python para modelar y organizar nuestro código de una manera más orientada a objetos, lo que nos permite abstraer conceptos, encapsular funcionalidades, reutilizar código y aprovechar la herencia para construir sistemas más complejos y flexibles.

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

## Método que se ejecuta automáticamente cuando se crea una instancia de una clase

En Python, el método que se ejecuta automáticamente cuando se crea una instancia de una clase es el método `__init__()`, también conocido como constructor de la clase. 

Este método se llama automáticamente cuando creamos un nuevo objeto de esa clase utilizando la sintaxis de inicialización.

### Función del Método `__init__()`:

El método `__init__()` se utiliza para inicializar los atributos de una instancia con valores predeterminados o proporcionados por el usuario. Es aquí donde se definen las propiedades básicas de un objeto justo después de su creación.

### Resumen:

En resumen, el método `__init__()` es fundamental en Python ya que se ejecuta automáticamente al crear una instancia de una clase, permitiendo la inicialización de los atributos de la instancia con valores específicos. Esto es útil para preparar el objeto para su uso inmediato después de su creación.

### Sintaxis del Método `__init__`:

```python
class clase:
    def __init__(self, parametro1, parametro2):
        self.parametro1 = parametro1
        self.parametro2 = parametro2
```

## Los tres verbos de API

Los tres verbos principales de API son:

1. **GET**: Este verbo se utiliza para recuperar datos de un recurso específico. En una solicitud GET, el cliente solicita al servidor que envíe de vuelta una representación del recurso solicitado.
   - Se utiliza para recuperar información, como obtener datos de un usuario específico o una lista de productos.
  
2. **POST**: El verbo POST se utiliza para enviar datos al servidor para crear un nuevo recurso. En una solicitud POST, el cliente envía datos al servidor, que luego procesa estos datos y crea un nuevo recurso.
   - Se utiliza para enviar datos nuevos al servidor, como crear una nueva publicación en un blog o agregar un nuevo usuario a una base de datos.
   
3. **PUT**: Este verbo se utiliza para actualizar un recurso existente en el servidor. En una solicitud PUT, el cliente envía datos al servidor para reemplazar completamente o actualizar parcialmente el recurso existente.
   - Se utiliza para actualizar información existente en el servidor, como modificar los detalles de un perfil de usuario o actualizar el estado de un pedido.

#### Resumen

Estos tres verbos son esenciales y proporcionan las operaciones básicas para interactuar con recursos en un sistema a través de la API. Mediante la combinación de estos verbos y la manipulación de los datos enviados y recibidos, los clientes pueden realizar una amplia gama de operaciones en un sistema remoto.

## MongoDB, ¿una base de datos SQL o NoSQL?

MongoDB es una base de datos NoSQL. 

A diferencia de las bases de datos SQL tradicionales, que almacenan datos en tablas y utilizan un lenguaje de consulta estructurado (SQL) para manipular esos datos, MongoDB utiliza un enfoque de almacenamiento basado en documentos.

### Características de MongoDB:

- **Modelo de Datos**: MongoDB almacena datos en documentos JSON-like (BSON), que son estructuras de datos flexibles y jerárquicas. Estos documentos pueden contener campos y valores de diferentes tipos, lo que permite una representación más natural de los datos.

- **Esquema Dinámico**: A diferencia de las bases de datos SQL, MongoDB no requiere un esquema predefinido o una estructura rígida para los datos. Esto significa que los documentos en una colección pueden tener diferentes estructuras y campos, lo que facilita la adaptación a cambios en los requisitos de los datos.

- **Escalabilidad Horizontal**: MongoDB es altamente escalable y puede manejar grandes volúmenes de datos y cargas de trabajo distribuidas. Esto se logra mediante la replicación automática y el particionamiento de datos en clústeres distribuidos.

- **Operaciones Avanzadas**: MongoDB proporciona una amplia gama de operaciones avanzadas, como consultas complejas, agregaciones, indexación flexible y capacidades de búsqueda geoespacial.

### Resumen:

MongoDB es una base de datos NoSQL que ofrece flexibilidad, escalabilidad y un modelo de datos intuitivo basado en documentos. 

Se utiliza en una amplia variedad de aplicaciones y casos de uso, desde aplicaciones web hasta análisis de big data y procesamiento de eventos en tiempo real.

### Ejemplo de Uso de MongoDB:

```python
# Crear una colección
coleccion = db["mi_coleccion"]

# Insertar un documento
documento = {"nombre": "Ander", "edad": 23}
coleccion.insert_one(documento)
```

## ¿Qué es una API?

Una API, o Interfaz de Programación de Aplicaciones, es un conjunto de reglas, protocolos y herramientas que permiten que diferentes aplicaciones informáticas se comuniquen entre sí y compartan datos o funcionalidades de manera estandarizada y controlada. En esencia, una API actúa como un intermediario que facilita la interacción entre diferentes sistemas de software. 

### Características de las APIs:

1. **Estandarización de la Comunicación**: Las APIs definen un conjunto de reglas y protocolos que estandarizan la forma en que las aplicaciones se comunican entre sí. Esto asegura que la comunicación sea coherente, predecible y fácil de entender para todas las partes involucradas.

2. **Abstracción de la Complejidad**: Una API oculta la complejidad interna de un sistema subyacente y proporciona una interfaz simple y coherente para interactuar con él. Esto permite a los desarrolladores utilizar las funcionalidades de un sistema sin necesidad de comprender todos los detalles técnicos de su implementación.

3. **Reutilización de Funcionalidades**: Al exponer ciertas funcionalidades o datos a través de una API, un sistema puede ser utilizado y aprovechado por otras aplicaciones de manera eficiente. Esto promueve la reutilización de código y funcionalidades, evitando la duplicación de esfuerzos y fomentando la colaboración entre desarrolladores y equipos.

4. **Seguridad y Control**: Las APIs permiten un control preciso sobre quién puede acceder a qué datos o funcionalidades, así como las acciones que pueden realizar. Esto se logra a través de mecanismos de autenticación, autorización y control de acceso integrados en la API.

### Ejemplos de Uso de las APIs:

- **APIs Web**: Muchas empresas y servicios en línea ofrecen APIs web que permiten a los desarrolladores acceder a sus datos o funcionalidades. Por ejemplo, la API de Twitter permite a los desarrolladores acceder a los tweets y perfiles de los usuarios de Twitter, mientras que la API de Google Maps proporciona acceso a funcionalidades de mapas y ubicaciones.

- **APIs de Plataforma**: Las plataformas de desarrollo, como Android o iOS, proporcionan APIs que permiten a los desarrolladores crear aplicaciones para sus sistemas operativos. Estas APIs ofrecen acceso a funcionalidades específicas del dispositivo, como la cámara, el GPS o los sensores.

- **APIs de Bibliotecas y Frameworks**: Muchos frameworks y bibliotecas de software ofrecen APIs que permiten a los desarrolladores extender y personalizar su funcionalidad. Por ejemplo, Django y Flask son frameworks de desarrollo web en Python que proporcionan APIs para crear aplicaciones web de manera eficiente.

### Resumen: 

Una API es una herramienta fundamental en el desarrollo de software moderno que facilita la comunicación y la integración entre diferentes sistemas y aplicaciones. Permite la creación de sistemas más complejos y potentes al permitir la colaboración y la reutilización de funcionalidades entre desarrolladores y equipos.

## Postman:

### ¿Qué es Postman?

Postman es una herramienta de colaboración para el desarrollo de APIs que facilita la creación, prueba y documentación de APIs.

Originalmente concebido como una extensión de Chrome, Postman ha evolucionado para convertirse en una plataforma independiente que ofrece una amplia gama de características y funcionalidades para ayudar a los desarrolladores a trabajar con APIs de manera más eficiente.

<img src="postman-logo-vert-2018.jpg" alt="Postman" width="350" height="200">

### Características de Postman:

1. **Entorno de Desarrollo Integrado (IDE) para APIs**: Postman proporciona un entorno completo para el desarrollo de APIs, que incluye herramientas para crear, editar, probar y depurar APIs de manera rápida y eficiente.

2. **Creación de Solicitudes HTTP**: Permite crear solicitudes HTTP personalizadas, como GET, POST, PUT y DELETE, con parámetros, encabezados y cuerpos de solicitud configurables.

3. **Colecciones de Solicitudes**: Postman permite organizar solicitudes relacionadas en colecciones, lo que facilita su gestión y compartición entre miembros del equipo.

4. **Pruebas Automatizadas**: Postman incluye un potente motor de pruebas que permite escribir y ejecutar scripts de prueba automatizados para validar el comportamiento de las APIs.

5. **Documentación de APIs**: Permite generar documentación automática para APIs a partir de colecciones de solicitudes, facilitando la comprensión y el consumo de las APIs por parte de otros desarrolladores.

6. **Monitoreo y Análisis de APIs**: Postman proporciona herramientas para monitorear el rendimiento y la disponibilidad de las APIs, así como para analizar el tráfico y las tendencias de uso.

### Uso de Postman:

Postman se utiliza comúnmente en el desarrollo de software para interactuar con APIs durante el proceso de diseño, pruebas y depuración. 

Los desarrolladores pueden crear solicitudes HTTP personalizadas, probar diferentes escenarios de uso y colaborar con otros miembros del equipo para asegurarse de que la API funcione correctamente y cumpla con los requisitos del proyecto.

## ¿Qué es el polimorfismo?

El polimorfismo es un concepto fundamental en la programación orientada a objetos que se refiere a la capacidad de diferentes objetos de una jerarquía de clases para responder al mismo mensaje de manera diferente. 

En otras palabras, el polimorfismo permite que un mismo método o función pueda comportarse de manera distinta según el tipo de objeto que lo invoque.

### Características del Polimorfismo:

- **Mismo Nombre, Distintos Comportamientos**: En el polimorfismo, múltiples clases pueden definir métodos con el mismo nombre pero con comportamientos diferentes.
  
- **Flexibilidad**: Permite a las clases derivadas proporcionar implementaciones específicas de un método heredado de una clase base.
  
- **Abstracción**: Permite tratar objetos de diferentes clases de manera uniforme a través de una interfaz común.

### Tipos de Polimorfismo:

1. **Polimorfismo de Subtipos (Herencia)**: En este tipo de polimorfismo, las clases derivadas (subtipos) pueden proporcionar implementaciones específicas de los métodos heredados de sus clases base. Esto permite que objetos de diferentes clases respondan al mismo mensaje de manera diferente.

2. **Polimorfismo Paramétrico (Sobrecarga)**: En este tipo de polimorfismo, una misma función puede tener múltiples definiciones o implementaciones, cada una con una lista diferente de parámetros. El compilador o intérprete selecciona la implementación adecuada en función del número y tipo de argumentos proporcionados al llamar a la función.

3. **Polimorfismo de Inclusión (Interfaces)**: En este tipo de polimorfismo, las interfaces proporcionan una forma de definir un comportamiento común para diferentes clases sin especificar cómo se implementa ese comportamiento. Las clases que implementan una interfaz pueden proporcionar su propia implementación del comportamiento definido por la interfaz.

### Resumen:

El polimorfismo es un concepto poderoso que permite escribir código más flexible y modular, ya que permite interactuar con objetos de manera genérica, sin necesidad de conocer su tipo específico. Esto facilita la reutilización del código y la creación de sistemas más robustos y escalables.

## ¿Qué es un método dunder?

Un método dunder, también conocido como método especial o método mágico, es un tipo de método en Python que utiliza un formato específico de doble subrayado (`__`). 

Estos métodos están predefinidos en la definición de una clase y tienen un propósito especial en el comportamiento de los objetos de esa clase.

### Características y ejemplos de los Métodos Dunder:

- **Nombre Especial**: Los métodos dunder tienen nombres que siguen el patrón `__nombre__`.
  
- **Comportamiento Especial**: Los métodos dunder son utilizados por Python para realizar ciertas operaciones especiales, como la inicialización de objetos (`__init__`), la representación de objetos (`__repr__`) y la sobrecarga de operadores (`__add__`, `__sub__`, etc.).
  
- **Implementación Implícita**: Los métodos dunder son llamados implícitamente por Python en ciertos contextos, como al crear, comparar o interactuar con objetos.

### Ejemplos de Métodos Dunder Comunes:

1. `__init__`: Este es el método de inicialización de una clase en Python. Se llama automáticamente cuando se crea una nueva instancia de la clase y se utiliza para inicializar los atributos de esa instancia.

2. `__str__` y `__repr__`: Estos métodos se utilizan para definir la representación de cadena de un objeto cuando se imprime en la consola o se convierte a una cadena de texto.

3. `__len__`: Este método se utiliza para definir la longitud de un objeto, como una lista o una cadena, y se llama automáticamente cuando se utiliza la función `len()`.

4. `__add__`, `__sub__`, `__mul__`, etc.: Estos métodos se utilizan para definir la operación de adición, sustracción, multiplicación, etc., entre objetos y se llaman automáticamente cuando se utilizan los operadores correspondientes (`+`, `-`, `*`, etc.).

## ¿Qué es un decorador de Python?

En Python, un decorador es una función que modifica el comportamiento de otra función o método. 

Los decoradores son una característica poderosa y flexible que permite agregar funcionalidades adicionales a las funciones sin modificar su código interno.

### Características de los Decoradores:

1. **Sintaxis Especial**: Los decoradores utilizan una sintaxis especial utilizando el símbolo `@` seguido del nombre del decorador encima de la definición de la función que se va a decorar.

2. **Funciones de Orden Superior**: Los decoradores son funciones de orden superior, lo que significa que pueden aceptar funciones como argumentos y devolver funciones como resultado.

3. **Transparencia**: Los decoradores pueden añadir funcionalidades adicionales a una función sin modificar su comportamiento original, lo que permite una separación clara de preocupaciones y una mayor modularidad del código.

### Usos Comunes de los Decoradores:

1. **Registro y Seguimiento**: Los decoradores pueden utilizarse para llevar un registro de las llamadas a una función, medir su rendimiento o realizar un seguimiento del estado de una aplicación.

2. **Autenticación y Autorización**: Los decoradores pueden utilizarse para verificar la autenticación de un usuario antes de llamar a una función o para verificar si un usuario tiene permisos para acceder a ciertos recursos.

3. **Caching y Memoización**: Los decoradores pueden utilizarse para implementar técnicas de almacenamiento en caché o memoización para mejorar el rendimiento de las funciones que realizan cálculos costosos.

### Resumen: 

Los decoradores son una característica poderosa y flexible de Python que permite agregar funcionalidades adicionales a las funciones de manera transparente y modular. Su uso puede mejorar la legibilidad, la reutilización y el mantenimiento del código.

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