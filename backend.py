import sqlite3

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.inicializar()

    # Función para inicializar la base de datos
    def inicializar(self):
        with sqlite3.connect(self.db_name) as conn:
            cur = conn.cursor()
            cur.execute('CREATE TABLE IF NOT EXISTS libros (id INTEGER PRIMARY KEY, titulo TEXT, autor TEXT, anio INTEGER, isbn INTEGER)')
            conn.commit()

    # Función para insertar datos en la base de datos
    def insertar(self, titulo, autor, anio, isbn):
        with sqlite3.connect(self.db_name) as conn:
            cur = conn.cursor()
            cur.execute('INSERT INTO libros VALUES (NULL, ?, ?, ?, ?)', (titulo, autor, anio, isbn))
            conn.commit()

    # Función para mostrar los datos en la lista
    def ver(self):
        with sqlite3.connect(self.db_name) as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM libros')
            rows = cur.fetchall()
        return rows

    # Función para buscar datos en la base de datos
    def buscar(self, titulo="", autor="", anio="", isbn=""):
        with sqlite3.connect(self.db_name) as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM libros WHERE titulo=? OR autor=? OR anio=? OR isbn=?', (titulo, autor, anio, isbn))
            rows = cur.fetchall()
        return rows

    # Función para eliminar datos de la base de datos
    def eliminar(self, id):
        with sqlite3.connect(self.db_name) as conn:
            cur = conn.cursor()
            cur.execute('DELETE FROM libros WHERE id=?', (id,))
            conn.commit()

    # Función para actualizar datos en la base de datos
    def actualizar(self, id, titulo, autor, anio, isbn):
        with sqlite3.connect(self.db_name) as conn:
            cur = conn.cursor()
            cur.execute('UPDATE libros SET titulo=?, autor=?, anio=?, isbn=? WHERE id=?', (titulo, autor, anio, isbn, id))
            conn.commit()