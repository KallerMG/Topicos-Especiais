import psutil
import time
import mysql.connector
from threading import Thread
from datetime import datetime
from datetime import date

#tempo do funcionamento em segundos
tempo_de_Espera = 360 

#funcs encapsuladas para as coleta de dados
def cpuUsoKaller():
    porcentagem = psutil.cpu_percent(1)
    retorno = porcentagem
    return retorno


def cpuFreqKaller():
    freq = psutil.cpu_freq()
    retorno =  freq.current
    return retorno

def cpuTempKaller():
    try:
        temp = psutil.sensors_temperatures(fahrenheit=False)
        temp_2 = temp['coretemp']
        retorno = temp_2[0].current
        return retorno
    except:
        print("bizonho")

def cpuMediaKaller():
    media = psutil.getloadavg()
    retorno = media[1]  # + str(media[1]) +", " +  str(media[2])  
    return retorno

def memoUsoKaler():
    uso = psutil.virtual_memory()
    retorno =  uso.used
    return retorno

def memoDispKaller():
    uso = psutil.virtual_memory()
    retorno = uso.available
    return retorno

def memoLivreKaller():
    uso = psutil.virtual_memory()
    retorno = uso.free
    return retorno

def memoPorcentKaller():
    porce =psutil.virtual_memory()
    retorno = porce.percent
    return retorno

def fanVelKaller():
    vel = psutil.sensors_fans()
    vel_2 = vel['dell_smm']
    retorno = vel_2[0].current
    return retorno


#func principal que vai iniciar a coleta de dados
def iniciarColeta(tempo):
    #ciclo infinito
    while True:
        try:
            #Conenctando com o banco de dados
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pcinfo"
            )

            mycursor = mydb.cursor()
            
            #Salvando dados das funcs em variaveis 
            cpu_uso = cpuUsoKaller()
            cpu_freq = cpuFreqKaller()
            cpu_media = cpuMediaKaller()
            cpu_temp = cpuTempKaller()
            memo_uso = memoUsoKaler()
            memo_disp = memoDispKaller()
            memo_porc = memoPorcentKaller()
            memo_livre = memoLivreKaller()
            fan_vel = fanVelKaller()    

            #inserindo valores no banco de dados
            sql = "INSERT INTO pcinfo3 ( cpu_uso, cpu_freq, cpu_media, cpu_temp, memo_uso, memo_disp, memo_porc, memo_livre, fan_vel) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = ( cpu_uso, cpu_freq, cpu_media, cpu_temp, memo_uso, memo_disp, memo_porc, memo_livre, fan_vel)

            mycursor.execute(sql, val)

            mydb.commit()
            print("Dado foi inserido no banco")
            mydb.disconnect()
        except:
            print("Ops, deu erro em algo")

        time.sleep(tempo)


#func teste implementação

def iniciarColetaInterface(tempo):
    #ciclo infinito
    while True:
        try:
            #Salvando dados das funcs em variaveis 
            cpu_uso = cpuUsoKaller()
            cpu_freq = cpuFreqKaller()
            cpu_media = cpuMediaKaller()
            cpu_temp = cpuTempKaller()
            memo_uso = memoUsoKaler()
            memo_disp = memoDispKaller()
            memo_porc = memoPorcentKaller()
            memo_livre = memoLivreKaller()
            fan_vel = fanVelKaller()    

            val = ( cpu_uso, cpu_freq, cpu_media, cpu_temp, memo_uso, memo_disp, memo_porc, memo_livre, fan_vel)

            
        except:
            print("Ops, deu erro em algo")

        return val
        time.sleep(tempo)

def coletasDadosAtual():
    try:
        #Salvando dados das funcs em variaveis 
        cpu_uso = cpuUsoKaller()
        cpu_freq = cpuFreqKaller()
        cpu_media = cpuMediaKaller()
        cpu_temp = cpuTempKaller()
        memo_uso = memoUsoKaler()
        memo_disp = memoDispKaller()
        memo_porc = memoPorcentKaller()
        memo_livre = memoLivreKaller()
        fan_vel = fanVelKaller()    

        val = ( cpu_uso, cpu_freq, cpu_media, cpu_temp, memo_uso, memo_disp, memo_porc, memo_livre, fan_vel)

            
    except:
        print("Ops, deu erro em algo")
            
    return val



#definindo a Thread da func principal
#t = Thread(iniciarColeta(tempo_de_Espera))
#Iniciando a Thread
#t.start()
