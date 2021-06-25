import psutil
import time
import mysql.connector
from threading import Thread
from datetime import datetime

#funcs  das consultas dos dados

#função retorna data e porcentagem de uso de memoria abaixo e igual 28%
def memoPorcBaixa(numero):
    try:
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pcinfo"
            )
        mycursor = mydb.cursor()
        select = "SELECT data,memo_porc FROM pcinfo3 WHERE memo_porc <= " + numero + " ORDER BY `pcinfo3`.`data` ASC"
       
        mycursor.execute(select)
    
        resultado = mycursor.fetchall()
        mydb.close()

        palavras = []

        for val in resultado:
            palavras.append({'name': str(val[0]) ,'Memoria_Porc' : val[1]})

        return palavras
    except:
        print('erro')


def cpuUsoDias(numero):
    try:
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pcinfo"
            )
        mycursor = mydb.cursor()
        select = "SELECT data,cpu_uso FROM pcinfo3 WHERE cpu_uso <= " + numero + " ORDER BY `pcinfo3`.`data` ASC"
       
        mycursor.execute(select)
    
        resultado = mycursor.fetchall()
        mydb.close()

        palavras = []

        for val in resultado:
            palavras.append({'name': str(val[0]) ,'CPU_Uso' : val[1]})

        return palavras
    except:
        print('erro')

def cpuFreqDias(numero):
    try:
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pcinfo"
            )
        mycursor = mydb.cursor()
        select = "SELECT data,cpu_freq FROM pcinfo3 WHERE cpu_freq <= " + numero + " ORDER BY `pcinfo3`.`data` ASC"
       
        mycursor.execute(select)
    
        resultado = mycursor.fetchall()
        mydb.close()

        palavras = []

        for val in resultado:
            palavras.append({'name': str(val[0]) ,'CPU_Freq' : val[1]})

        return palavras
    except:
        print('erro')

def cpuTempDias(numero):
    try:
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pcinfo"
            )
        mycursor = mydb.cursor()
        select = "SELECT data,cpu_temp FROM pcinfo3 WHERE cpu_temp <= " + numero + " ORDER BY `pcinfo3`.`data` ASC"
       
        mycursor.execute(select)
    
        resultado = mycursor.fetchall()
        mydb.close()

        palavras = []

        for val in resultado:
            palavras.append({'name': str(val[0]) ,'CPU_Temp' : val[1]})

        return palavras
    except:
        print('erro')


def ultimosDias(numero):
    try:
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pcinfo"
            )

        
        select = "SELECT `data`, `cpu_uso`, `cpu_freq`, `cpu_media`, `cpu_temp`, `memo_uso`, `memo_disp`, `memo_porc`, `memo_livre` FROM `pcinfo3` WHERE data BETWEEN CURRENT_DATE()-"+ numero + " AND CURRENT_DATE() ORDER BY `pcinfo3`.`data` ASC"

        mycursor = mydb.cursor()
        mycursor.execute(select)
    
        resultado = mycursor.fetchall()
        mydb.close()

        print(resultado)

        palavras = []

    
        for val in resultado:
            palavras.append({'name': str(val[0]) ,'CPU_Uso' : val[1], 'CPU_Freq': val[2], 'CPU_Media': val[3], 'CPU_Temp': val[4], 'Memoria_Uso' :val[5], 'Memoria_Disp' :val[6], 'Memoria_Porc' : val[7], 'Memoria_Livre': val[8] })

        return palavras
      
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




