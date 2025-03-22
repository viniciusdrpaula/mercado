from flask import Flask
from src.database import db, migrate
from src.config import Config  # Configuração para MySQL

def create_app():
    app = Flask(__name__)
    
    # Carregar as configurações do arquivo Config
    app.config.from_object(Config)

    # Inicializar as extensões do banco de dados
    db.init_app(app)
    migrate.init_app(app, db)

    # Registrar rotas
    from src.Routes.main_routes import main_routes
    app.register_blueprint(main_routes)

    return app
