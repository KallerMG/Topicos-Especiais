import psutil
import time
import mysql.connector
from threading import Thread
from datetime import datetime

#tempo do funcionamento em segundos
tempo_de_Espera = 10

def cpu_uso_kaller():
    porcentagem = psutil.cpu_percent(1)
    retorno = "Uso da CPU: " + str(porcentagem) + "%"
    print(retorno)
    return retorno


def cpu_freq_kaller():
    freq = psutil.cpu_freq()
    retorno = "Frequencia da CPU: " + str(round(freq.current,2)) + " MHz"
    print(retorno)
    return retorno

def cpu_temp_kaller():
    try:
        temp = psutil.sensors_temperatures(fahrenheit=False)
        temp_2 = temp['coretemp']
        retorno = "Temp CPU: " + str(temp_2[0].current) +"ºC"
        print(retorno)
        return retorno
    except:
        print("bizonho")

def cpu_media_kaller():
    media = psutil.getloadavg()
    retorno = "Media 1 min: " + str(media[0]) +"% " + "Media 5 min: " + str(media[1]) +"% " + "Media 15 min: " + str(media[2]) + "%" 
    print(retorno)
    return retorno

def memo_uso_kaller():
    uso = psutil.virtual_memory()
    retorno = "Memoria Usada: " + str(uso.used) + " bytes"
    print(retorno)
    return retorno

def memo_dispo_kaller():
    uso = psutil.virtual_memory()
    retorno = "Memoria Disponivel: " + str(uso.available) + " bytes"
    print(retorno)
    return retorno

def memo_livre_kaller():
    uso = psutil.virtual_memory()
    retorno = "Memoria Livre: " + str(uso.free) + " bytes"
    print(retorno)
    return retorno

def memo_porcen_kaller():
    porce =psutil.virtual_memory()
    retorno = "Memoria Porcentagem Utilizada: " + str(porce.percent) + "%"
    print(retorno)
    return retorno

def fan_vel_kaller():
    vel = psutil.sensors_fans()
    vel_2 = vel['dell_smm']
    retorno = "Velocidade Fan: " + str(vel_2[0].current) +" RPM"
    print(retorno)
    return retorno



def iniciar_coleta(tempo):
    while True:
        try:

            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="pcinfo"
            )

            mycursor = mydb.cursor()

            cpu_uso = cpu_uso_kaller()
            cpu_freq = cpu_freq_kaller()
            cpu_media = cpu_media_kaller()
            cpu_temp = cpu_temp_kaller()
            memo_uso = memo_uso_kaller()
            memo_disp = memo_dispo_kaller()
            memo_porc = memo_porcen_kaller()
            memo_livre = memo_livre_kaller()
            fan_vel = fan_vel_kaller()    


            #Data de agora
            data_atual = datetime.now()
            data_atual_certa = data_atual.strftime('%d/%m/%Y %H:%M')

            #salvar os dados no arquivo
            salvar = (data_atual_certa +"\n"+ cpu_uso +"\n"+ cpu_freq +"\n"+ cpu_media +"\n"+ cpu_temp +"\n"+ memo_uso +"\n"+ memo_disp +"\n"+ memo_porc +"\n"+ memo_livre +"\n"+ fan_vel + "\n" +"\n")

            #arquivo = open('dados.txt','a+')
            #arquivo.writelines(salvar)
            #arquivo.close()

            sql = "INSERT INTO pcinfo (data, cpu_uso, cpu_freq, cpu_media, cpu_temp, memo_uso, memo_disp, memo_porc, memo_livre, fan_vel) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (data_atual_certa, cpu_uso, cpu_freq, cpu_media, cpu_temp, memo_uso, memo_disp, memo_porc, memo_livre, fan_vel)
            mycursor.execute(sql, val)

            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
            mydb.disconnect()
        except:
            print("erro em algo")

        time.sleep(tempo)

t = Thread(iniciar_coleta(tempo_de_Espera))
t.start()
