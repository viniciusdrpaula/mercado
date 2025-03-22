from flask import Blueprint
from src.Routes.main_routes import main_routes

# Criar o Blueprint geral para a aplicação
routes = Blueprint('routes', __name__)

# Registrar apenas o Blueprint principal
routes.register_blueprint(main_routes, url_prefix='/')
