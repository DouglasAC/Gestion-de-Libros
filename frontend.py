from tkinter import *
from tkinter import messagebox 
from backend import Database

class BibliotecaApp:

    def __init__(self, window):
        self.window = window
        # Título de la ventana
        self.window.wm_title("Aplicación de libros")

        # Crear una instancia de la clase Database
        self.database = Database("libros.db")

        # Etiquetas para los campos de entrada
        l1 = Label(window, text="Titulo")
        l1.grid(row=0, column=0)

        l2 = Label(window, text="Autor")
        l2.grid(row=0, column=2)

        l3 = Label(window, text="Año")
        l3.grid(row=1, column=0)

        l4 = Label(window, text="ISBN")
        l4.grid(row=1, column=2)

        # Campos de entrada para los datos
        self.titulo_valor = StringVar()
        self.e1 = Entry(window, textvariable=self.titulo_valor)
        self.e1.grid(row=0, column=1)

        self.autor_valor = StringVar()
        self.e2 = Entry(window, textvariable=self.autor_valor)
        self.e2.grid(row=0, column=3)

        self.anio_valor = StringVar()
        self.e3 = Entry(window, textvariable=self.anio_valor)
        self.e3.grid(row=1, column=1)

        self.isbn_valor = StringVar()
        self.e4 = Entry(window, textvariable=self.isbn_valor)
        self.e4.grid(row=1, column=3)

        # Lista para mostrar los datos y barra de desplazamiento vertical
        self.list1 = Listbox(window, height=6, width=35)
        self.list1.grid(row=2, column=0, rowspan=6, columnspan=2)

        self.sb1 = Scrollbar(window)
        self.sb1.grid(row=3, column=2, rowspan=4, sticky='ns')

        # Barra de desplazamiento horizontal
        self.sb2 = Scrollbar(window, orient=HORIZONTAL)
        self.sb2.grid(row=7, column=0, columnspan=2, sticky='ew')

        self.list1.configure(xscrollcommand=self.sb2.set)
        self.sb2.configure(command=self.list1.xview)

        # Vincular la lista y la barra de desplazamiento
        self.list1.configure(yscrollcommand=self.sb1.set)
        self.sb1.configure(command=self.list1.yview)

        self.list1.bind('<<ListboxSelect>>', self.fila_seleccionada)


        # Botones para las acciones
        b1 = Button(window, text="Ver todos", width=15, command=self.ver_comando)
        b1.grid(row=2, column=3)

        b2 = Button(window, text="Buscar entrada", width=15, command=self.buscar_comando)
        b2.grid(row=3, column=3)

        b3 = Button(window, text="Agregar entrada", width=15, command=self.agregar_comando)
        b3.grid(row=4, column=3)

        b4 = Button(window, text="Actualizar seleccion", width=15, command=self.actualizar_comando)
        b4.grid(row=5, column=3)

        b5 = Button(window, text="Borrar seleccion", width=15, command=self.eliminar_comando)
        b5.grid(row=6, column=3)

        b6 = Button(window, text="Cerrar", width=15, command=window.destroy)
        b6.grid(row=7, column=3)

    # Funcion para obtener la fila seleccionada
    def fila_seleccionada(self, event):
        try:
            index = self.list1.curselection()[0]
            self.seleccionada = self.list1.get(index)
            self.e1.delete(0, END)
            self.e1.insert(END, self.seleccionada[1])
            self.e2.delete(0, END)
            self.e2.insert(END, self.seleccionada[2])
            self.e3.delete(0, END)
            self.e3.insert(END, self.seleccionada[3])
            self.e4.delete(0, END)
            self.e4.insert(END, self.seleccionada[4])
        except IndexError:
            pass

    # Funciones que conectan el backend con el frontend
    # Ver todos los registros
    def ver_comando(self):
        self.list1.delete(0, END)
        for row in self.database.ver():
            self.list1.insert(END, row)

    # Buscar un registro
    def buscar_comando(self):
        self.list1.delete(0, END)
        for row in self.database.buscar(self.titulo_valor.get(), self.autor_valor.get(), self.anio_valor.get(), self.isbn_valor.get()):
            self.list1.insert(END, row)

    # Crear un registro
    def agregar_comando(self):
        self.database.insertar(self.titulo_valor.get(), self.autor_valor.get(), self.anio_valor.get(), self.isbn_valor.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.titulo_valor.get(), self.autor_valor.get(), self.anio_valor.get(), self.isbn_valor.get()))

    # Eliminar un registro
    def eliminar_comando(self):
        try:
            if messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar este registro?"):
                self.database.eliminar(self.seleccionada[0])
                self.ver_comando()
        except AttributeError:
            messagebox.showerror("Error", "Selecciona un registro primero")

    # Actualizar un registro
    def actualizar_comando(self):
        self.database.actualizar(self.seleccionada[0], self.titulo_valor.get(), self.autor_valor.get(), self.anio_valor.get(), self.isbn_valor.get())
        self.ver_comando()





# Ejecutar la aplicación
if __name__ == "__main__":
    root = Tk()
    app = BibliotecaApp(root)
    root.mainloop()