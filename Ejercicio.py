# Clase usuario
class Usuario:
    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña

# Objeto
Usuario1 = Usuario("Ander", "contraseña")

print("Nombre de usuario:", Usuario1.nombre_usuario)
print("Contraseña:", Usuario1.contraseña)