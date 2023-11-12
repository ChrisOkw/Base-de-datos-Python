import os
import helpers
import database as db
import menu
import submenu

def anakin():
    print("=====================================")
    print("    Bienvenido al Templo Jedi        ")
    print("=====================================")
    print("        ¿Qué Anakin eres?            ")
    print("[1] Episodio 1                       ")
    print("[2] Episodio 2                       ")
    print("[3] Episodio 3                       ")

    opcion = input("> ")
    helpers.limpiar_pantalla()

    if opcion == '1':
        print(f"Bienvenido al Templo Jedi, padawan Anakin. Por tu culpa murió Qua-gon Jin, más te vale ser el elegido.")
        submenu.jedi()
    
    elif opcion == '2':
        print(f"Bienvenido al Templo Jedi, Anakin. Te tenemos envidia y por eso no te hacemos maestro. Tienes acceso de clase B.")
        submenu.jedi()

    elif opcion == '3':
        print("Bienvenido, maestro Anakin. Además de tener acceso total al archivo, tiene a todos los padawan que quiera a su disposición. Diviértase.")
        submenu.maestro()