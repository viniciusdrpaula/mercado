from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pymysql

# Inicializar SQLAlchemy e Migrate
db = SQLAlchemy()
migrate = Migrate()

# Método opcional para conexão direta ao MySQL
def get_mysql_connection():
    return pymysql.connect(
        host='localhost',
        user='usuario',
        password='senha',
        database='nome_do_banco'
    )
