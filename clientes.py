# importando a biblioteca de conexão com o banco de dados mysql
#Vamos adicionar um alias a biblioteca

import mysql.connector as mc 

# vamos estabele a conexão com o banco de dados e para tal iremos passar os seguintes dados:
#servidor, porta, usuario, senha, banco 
conexao = mc.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="senac@123",
    database="banco"
)
# Estamos testando a conexão, pedindo para exibir o id da conexão. Caso exiba uma pilha de erros, então você tem um erro na linha de conexão
print(conexao)

# Para se movimenta dentro da estrutura de banco de dados e retornar os dados necessarios iremos criar um cursor
cursor = conexao.cursor()
# vamos execultar o comando usadno um cursor
# cursor.execute("Create database Ola") 

# cursor.execute("insert into clientes(nome_clientes,email,telefone)values('Aang','aang.avatar@uol','(15)96523-5412')")

# Vamos selecionar todos os dados da tabela cliente 
cursor.execute("Select * from banco.Clientes")
print(cursor)
for c in cursor: 
    print(f"Id do cliente: {c[0]}")
    print(f"Nome do cliente: {c[1]}")
    print(f"email: {c[2]}")

