import psutil
import time
import mysql.connector
from threading import Thread
from datetime import datetime

#funcs  das consultas dos dados
def ultimaTemp():
    try:
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pcinfo"
            )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT cpu_temp from pcinfo3 order by data desc limit 1")
    
        resultado = mycursor.fetchall()

        print("ultima temp:", resultado[0])
        mydb.close()
    except:
        print('erro')

def quandoFrqMinMax():
    try:
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pcinfo"
            )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT data from pcinfo3 order by cpu_freq desc limit 1")
    
        resultado = mycursor.fetchall()

        print("Quando freq maxima:", resultado[0])

        mycursor.execute("SELECT data from pcinfo3 order by cpu_freq asc limit 1")
    
        resultado = mycursor.fetchall()

        print("quando freq minima:", resultado[0])

        mydb.close()
    except:
        print('erro')


    
ultimaTemp()
quandoFrqMinMax()
    
