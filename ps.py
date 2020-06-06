from tkinter import ttk
from tkinter import *
import math
import datetime

class Desk:
    def __init__(self, window):
        
        ancho = 600
        
        alto = 300
        
        self.wind = window

        
        self.wind.geometry(str(ancho)+'x'+str(alto))

        self.wind.columnconfigure(0, weight=1)
        self.wind.title('Exámen Final')
        

        frame = LabelFrame(self.wind, text = '')
        frame.grid(row = 0, column = 0, columnspan = 8, pady = 20)   

        Label(frame, text = 'BIENVENIDO').grid(row = 0, column = 2)   
        
        Label(frame, text = 'Nombre: ', bg="light sky blue").grid(row = 1, column = 0)
       
        self.variable1 = Entry(frame)
        self.variable1.focus()
        self.variable1.grid(row = 1, columnspan = 6)

        Label(frame, text = 'Apellido: ', bg='light sky blue').grid(row = 2, column = 0)
        self.variable2 = Entry(frame)
        self.variable2.grid(row = 2, columnspan = 6)

        Label(frame, text = 'Día: ', bg='light sky blue').grid(row = 3, column = 0)
        self.variable3 = Entry(frame)
        self.variable3.grid(row = 3, columnspan = 6)

        Label(frame, text = 'Mes: ', bg='light sky blue').grid(row = 4, column = 0)
        self.variable4 = Entry(frame)
        self.variable4.grid(row = 4, columnspan = 6)

        Label(frame, text = 'Año: ', bg='light sky blue').grid(row = 5, column = 0)
        self.variable5 = Entry(frame)
        self.variable5.grid(row = 5, columnspan = 6)


        
        Button(frame, text = 'función 1', command = self.funcion1).grid(row = 6, column = 0 , sticky = W + E)
        Button(frame, text = 'función 2', command = self.funcion2).grid(row = 6, column = 1 , sticky = W + E)
        Button(frame, text = 'función 3', command = self.funcion3).grid(row = 6, column = 2 , sticky = W + E)
        Button(frame, text = 'función 4', command = self.funcion4).grid(row = 6, column = 3 , sticky = W + E)
        Button(frame, text = 'función 5', command = self.funcion5).grid(row = 6, column = 4 , sticky = W + E)
 



        
        self.message = Label(text = '', bg='light sky blue')
        self.message.grid(row = 3, column = 0, columnspan = 2)

    
    def funcion1(self):
        dia=int(self.variable3.get())
        mes=int(self.variable4.get())
        anio=int(self.variable5.get())
        a=format(dia, '0b' )
        b=format(mes, '0b')
        c=format(anio, '0b')

        self.message['text'] = 'La fecha es: {}/{}/{} = {}/{}/{}'.format(dia,mes,anio,a,b,c)


    def funcion2(self):
            
        dia=int(self.variable3.get())
        mes=int(self.variable4.get())
        anio=int(self.variable5.get())
        fecha_de_nacimiento = datetime.datetime(anio, mes, dia)
        fecha_actual = datetime.datetime.now()
        diferencia = fecha_actual - fecha_de_nacimiento
        dias_vividos = diferencia.days
        self.message['text'] = 'Usted nació {}/{}/{} y a vivido {} días'.format(dia,mes,anio,dias_vividos)

    def funcion3(self):
        nombre=str(self.variable1.get())
        apellido=str(self.variable2.get())
        nombre1=int(len(nombre))
        apellido1=int(len(apellido))
        if nombre1%2==0 and apellido1 %2==0 :
            self.message['text'] = '{} tiene cantidad de letras par, {} tiene cantidad de letras par'.format(nombre,apellido)
        elif nombre1%2==0 and apellido1 %2==1:
            self.message['text'] = '{} tiene cantidad de letras par, {} tiene cantidad de letras impar'.format(nombre,apellido)
        elif nombre1%2==1 and apellido1 %2==0:
            self.message['text'] = '{} tiene cantidad de letras impar,{} tiene cantidad de letras par'.format(nombre,apellido)
        else:
            self.message['text'] = '{} tiene cantidad de letras impar , {} tiene cantidad de letras impar'.format(nombre,apellido)

    def funcion4(self):
        nombre=str(self.variable1.get())
        apellido=str(self.variable2.get())
        cuenta = 0
        for carac in nombre:
            if carac == 'a' or carac =='A' or carac =='e' or carac =='E' or carac =='i' or carac=='I' or carac=='o' or carac=="O" or carac=="u" or carac=="U":
                cuenta += 1
        for carac in apellido:
            if carac == 'a' or carac =='A' or carac =='e' or carac =='E' or carac =='i' or carac=='I' or carac=='o' or carac=="O" or carac=="u" or carac=="U":
                cuenta += 1
        cuntal=len(nombre)
        cuntal1=len(apellido)
        consonante=cuntal+cuntal1-cuenta

        self.message['text'] = 'Su nombre y apellido tienen {} vocales y {} consonantes'.format(cuenta,consonante)
     

    def funcion5(self):
        nombre=str(self.variable1.get())
        apellido=str(self.variable2.get())
        cadena_invertida = ""
        cadena_invertida1= ""
        for letra in nombre:
            cadena_invertida = letra + cadena_invertida
        for letra1 in apellido:
            cadena_invertida1 = letra1 + cadena_invertida1
        self.message['text'] = 'Su nombre es {} {} y al revés es {} {}'.format(nombre,apellido,cadena_invertida,cadena_invertida1)


if __name__ == '__main__':
    
    
    window = Tk()
    
    
    app = Desk(window)

  
    window.mainloop()

