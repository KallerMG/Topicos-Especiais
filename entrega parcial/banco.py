import mysql.connector

#Conectando com o banco de dados
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pcinfo"
)

mycursor = mydb.cursor()

#criar banco de dados
#mycursor.execute("CREATE DATABASE pcinfo")


#mycursor.execute("CREATE TABLE pcinfo (id INT AUTO_INCREMENT PRIMARY KEY, data VARCHAR(255), cpu_uso VARCHAR(255), cpu_freq VARCHAR(255), cpu_media VARCHAR(255), cpu_temp VARCHAR(255), memo_uso VARCHAR(255), memo_disp VARCHAR(255), memo_porc VARCHAR(255), memo_livre VARCHAR(255), fan_vel VARCHAR(255) )")

#mycursor.execute("CREATE TABLE pcinfo2 (id INT AUTO_INCREMENT PRIMARY KEY, data timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, cpu_uso VARCHAR(255), cpu_freq VARCHAR(255), cpu_media VARCHAR(255), cpu_temp VARCHAR(255), memo_uso VARCHAR(255), memo_disp VARCHAR(255), memo_porc VARCHAR(255), memo_livre VARCHAR(255), fan_vel VARCHAR(255) )")


#Criar Tabela pcinfo3
mycursor.execute("CREATE TABLE pcinfo3 (id INT AUTO_INCREMENT PRIMARY KEY, data timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, cpu_uso DOUBLE(50,4), cpu_freq DOUBLE(50,4), cpu_media DOUBLE(50,4), cpu_temp DOUBLE(50,4), memo_uso DOUBLE(50,4), memo_disp DOUBLE(50,4), memo_porc DOUBLE(50,4), memo_livre DOUBLE(50,4), fan_vel DOUBLE(50,4) )")


mydb.commit()



