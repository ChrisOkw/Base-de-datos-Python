import unittest
import database as db
import copy
import config
import csv

class TestDatabase(unittest.TestCase):

    def setUp(self):
        db.Usuarios.lista = [
            db.Usuario("Yoda", "Jedi", "Maestro", "Verde", "No", "Terragrogu"),   
            db.Usuario("Maul", "Sith", "Aprendiz", "Rojo", "Sí", "Dathomir"),
            db.Usuario("Ezra", "Jedi", "Ronin", "Azul", "No", "Lothal"),
        ]
    
    def test_buscar_usuario(self):
        usuario_existente = db.Usuarios.buscar("Yoda")
        usuario_inexistente = db.Usuarios.buscar("Rex")
        self.assertIsNotNone(usuario_existente)
        self.assertIsNone(usuario_inexistente)

    def test_crear_usuario(self):
        nuevo_usuario = db.Usuarios.crear("Windu", "Jedi", "Maestro", "Lila", "No", "Coruscant")
        usuario_inexistente = db.Usuarios.buscar("Rex")
        self.assertEqual(len(db.Usuarios.lista), 4)
        self.assertEqual(nuevo_usuario.nombre, "Windu")
        self.assertEqual(nuevo_usuario.alineacion, "Jedi")
        self.assertEqual(nuevo_usuario.rango, "Maestro")

    def test_modificar_usuario(self):
        usuario_a_modificar = copy.copy(db.Usuarios.buscar("Yoda"))
        usuario_modificado = db.Usuarios.modificar("Yoda","Jedi", "Maestro", "Amarillo", "No", "Terragrogu")
        self.assertEqual(usuario_a_modificar.color_sable, "Verde")
        self.assertEqual(usuario_modificado.color_sable, "Amarillo")

    def test_borrar_usuario(self):
        usuario_borrado = db.Usuarios.borrar("Ezra")
        usuario_rebuscado = db.Usuarios.buscar("Ezra")
        self.assertEqual(usuario_borrado.nombre, "Ezra")
        self.assertIsNone(usuario_rebuscado)

    def test_escritura_csv(self):
        db.Usuarios.borrar('Yoda')
        db.Usuarios.borrar('Ezra')
        db.Usuarios.modificar('Maul', "Gris", "Ronin", "Rojo", "Sí", "Dathomir")

        nombre, alineacion, rango, color_sable, doble, lugar = None, None, None, None, None, None
        with open(config.DATABASE_PATH, newline='\n') as fichero:
            reader = csv.reader(fichero, delimiter=';')
            nombre, alineacion, rango, color_sable, doble, lugar = next(reader)
                                                                        
        self.assertEqual(nombre, 'Maul')
        self.assertEqual(alineacion, 'Gris')
        self.assertEqual(rango, 'Ronin')
        self.assertEqual(color_sable, 'Rojo')
        self.assertEqual(doble, 'Sí')
        self.assertEqual(lugar, 'Dathomir')


