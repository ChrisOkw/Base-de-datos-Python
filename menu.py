import os
import database as db
import helpers
import submenu
import anakin


def iniciar():
    while True:
        helpers.limpiar_pantalla()
        print("Bienvenido, identifíquese para poder acceder al Templo Jedi")

        nombre_usuario = input("Nombre: ").capitalize()
        usuario = db.Usuarios.buscar(nombre_usuario)  # Buscar al usuario en la base de datos

        if usuario:
            if usuario.nombre == "Anakin":
                anakin.anakin()

            if usuario.nombre == "Palpatine":
                helpers.limpiar_pantalla()
                print(f"Bienvenido al Templo Jedi, Canciller. Sabemos que tiene reliquias Sith en su despacho, pero le damos acceso de clase A VIP.")
                submenu.palpatine()
            
            elif usuario.rango == "Maestro":
                helpers.limpiar_pantalla()
                print(f"Bienvenido al Templo Jedi, Maestro {nombre_usuario}. Tiene acceso de clase A.")
                submenu.maestro()

            elif usuario.alineacion == "Sith":
                helpers.limpiar_pantalla()
                print(f"Eres {nombre_usuario}, un Sith reconocido. Sabemos que dejamos entrar muchos años a Palpatine, pero por suerte hemos mejorado la seguridad. \nLo siento, no podemos dejarte entrar.")
                
            elif usuario.alineacion == "Jedi":
                helpers.limpiar_pantalla()
                print(f"Bienvenido al Templo Jedi, {nombre_usuario}. Tiene acceso de clase B.")
                submenu.jedi()

            elif usuario.alineacion == "Mandaloriano":
                helpers.limpiar_pantalla()
                print(f"Bienvenido al Templo Jedi, {nombre_usuario}. Los mandalorianos tienen un acceso limitado de clase C. Solo puede ver registros de mandalorianos.")
                submenu.mandaloriano()

        else:
            print("Usuario deconocido. No estás autorizado para ingresar al Templo Jedi.")
        
        input("\nPresiona ENTER para volver a intentarlo...")





