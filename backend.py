import sqlite3

# Función para conectar a la base de datos
def connect():
    conn = sqlite3.connect('libros.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS libros (id INTEGER PRIMARY KEY, titulo TEXT, autor TEXT, anio INTEGER, isbn INTEGER)')
    conn.commit()
    conn.close()

# Función para insertar datos en la base de datos
def insertar(titulo, autor, anio, isbn):
    conn = sqlite3.connect('libros.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO libros VALUES (NULL, ?, ?, ?, ?)', (titulo, autor, anio, isbn))
    conn.commit()
    conn.close()

# Función para mostrar los datos en la lista
def ver():
    conn = sqlite3.connect('libros.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM libros')
    rows = cur.fetchall()
    conn.close()
    return rows

# Función para buscar datos en la base de datos
def buscar(titulo="", author="", anio="", isbn=""):
    conn = sqlite3.connect('libros.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM libros WHERE titulo=? OR autor=? OR anio=? OR isbn=?', (titulo, author, anio, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

# Función para eliminar datos de la base de datos
def eliminar(id):
    conn = sqlite3.connect('libros.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM libros WHERE id=?', (id,))
    conn.commit()
    conn.close()

# Función para actualizar datos en la base de datos
def actualizar(id, titulo, autor, anio, isbn):
    conn = sqlite3.connect('libros.db')
    cur = conn.cursor()
    cur.execute('UPDATE libros SET titulo=?, autor=?, anio=?, isbn=? WHERE id=?', (titulo, autor, anio, isbn, id))
    conn.commit()
    conn.close()

# Llamar a la función connect() para conectar a la base de datos
connect()