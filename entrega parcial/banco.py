import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pcinfo"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE pcinfo")


#mycursor.execute("CREATE TABLE pcinfo (id INT AUTO_INCREMENT PRIMARY KEY, data VARCHAR(255), cpu_uso VARCHAR(255), cpu_freq VARCHAR(255), cpu_media VARCHAR(255), cpu_temp VARCHAR(255), memo_uso VARCHAR(255), memo_disp VARCHAR(255), memo_porc VARCHAR(255), memo_livre VARCHAR(255), fan_vel VARCHAR(255) )")

sql = "INSERT INTO pcinfo (data, cpu_uso, cpu_freq, cpu_media, cpu_temp, memo_uso, memo_disp, memo_porc, memo_livre, fan_vel) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

#CREATE TABLE actor_backup (
#    actor_id smallint ,
#    first_name varchar(45) NOT NULL,
#    last_name varchar(45) NOT NULL,
#    last_update timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)

mydb.commit()

print(mycursor.rowcount, "record inserted.")


