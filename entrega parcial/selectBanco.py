import psutil
import time
import mysql.connector
from threading import Thread
from datetime import datetime

#funcs  das consultas dos dados

#função retorna data e porcentagem de uso de memoria abaixo e igual 28%
def memoPorcBaixa():
    try:
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pcinfo"
            )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT data,memo_porc FROM pcinfo3 WHERE memo_porc <= 28 ORDER BY `pcinfo3`.`data` ASC")
    
        resultado = mycursor.fetchall()

        print("Pocentagens de memoria abaixo de 28%", resultado)
        mydb.close()
    except:
        print('erro')

#função retorna temp maxima e minima do cpu nos ultimos 7 dias
def ultimosDiasTemp():
    try:
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pcinfo"
            )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT cpu_temp FROM pcinfo3 WHERE data BETWEEN CURRENT_DATE()-7 AND CURRENT_DATE() ORDER BY `pcinfo3`.`cpu_temp` DESC LIMIT 1")
    
        resultado = mycursor.fetchall()

        print("Temp maxima nos ultimos 7 dias", resultado)

        mycursor.execute("SELECT cpu_temp FROM pcinfo3 WHERE data BETWEEN CURRENT_DATE()-7 AND CURRENT_DATE() ORDER BY `pcinfo3`.`cpu_temp` asc LIMIT 1")
    
        resultado = mycursor.fetchall()

        print("Temp minima nos ultimos 7 dias", resultado)

        mydb.close()
    except:
        print('erro')


#função retorna a data e o uso da cpu quando ele esta entre 10% a 90% de uso
def cpuUsoEntre():
    try:
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pcinfo"
            )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT cpu_uso,data FROM pcinfo3 WHERE cpu_uso >= 10 and cpu_uso <= 90")
    
        resultado = mycursor.fetchall()

        print("Cpu uso >= 10% 'e' <= 90:", resultado)
        mydb.close()
    except:
        print('erro')


#função retorna ultima temp do Cpu
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


#função retorna data de quando  foi a freq maxima e minima do cpu
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

        print("Quando freq mínima:", resultado[0])

        mydb.close()
    except:
        print('erro')


    
""" ultimaTemp()
quandoFrqMinMax()
cpuUsoEntre()
ultimosDiasTemp()
memoPorcBaixa()
 """