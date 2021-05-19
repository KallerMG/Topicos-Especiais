from tkinter import *
import sistema
from threading import Thread
import asyncio

import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import animation


def atualizar():
    async def iniciarAtt():
        valores = sistema.coletasDadosAtual()

        entCpuUso.delete(0, END)
        entCpuUso.insert(INSERT, valores[0])

        entCpuTemp.delete(0, END)
        entCpuTemp.insert(INSERT, valores[3])

        entCpuFreq.delete(0, END)
        entCpuFreq.insert(INSERT,valores[1])

        entCpuMedia.delete(0, END)
        entCpuMedia.insert(INSERT, valores[2])

        entMemoUso.delete(0, END)
        entMemoUso.insert(INSERT, valores[4])

        entMemoDisp.delete(0, END)
        entMemoDisp.insert(INSERT, valores[5])

        entMemoPorc.delete(0, END)
        entMemoPorc.insert(INSERT, valores[6])

        entMemoLivre.delete(0, END)
        entMemoLivre.insert(INSERT, valores[7])

        entFanVel.delete(0, END)
        entFanVel.insert(INSERT, valores[8])

    asyncio.run(iniciarAtt())





fonte = ("Verdana", "15")
container1 = Frame()
container1["pady"] = 10
container1.pack()
container2 = Frame()
container2["padx"] = 20
container2["pady"] = 5
container2.pack()
container3 = Frame()
container3["padx"] = 20
container3["pady"] = 5
container3.pack()
container4 = Frame()
container4["padx"] = 20
container4["pady"] = 5
container4.pack()
container5 = Frame()
container5["padx"] = 20
container5["pady"] = 5
container5.pack()
container6 = Frame()
container6["padx"] = 20
container6["pady"] = 5
container6.pack()

container7 = Frame()
container7["padx"] = 20
container7["pady"] = 5
container7.pack()
container8 = Frame()
container8["padx"] = 20
container8["pady"] = 5
container8.pack()
container9 = Frame()
container9["padx"] = 20
container9["pady"] = 5
container9.pack()
container10 = Frame()
container10["padx"] = 20
container10["pady"] = 5
container10.pack()
container11 = Frame()
container11["padx"] = 20
container11["pady"] = 5
container11.pack()

container15 = Frame()
container15["padx"] = 20
container15["pady"] = 5
container15.pack()
container16 = Frame()
container16["padx"] = 20
container16["pady"] = 10
container16.pack()
container17 = Frame()
container17["pady"] = 15
container17.pack()

titulo = Label(container1, text="Monitor de Recursos")
titulo["font"] = ("Calibri", "15", "bold")
titulo.pack ()

espaco = Label(container2, text="",
font=fonte, width=25)
espaco.pack(side=LEFT)

btnAtualizar = Button(container2, text="Atualizar",
font=fonte, width=10)
btnAtualizar["command"] = atualizar()
btnAtualizar.pack(side=RIGHT)

lbCpuTemp = Label(container3, text="CPU-Temp:",
font=fonte, width=11)
lbCpuTemp.pack(side=LEFT)

entCpuTemp = Entry(container3)
entCpuTemp["width"] = 25
entCpuTemp["font"] = fonte
entCpuTemp.pack(side=LEFT)

lbCpuFreq = Label(container4, text="CPU-Freq:",
font=fonte, width=11)
lbCpuFreq.pack(side=LEFT)

entCpuFreq = Entry(container4)
entCpuFreq["width"] = 25
entCpuFreq["font"] = fonte
entCpuFreq.pack(side=LEFT)

lbCpuMedia= Label(container5, text="CPU-Media:",
font=fonte, width=11)
lbCpuMedia.pack(side=LEFT)

entCpuMedia = Entry(container5)
entCpuMedia["width"] = 25
entCpuMedia["font"] = fonte
entCpuMedia.pack(side=LEFT)

lbCpuUso= Label(container6, text="CPU-Uso:",
font=fonte, width=11)
lbCpuUso.pack(side=LEFT)

entCpuUso = Entry(container6)
entCpuUso["width"] = 25
entCpuUso["font"] = fonte
entCpuUso.pack(side=LEFT)


lbMemoUso= Label(container7, text="Memo-Uso:",
font=fonte, width=11)
lbMemoUso.pack(side=LEFT)

entMemoUso = Entry(container7)
entMemoUso["width"] = 25
entMemoUso["font"] = fonte
entMemoUso.pack(side=LEFT)

lbMemoDisp= Label(container8, text="Memo-Disp:",
font=fonte, width=11)
lbMemoDisp.pack(side=LEFT)

entMemoDisp = Entry(container8)
entMemoDisp["width"] = 25
entMemoDisp["font"] = fonte
entMemoDisp.pack(side=LEFT)

lbMemoPorc= Label(container9, text="Memo-Porc:",
font=fonte, width=11)
lbMemoPorc.pack(side=LEFT)

entMemoPorc = Entry(container9)
entMemoPorc["width"] = 25
entMemoPorc["font"] = fonte
entMemoPorc.pack(side=LEFT)

lbMemoLivre= Label(container10, text="Memo-Livre:",
font=fonte, width=11)
lbMemoLivre.pack(side=LEFT)

entMemoLivre = Entry(container10)
entMemoLivre["width"] = 25
entMemoLivre["font"] = fonte
entMemoLivre.pack(side=LEFT)

lbFanVel= Label(container11, text="Fan-Vel:",
font=fonte, width=11)
lbFanVel.pack(side=LEFT)

entFanVel = Entry(container11)
entFanVel["width"] = 25
entFanVel["font"] = fonte
entFanVel.pack(side=LEFT)

bntInsert = Button(container16, text="",
font=fonte, width=12)
bntInsert.pack (side=LEFT)

bntAlterar = Button(container16, text="",
font=fonte, width=12)
bntAlterar.pack (side=LEFT)

bntGraficos = Button(container16, text="Graficos",
font=fonte, width=12)
bntGraficos.pack(side=LEFT)
bntGraficos["command"]= criarNovaTela

lblmsg = Label(container17, text="")
lblmsg["font"] = ("Verdana", "9", "italic")
lblmsg.pack()



def criarNovaTela(self):
    fig, ax = plt.subplots()

    def animar():
        x=[0,1,3]
        y=[20,30,50]
        ax.clear()
        ax.plot([1,2,3,4],[1,4,9,16])
        ax.set_xlabel('teste')
        

    animar()

""" newWindow = Toplevel()
labelExample = Label(newWindow, text = "Graficossss aquiii")
botgraficos = Button(newWindow, text="teste grafico", command=graficoPlot)

labelExample.pack()
botgraficos.pack() """

        
        


root = Tk()
monitor(root)
root.mainloop()