import psutil
import time
import mysql.connector
from threading import Thread
from datetime import datetime

#tempo do funcionamento em segundos
tempo_de_Espera = 300 

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



def iniciarColeta(tempo):
    while True:
        try:

            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pcinfo"
            )

            mycursor = mydb.cursor()

            cpu_uso = cpuUsoKaller()
            cpu_freq = cpuFreqKaller()
            cpu_media = cpuMediaKaller()
            cpu_temp = cpuTempKaller()
            memo_uso = memoUsoKaler()
            memo_disp = memoDispKaller()
            memo_porc = memoPorcentKaller()
            memo_livre = memoLivreKaller()
            fan_vel = fanVelKaller()    


            #Data de agora
            #data_atual = datetime.now()
            #data_atual_certa = data_atual.strftime('%d/%m/%Y %H:%M')

            #salvar os dados no arquivo
            #salvar = (data_atual_certa +"\n"+ cpu_uso +"\n"+ cpu_freq +"\n"+ cpu_media +"\n"+ cpu_temp +"\n"+ memo_uso +"\n"+ memo_disp +"\n"+ memo_porc +"\n"+ memo_livre +"\n"+ fan_vel + "\n" +"\n")

            #arquivo = open('dados.txt','a+')
            #arquivo.writelines(salvar)
            #arquivo.close()

            #sql = "INSERT INTO pcinfo (data, cpu_uso, cpu_freq, cpu_media, cpu_temp, memo_uso, memo_disp, memo_porc, memo_livre, fan_vel) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            #val = (data_atual_certa, cpu_uso, cpu_freq, cpu_media, cpu_temp, memo_uso, memo_disp, memo_porc, memo_livre, fan_vel)

            sql = "INSERT INTO pcinfo3 ( cpu_uso, cpu_freq, cpu_media, cpu_temp, memo_uso, memo_disp, memo_porc, memo_livre, fan_vel) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = ( cpu_uso, cpu_freq, cpu_media, cpu_temp, memo_uso, memo_disp, memo_porc, memo_livre, fan_vel)

            
            mycursor.execute(sql, val)

            mydb.commit()
            print("Dado foi inserido no banco")
            mydb.disconnect()
        except:
            print("Ops, deu erro em algo")

        time.sleep(tempo)

t = Thread(iniciarColeta(tempo_de_Espera))
t.start()
