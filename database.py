import csv
import config

class Usuario:
    def __init__(self,nombre,alineacion,rango,color_sable,doble,lugar):
        self.nombre = nombre
        self.alineacion = alineacion
        self.rango = rango
        self.color_sable = color_sable
        self.doble = doble
        self.lugar = lugar

    def __str__(self):
        return """\
NOMBRE\t\t\t{}
ALINEACION\t\t{}
RANGO\t\t\t{}
COLOR SABLE\t\t{}
DOBLE\t\t\t{}
PLANETA\t\t\t{}""".format(self.nombre,self.alineacion,self.rango,self.color_sable,self.doble,self.lugar)


class Usuarios():

    lista = []
    with open(config.DATABASE_PATH, newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for nombre, alineacion, rango, color_sable, doble, lugar in reader:
            usuario = Usuario(nombre, alineacion, rango, color_sable, doble, lugar)
            lista.append(usuario)


    @staticmethod
    def buscar(nombre):
        for usuario in Usuarios.lista:
            if usuario.nombre == nombre:
                return usuario
            
    @staticmethod
    def crear(nombre, alineacion, rango, color_sable, doble, lugar):
        usuario = Usuario(nombre, alineacion, rango, color_sable, doble, lugar)
        Usuarios.lista.append(usuario)
        Usuarios.guardar()
        return usuario


    @staticmethod
    def modificar(nombre, alineacion, rango, color_sable, doble, lugar):
        for indice,usuario in enumerate(Usuarios.lista):
            if usuario.nombre == nombre:
                Usuarios.lista[indice].nombre = nombre
                Usuarios.lista[indice].alineacion = alineacion
                Usuarios.lista[indice].rango = rango
                Usuarios.lista[indice].color_sable = color_sable
                Usuarios.lista[indice].doble = doble
                Usuarios.lista[indice].lugar = lugar
                Usuarios.guardar()
                return Usuarios.lista[indice]
            
    @staticmethod
    def borrar(nombre):
        for indice,usuario in enumerate(Usuarios.lista):
            if usuario.nombre == nombre:
                usuario = Usuarios.lista.pop(indice)
                Usuarios.guardar()
                return usuario
            

    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for usuario in Usuarios.lista:
                writer.writerow((usuario.nombre,usuario.alineacion,usuario.rango,usuario.color_sable,usuario.doble,usuario.lugar))