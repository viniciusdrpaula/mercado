import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

class Config:
    # Configuração do SQLAlchemy (Banco de Dados)
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "mysql+pymysql://root:password@localhost/gestao_mercado"  # Valor padrão
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configuração da chave secreta
    SECRET_KEY = os.getenv("SECRET_KEY", "sua_chave_secreta_default")
    
    # Configuração de ambiente (opcional)
    FLASK_ENV = os.getenv("FLASK_ENV", "development")

    # Configuração de debug (opcional)
    DEBUG = os.getenv("DEBUG", "True").lower() in ["true", "1"]
