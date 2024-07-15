from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymongo

URLmongo = 'mongodb://localhost:27017/'
conex = pymongo.MongoClient(URLmongo, serverSelectionTimeoutMS=1000)
baseData = conex['Tkinter']
collection = baseData['Trabajador']

def mostrarData():
    try:
        
        for x in collection.find():
            tabla.insert('', 0, text=x['_id'], values=x['nombre'])

    except Exception as ex:
        print('Error: ',ex)

def crearRegistro():
    if len(nombre.get()) != 0 and len(edad.get()) != 0:
        x = {'nombre': nombre.get(),
             'edad': edad.get()}
        try:
            collection.insert_one(x)
        except Exception as ex:
            print('Error: ',ex)
    mostrarData()


app = Tk()

tabla = ttk.Treeview(app, columns=2)
tabla.grid(row=1,column=0,columnspan=2)
tabla.heading('#0', text='ID')
tabla.heading('#1', text='nombre')
#nombre
Label(app, text='nombre').grid(row=2,column=0)
nombre = Entry(app)
nombre.grid(row=2, column=1)

#edad
Label(app, text='edad').grid(row=3,column=0)
edad = Entry(app)
edad.grid(row=3, column=1)

#crear boton

create = Button(app, text='Crear x', command=crearRegistro, bg='green', fg='white')
create.grid(row=5, columnspan=2)
mostrarData()
app.mainloop()