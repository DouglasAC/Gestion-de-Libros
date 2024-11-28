import sqlite3

class Database():
    # Función para inicializar 
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.cur = self.conn.cursor()
        self.cur.execute('CREATE TABLE IF NOT EXISTS libros (id INTEGER PRIMARY KEY, titulo TEXT, autor TEXT, anio INTEGER, isbn INTEGER)')
        self.conn.commit()

    # Función para insertar datos en la base de datos
    def insertar(self, titulo, autor, anio, isbn):
        self.cur.execute('INSERT INTO libros VALUES (NULL, ?, ?, ?, ?)', (titulo, autor, anio, isbn))
        self.conn.commit()

    # Función para mostrar los datos en la lista
    def ver(self):
        self.cur.execute('SELECT * FROM libros')
        rows = self.cur.fetchall()
        return rows

    # Función para buscar datos en la base de datos
    def buscar(self, titulo="", author="", anio="", isbn=""):
        self.cur.execute('SELECT * FROM libros WHERE titulo=? OR autor=? OR anio=? OR isbn=?', (titulo, author, anio, isbn))
        rows = self.cur.fetchall()
        return rows

    # Función para eliminar datos de la base de datos
    def eliminar(self, id):
        self.cur.execute('DELETE FROM libros WHERE id=?', (id,))
        self.conn.commit()

    # Función para actualizar datos en la base de datos
    def actualizar(self, id, titulo, autor, anio, isbn):
        self.cur.execute('UPDATE libros SET titulo=?, autor=?, anio=?, isbn=? WHERE id=?', (titulo, autor, anio, isbn, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()