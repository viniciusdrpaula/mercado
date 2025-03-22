import pymysql

# Criando a conexão com o banco de dados
connection = pymysql.connect(
    host='localhost',
    user='usuario',
    password='senha',
    database='nome_do_banco'
)

# Exemplo de consulta
cursor = connection.cursor()
cursor.execute("SELECT * FROM tabela_exemplo")
resultados = cursor.fetchall()

for linha in resultados:
    print(linha)

# Encerrando a conexão
cursor.close()
connection.close()
