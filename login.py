# login.py
# Simulación de inicio de sesión de un estudiante en EduPlus

def login(usuario, contrasena):
    if usuario == "estudiante" and contrasena == "1234":
        return "Inicio de sesión exitoso. ¡Bienvenido a EduPlus!"
    else:
        return "Error: usuario o contraseña incorrectos."

# Prueba rápida
print(login("estudiante", "1234"))
print(login("otro", "5678"))



