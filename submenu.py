import os
import helpers
import database as db
import menu

def maestro():
    while True: 
        print("")
        print("      Archivo del Templo Jedi        ")
        print("=====================================")
        print("[1] Listado de usuarios de la fuerza ")
        print("[2] Buscar un usuario de la fuerza   ")
        print("[3] Añadir un usuario de la fuerza   ")
        print("[4] Modificar un usuario de la fuerza")
        print("[5] Borrar un usuario de la fuerza   ")
        print("[6] Info - Clases de acceso          ")
        print("[7] Salir del Templo Jedi            ")
        print("=====================================")

        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("Registro de los usuarios de la fuerza...\n")
            for usuario in db.Usuarios.lista:
                print(usuario, '\n') 

        elif opcion == '2':
            print("Buscando un usuario de la fuerza...\n")
            nombre = helpers.leer_texto(2, 30, "Nombre (de 2 a 30 chars)  ").capitalize()
            usuario = db.Usuarios.buscar(nombre)
            print(usuario) if usuario else print("Usuario no encontrado.")

        elif opcion == '3':
            print("Añadiendo un nuevo usuario de la fuerza..\n")
            nombre = helpers.leer_texto(2, 30, "Nombre (de 2 a 30 chars)").capitalize()
            alineacion = helpers.leer_texto(2, 30, "Alineacion (de 2 a 30 chars)").capitalize()
            rango = helpers.leer_texto(2, 30, "Rango (de 2 a 30 chars)").capitalize()
            color_sable = helpers.leer_texto(2, 30, "Color de sable (de 2 a 30 chars)").capitalize()
            doble = helpers.leer_texto(2, 30, "Doble (de 2 a 30 chars)").capitalize()
            lugar = helpers.leer_texto(2, 30, "Lugar de origen (de 2 a 30 chars)").capitalize()
            db.Usuarios.crear(nombre, alineacion, rango, color_sable, doble, lugar)
            print("Nuevo usuario añadido correctamente.")


        elif opcion == '4':
            print("Modificando un usuario de la fuerza...\n")
            nombre = helpers.leer_texto(2, 30, "Nombre (de 2 a 30 chars)").capitalize()
            usuario = db.Usuarios.buscar(nombre)
            if usuario:
                alineacion = helpers.leer_texto(
                    2, 30, f"Alineación (de 2 a 30 chars) [{usuario.alineacion}]").capitalize()
                rango = helpers.leer_texto(
                    2, 30, f"Rango (de 2 a 30 chars) [{usuario.rango}]").capitalize()
                color_sable = helpers.leer_texto(
                    2, 30, f"Color de sable (de 2 a 30 chars) [{usuario.color_sable}]").capitalize()
                doble = helpers.leer_texto(
                    2, 30, f"Doble (de 2 a 30 chars) [{usuario.doble}]").capitalize()
                lugar = helpers.leer_texto(
                    2, 30, f"Planeta de origen (de 2 a 30 chars) [{usuario.lugar}]").capitalize()
                
                db.Usuarios.modificar(usuario.nombre, alineacion, rango, color_sable, doble, lugar)
                print("Usuario modificado correctamente.")
            else:
                print("Usuario no encontrado.")

        elif opcion == '5':
            print("Borrando un usuario de la fuerza...\n")
            nombre = helpers.leer_texto(2, 30, "Nombre (de 2 a 30 chars)").capitalize()
            print("Usuario borrado correctamente.") if db.Usuarios.borrar(
                nombre) else print("Usuario no encontrado.")

        elif opcion == '6':
            print("Clase A: Acceso total sin restricciones.\n")
            print("Clase B: Acceso a consultas de usuarios sin restricciones.\n")
            print("Clase C: Acceso a consultas de usuarios limitado a la base de datos mandaloriana.\n")

        elif opcion == '7':
            print("Saliendo del Templo Jedi...\n")
            break

        input("\nPresiona ENTER para continuar...")
        helpers.limpiar_pantalla()
        print(f"Bienvenido al Templo Jedi, Maestro. Tiene acceso de clase A.")

def jedi():
    while True:
        print("")
        print("      Archivo del Templo Jedi        ")
        print("=====================================")
        print("[1] Listado de usuarios de la fuerza ")
        print("[2] Buscar un usuario de la fuerza   ")
        print("[3] Añadir un usuario de la fuerza   ")
        print("[4] Modificar un usuario de la fuerza")
        print("[5] Borrar un usuario de la fuerza   ")
        print("[6] Info - Clases de acceso          ")
        print("[7] Salir del Templo Jedi            ")
        print("=====================================")

        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("Registro de los usuarios de la fuerza...\n")
            for usuario in db.Usuarios.lista:
                print(usuario, '\n') 

        elif opcion == '2':
            print("Buscando un usuario de la fuerza...\n")
            nombre = helpers.leer_texto(2, 30, "Nombre (de 2 a 30 chars)  ").capitalize()
            usuario = db.Usuarios.buscar(nombre)
            print(usuario) if usuario else print("Usuario no encontrado.")

        elif opcion == '3':
            print("Acceso restringido. Solo para Maestros del Consejo Jedi...\n")

        elif opcion == '4':
            print("Acceso restringido. Solo para Maestros del Consejo Jedi...\n")

        elif opcion == '5':
            print("Acceso restringido. Solo para Maestros del Consejo Jedi...\n")

        elif opcion == '6':
            print("Clase A: Acceso total sin restricciones.\n")
            print("Clase B: Acceso a consultas de usuarios sin restricciones.\n")
            print("Clase C: Acceso a consultas de usuarios restringido a la base de datos mandaloriana.\n")

        elif opcion == '7':
            print("Saliendo del Templo Jedi...\n")
            break


        input("\nPresiona ENTER para volver al menú principal...")
        helpers.limpiar_pantalla()
        print(f"Bienvenido al Templo Jedi. Tiene acceso de clase B.")

def mandaloriano():
    while True:
        print("")
        print("      Archivo del Templo Jedi        ")
        print("=====================================")
        print("[1] Listado de usuarios de la fuerza ")
        print("[2] Buscar un usuario de la fuerza   ")
        print("[3] Añadir un usuario de la fuerza   ")
        print("[4] Modificar un usuario de la fuerza")
        print("[5] Borrar un usuario de la fuerza   ")
        print("[6] Info - Clases de acceso          ")
        print("[7] Salir del Templo Jedi            ")
        print("=====================================")

        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("Registro de los usuarios de la fuerza...\n")
            for usuario in db.Usuarios.lista:
                if usuario.alineacion == "Mandaloriano":
                    print(usuario, '\n') 

        elif opcion == '2':
            print("Buscando un usuario de la fuerza...\n")
            nombre = helpers.leer_texto(2, 30, "Nombre (de 2 a 30 chars)  ").capitalize()
            usuario = db.Usuarios.buscar(nombre)
            print(usuario) if usuario and usuario.alineacion == "Mandaloriano" else print("Usuario no encontrado.")


        elif opcion == '3':
            print("Acceso restringido. Solo para Maestros del Consejo Jedi...\n")

        elif opcion == '4':
            print("Acceso restringido. Solo para Maestros del Consejo Jedi...\n")

        elif opcion == '5':
            print("Acceso restringido. Solo para Maestros del Consejo Jedi...\n")

        elif opcion == '6':
            print("Clase A: Acceso total sin restricciones.\n")
            print("Clase B: Acceso a consultas de usuarios sin restricciones.\n")
            print("Clase C: Acceso a consultas de usuarios restringido a la base de datos mandaloriana.\n")

        elif opcion == '7':
            print("Saliendo del Templo Jedi...\n")
            break

        input("\nPresiona ENTER para volver al menú principal...")
        helpers.limpiar_pantalla()
        print(f"Bienvenido al Templo Jedi. Tiene acceso de clase C.")


def palpatine():
    while True: 
        print("")
        print("      Archivo del Templo Jedi        ")
        print("=====================================")
        print("[1] Listado de usuarios de la fuerza ")
        print("[2] Buscar un usuario de la fuerza   ")
        print("[3] Añadir un usuario de la fuerza   ")
        print("[4] Modificar un usuario de la fuerza")
        print("[5] Borrar un usuario de la fuerza   ")
        print("[6] Info - Clases de acceso          ")
        print("[7] Salir del Templo Jedi            ")
        print("=====================================")

        opcion = input("> ")
        helpers.limpiar_pantalla()

        if opcion == '1':
            print("Registro de los usuarios de la fuerza...\n")
            for usuario in db.Usuarios.lista:
                print(usuario, '\n') 

        elif opcion == '2':
            print("Buscando un usuario de la fuerza...\n")
            nombre = helpers.leer_texto(2, 30, "Nombre (de 2 a 30 chars)  ").capitalize()
            usuario = db.Usuarios.buscar(nombre)
            print(usuario) if usuario else print("Usuario no encontrado.")

        elif opcion == '3':
            print("Añadiendo un nuevo usuario de la fuerza..\n")
            nombre = helpers.leer_texto(2, 30, "Nombre (de 2 a 30 chars)").capitalize()
            alineacion = helpers.leer_texto(2, 30, "Alineacion (de 2 a 30 chars)").capitalize()
            rango = helpers.leer_texto(2, 30, "Rango (de 2 a 30 chars)").capitalize()
            color_sable = helpers.leer_texto(2, 30, "Color de sable (de 2 a 30 chars)").capitalize()
            doble = helpers.leer_texto(2, 30, "Doble (de 2 a 30 chars)").capitalize()
            lugar = helpers.leer_texto(2, 30, "Lugar de origen (de 2 a 30 chars)").capitalize()
            db.Usuarios.crear(nombre, alineacion, rango, color_sable, doble, lugar)
            print("Nuevo usuario añadido correctamente.")


        elif opcion == '4':
            print("Modificando un usuario de la fuerza...\n")
            nombre = helpers.leer_texto(2, 30, "Nombre (de 2 a 30 chars)").capitalize()
            usuario = db.Usuarios.buscar(nombre)
            if usuario:
                alineacion = helpers.leer_texto(
                    2, 30, f"Alineación (de 2 a 30 chars) [{usuario.alineacion}]").capitalize()
                rango = helpers.leer_texto(
                    2, 30, f"Rango (de 2 a 30 chars) [{usuario.rango}]").capitalize()
                color_sable = helpers.leer_texto(
                    2, 30, f"Color de sable (de 2 a 30 chars) [{usuario.color_sable}]").capitalize()
                doble = helpers.leer_texto(
                    2, 30, f"Doble (de 2 a 30 chars) [{usuario.doble}]").capitalize()
                lugar = helpers.leer_texto(
                    2, 30, f"Planeta de origen (de 2 a 30 chars) [{usuario.lugar}]").capitalize()
                
                db.Usuarios.modificar(usuario.nombre, alineacion, rango, color_sable, doble, lugar)
                print("Usuario modificado correctamente.")
            else:
                print("Usuario no encontrado.")

        elif opcion == '5':
            print("Borrando un usuario de la fuerza...\n")
            nombre = helpers.leer_texto(2, 30, "Nombre (de 2 a 30 chars)").capitalize()
            print("Usuario borrado correctamente.") if db.Usuarios.borrar(
                nombre) else print("Usuario no encontrado.")

        elif opcion == '6':
            print("Clase A: Acceso total sin restricciones.\n")
            print("Clase B: Acceso a consultas de usuarios sin restricciones.\n")
            print("Clase C: Acceso a consultas de usuarios limitado a la base de datos mandaloriana.\n")

        elif opcion == '7':
            print("Saliendo del Templo Jedi...\n")
            break

        input("\nPresiona ENTER para continuar...")
        helpers.limpiar_pantalla()
        print(f"Bienvenido al Templo Jedi, Canciller. Como Pedro por su casa.")


        