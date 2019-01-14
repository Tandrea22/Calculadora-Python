from tkinter import*

r= Tk()

mFrame= Frame(r)

mFrame.pack()
operacion=""
memoriaSuma=0
memoriaResta = 0
memoriaMulti = 1
memoriaDivi = 1

#----------Pantalla----------
npantalla= StringVar()

pantalla=Entry(mFrame,textvariable= npantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10,columnspan=4)
pantalla.config(background="Black", fg="white", justify="right")

#-------------Pulsaciones

def pul(num):
    if npantalla.get() == "0" and num == "0" :
        npantalla.set("0")
    elif npantalla.get() == "0" and num == ",":
        npantalla.set("0,")
    elif npantalla.get() == "0" and num != "0":
        npantalla.set(num)
    else:
        if npantalla.get().count(",") == 0:
            npantalla.set(npantalla.get() + num)
        elif npantalla.get().count(",") >= 1 and num == ",":
            npantalla.get()
        else:
            npantalla.set(npantalla.get() + num)
#-----------------------BORRAR----------------------------------

def borra():
    borrado = npantalla.get()
    npantalla.set(borrado[0:-1])

#-------------Operaciones

def suma():
    global operacion
    global memoriaSuma
    global memoriaResta
    global memoriaMulti
    global memoriaDivi
    operacion = "suma"

    if memoriaResta == 0 and memoriaMulti == 1 and memoriaDivi == 1:
        if(npantalla.get()==""):
            npantalla.set("0")
            memoriaSuma = memoriaSuma + int(npantalla.get())
            npantalla.set("0")
        else:
            memoriaSuma = memoriaSuma + int(npantalla.get())
            npantalla.set("0")

    else:
        if(npantalla.get()==""):
               npantalla.set("0")
               if memoriaResta != 0:
                   memoriaSuma = memoriaResta - int(npantalla.get())
                   npantalla.set("0")
                   memoriaResta = 0
               elif memoriaMulti != 1:
                      memoriaSuma = memoriaMulti * int(npantalla.get())
                      npantalla.set("0")
                      memoriaMulti = 1
               else:
                  memoriaSuma = memoriaDivi / int(npantalla.get())
                  npantalla.set("0")
                  memoriaDivi = 1
        else:
            if memoriaResta != 0:
                   memoriaSuma = memoriaResta - int(npantalla.get())
                   npantalla.set("0")
                   memoriaResta = 0
            elif memoriaMulti != 1:
                      memoriaSuma = memoriaMulti * int(npantalla.get())
                      npantalla.set("0")
                      memoriaMulti = 1
            else:
                  memoriaSuma = memoriaDivi / int(npantalla.get())
                  npantalla.set("0")
                  memoriaDivi = 1



def resta():
    global operacion
    global memoriaResta
    global memoriaSuma
    global memoriaMulti
    global memoriaDivi
    operacion = "resta"

    if memoriaSuma == 0 and memoriaMulti == 1 and memoriaDivi == 1:
        if memoriaResta == 0:
            if(npantalla.get()==""):
              npantalla.set("0")
              memoriaResta = int(npantalla.get()) - memoriaResta
            else:
              memoriaResta = int(npantalla.get()) - memoriaResta
        else:
             if(npantalla.get()==""):
               npantalla.set("0")
               memoriaResta = memoriaResta - int(npantalla.get())
             else:
               memoriaResta = memoriaResta - int(npantalla.get())
    else:
         if(npantalla.get()==""):
              npantalla.set("0")
              if memoriaSuma != 0:
                memoriaResta = memoriaSuma + int(npantalla.get())
                npantalla.set("0")
                memoriaSuma = 0
              elif memoriaMulti != 1:
                 memoriaResta = memoriaMulti * int(npantalla.get())
                 npantalla.set("0")
                 memoriaMulti = 1
              else:
                  memoriaResta = memoriaDivi / int(npantalla.get())
                  npantalla.set("0")
                  memoriaDivi = 1
         else:
              if memoriaSuma != 0:
                memoriaResta = memoriaSuma + int(npantalla.get())
                npantalla.set("0")
                memoriaSuma = 0
              elif memoriaMulti != 1:
                 memoriaResta = memoriaMulti * int(npantalla.get())
                 npantalla.set("0")
                 memoriaMulti = 1
              else:
                  memoriaResta = memoriaDivi / int(npantalla.get())
                  npantalla.set("0")
                  memoriaDivi = 1

    npantalla.set("0")



def multi():
    global operacion
    global memoriaMulti
    global memoriaSuma
    global memoriaResta
    global memoriaDivi
    operacion = "multi"

    if memoriaSuma == 0 and memoriaResta == 0 and memoriaDivi == 1:
        if(npantalla.get()==""):
            npantalla.set("0")
            memoriaMulti = int(npantalla.get()) * memoriaMulti
            npantalla.set("0")
        else:
            memoriaMulti = int(npantalla.get()) * memoriaMulti
            npantalla.set("0")
    else:
         if(npantalla.get()==""):
            npantalla.set("0")
            if memoriaSuma != 0:
                memoriaMulti = memoriaSuma + int(npantalla.get())
                npantalla.set("0")
                memoriaSuma = 0
            elif memoriaResta != 0:
                memoriaMulti = memoriaResta - int(npantalla.get())
                npantalla.set("0")
                memoriaResta = 0
            else:
                memoriaMulti = memoriaDivi / int(npantalla.get())
                npantalla.set("0")
                memoriaDivi = 1
         else:
             if memoriaSuma != 0:
                memoriaMulti = memoriaSuma + int(npantalla.get())
                npantalla.set("0")
                memoriaSuma = 0
             elif memoriaResta != 0:
                memoriaMulti = memoriaResta - int(npantalla.get())
                npantalla.set("0")
                memoriaResta = 0
             else:
                memoriaMulti = memoriaDivi / int(npantalla.get())
                npantalla.set("0")
                memoriaDivi = 1


def divi():
    global operacion
    global memoriaDivi
    global memoriaSuma
    global memoriaResta
    global memoriaMulti
    operacion = "divi"

    if memoriaSuma == 0 and memoriaResta == 0 and memoriaMulti == 1:
        if(npantalla.get()==""):
            npantalla.set("0")
            memoriaDivi = int(npantalla.get()) / memoriaDivi
            npantalla.set("0")
        else:
            memoriaDivi = int(npantalla.get()) / memoriaDivi
            npantalla.set("0")
    else:
        if(npantalla.get()==""):
            npantalla.set("0")
            if memoriaSuma != 0:
              memoriaDivi = memoriaSuma + int(npantalla.get())
              npantalla.set("0")
              memoriaSuma = 0
            elif memoriaResta != 0:
              memoriaDivi = memoriaResta - int(npantalla.get())
              npantalla.set("0")
              memoriaResta = 0
            else:
              memoriaDivi = memoriaMulti * int(npantalla.get())
              npantalla.set("0")
              memoriaMulti = 1
        else:
            if memoriaSuma != 0:
              memoriaDivi = memoriaSuma + int(npantalla.get())
              npantalla.set("0")
              memoriaSuma = 0
            elif memoriaResta != 0:
              memoriaDivi = memoriaResta - int(npantalla.get())
              npantalla.set("0")
              memoriaResta = 0
            else:
              memoriaDivi = memoriaMulti * int(npantalla.get())
              npantalla.set("0")
              memoriaMulti = 1



def igual():
    global operacion
    global memoriaSuma
    global memoriaResta
    global memoriaMulti
    global memoriaDivi

    if operacion == "suma":
        npantalla.set(memoriaSuma + int(npantalla.get()))
        memoriaSuma = 0
    elif operacion == "resta":
        npantalla.set(memoriaResta - int(npantalla.get()))
        memoriaResta = 0
    elif operacion == "multi":
        npantalla.set(memoriaMulti * int(npantalla.get()))
        memoriaMulti = 1
    else:
        if npantalla.get()=="":
            npantalla.set("Error")

        else:
            npantalla.set(memoriaDivi / int(npantalla.get()))
            memoriaDivi = 1


#-----------Fila 1------------

btn7= Button(mFrame,text="7", width=8, command=lambda:pul("7"))
btn7.grid(row=2, column=1)
btn8= Button(mFrame,text="8", width=8, command=lambda:pul("8"))
btn8.grid(row=2, column=2)
btn9= Button(mFrame,text="9", width=8, command=lambda:pul("9"))
btn9.grid(row=2, column=3)
btnDiv= Button(mFrame,text="/", width=8,command=lambda:divi())
btnDiv.grid(row=2, column=4)

#-----------Fila 2------------

btn4= Button(mFrame,text="4", width=8, command=lambda:pul("4"))
btn4.grid(row=3, column=1)
btn5= Button(mFrame,text="5", width=8, command=lambda:pul("5"))
btn5.grid(row=3, column=2)
btn6= Button(mFrame,text="6", width=8, command=lambda:pul("6"))
btn6.grid(row=3, column=3)
btnM= Button(mFrame,text="x", width=8,command=lambda:multi())
btnM.grid(row=3, column=4)

#-----------Fila 3-----------

btn1= Button(mFrame,text="1", width=8, command=lambda:pul("1"))
btn1.grid(row=4, column=1)
btn2= Button(mFrame,text="2", width=8, command=lambda:pul("2"))
btn2.grid(row=4, column=2)
btn3= Button(mFrame,text="3", width=8, command=lambda:pul("3"))
btn3.grid(row=4, column=3)
btnR= Button(mFrame,text="-", width=8,command=lambda:resta())
btnR.grid(row=4, column=4)

#-----------Fila 4-----------

btn0= Button(mFrame,text="0", width=8, command=lambda:pul("0"))
btn0.grid(row=5, column=1)
btnc= Button(mFrame,text=",", width=8,command=lambda:pul(","))
btnc.grid(row=5, column=2)
btnI= Button(mFrame,text="=", width=8,command=lambda:igual())
btnI.grid(row=5, column=3)
btnS= Button(mFrame,text="+", width=8,command=lambda:suma() )
btnS.grid(row=5, column=4)

#----------------------------FILA 5----------------------------------

botonBorra=Button(mFrame,text="Borrar",width=18,fg="black",command=lambda:borra())
botonBorra.grid(row=6,column=2,columnspan=2,pady=10)



r.mainloop()
