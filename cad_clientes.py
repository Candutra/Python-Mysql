import mysql.connector as mc
# estabelecer a conexão com o banco

cx = mc.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="senac@123",
    database="banco"
)
#  verificar se a conexão foi estabelecida
print(cx)

#  criação de variaveis para o usuario passar os dados do clientes para cadastrar
nome = input("Digite o nome do cliente: ")
email = input("Digite o email do cliente: ")
telefone = input("Digite o telefone do cliente: ")

cursor = cx.cursor()
cursor.execute("insert into Clientes(nome_clientes,email,telefone)values('"+nome+"','"+email+"','"+telefone+"')")
# confirmar a inserção dos dados na tabela

print(cx.commit())