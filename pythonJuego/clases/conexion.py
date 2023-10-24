import sqlite3 as slq


class Conexion:
    def __init__(self, nombreBaseDatos):
        self.conexion = slq.connect(nombreBaseDatos)
        self.cursor = self.conexion.cursor()

    def crearTabla(self):
        self.cursor.execute(
            '''CREATE TABLE IF NOT EXISTS jugador (id integer PRIMARY KEY AUTOINCREMENT, nombre varchar(50), marcador integer)''')
        self.conexion.commit()

    def agregar(self, nombre, marcador):
        self.cursor.execute('''INSERT INTO jugador (nombre,marcador) VALUES(?,?)''', (nombre, marcador))
        self.conexion.commit()

    def modificar(self, nombre, marcador, id):
        self.cursor.execute('''UPDATE jugador set nombre=?,marcador=? where id=?''',
                            (nombre, marcador, id))
        self.conexion.commit()

    def eliminar(self, id):
        self.cursor.execute('''DELETE from jugador where id=?''', (id))
        self.conexion.commit()

    def mostrar(self):
        self.cursor.execute('''SELECT * FROM jugador''')
        resultado = self.cursor.fetchall()
        return resultado

    def cerrarBd(self):
        self.cursor.close()
        self.conexion.close()

