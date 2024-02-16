import mysql.connector as mc 
import os
con = mc.connect(
    host = "127.0.0.1",
    port = "3784",
    user = "root",
    password = "senac@123",
    database = "banco"
)

os.system("cls")

cursor = con.cursor()
cursor.execute("select * from Clientes")
for c in cursor:
    print(c)

id = input("Digite o id do cliente que deseja apagar: ")
rs = input("Você realmente deseja apagar esse cliente, digite (s ou n):")
if(rs=="s" or rs=="S"):
    cursor.execute("delete from Clientes where clientes_id="+id)
    con.commit()
else:
    print("-----------A operação foi cancelada--------------")