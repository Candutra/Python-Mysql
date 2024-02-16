# Conexão do Python com o Mysql

!["Imagem Python com MySQL"](https://www.learntek.org/blog/wp-content/uploads/2019/06/Mysql-python.png)

## Divre de comunicação com o mysql
Para estabelecer a comunicação entre o Python e o banco Mysql, iremos usar o seguinte drive:
<a href="https://pypi.org/project/mysql-connector-python/#history">https://pypi.org/project/mysql-connector-python/#history</a>


### Comando para instalar 
``` python
    python -m pip install mysql-connector-python
```
---
### Configuração do banco de dados Mysql
O nosso banco de dados esta em um container de docker, para acessa-lo será necessario criar o container. Então faremos os seguintes comandos em um servidor Fderoa com o docker instalado

#### Criação do volume
``` shell
mkdir dadosclientes 
```
#### Criação do container
<center>
<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNT_a8nqBIuQaGrqxrao1jngeC3Xyl-kctCw&usqp=CAU"
height="100" width="100">
<center> 

``` shell
docker run --name srv-mysql -v ~/dadosclientes:/var/lib/mysql -p 3784:3306 -e MYSQL_ROOT_PASSWORD=senac@123 -d mysql
```
### Criação banco de dados da tabela clientes
```sql 
create database banco;

use banco;

create table Clientes(
clientes_id int auto_increment primary key,
nome_clientes varchar(50) not null,
email varchar(100) not null unique,
telefone varchar(20) 
);
```

#### Arquivo clientes.py
``` python
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
```

#### Arquivos de cadastro: cad_clientes.py
```python
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
```

#### Arquivo de atualização up_clientes
``` python
import mysql.connector as mc 
cx = mc.connect(
    host="127.0.0.1",
    port="3784",
    user="root",
    password="senac@123",
    database="banco"
)
cursor = cx.cursor()
cursor.execute("Select * from Clientes")
for i in cursor:
    print(i)

print("O que você deseja atualizar, digite: ")
print("1 - Nome")
print("2 - E-mail")
print("3 - Telefone")

op = input("Digite a opção desejada: ")
id = input("Agora digite o id do cliente: ")
dado = input("Digite a nova informação: ")

if(op== "1"):
    cursor.execute("update Clientes set nome_clientes='"+dado+"' where clientes_id="+id)
elif(op== "2"):
    cursor.execute("update Clientes set email='"+dado+"' where clientes_id="+id)
elif (op== "3"):
    cursor.execute("update Clientes set telefone='"+dado+"' where clientes_id="+id)
else:
    print("Opção invalida")

cx.commit()
```