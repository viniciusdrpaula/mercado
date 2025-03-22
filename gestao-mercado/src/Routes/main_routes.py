from flask import Blueprint, jsonify, request
from src.Application.Controllers.usersmarket_controller import UsersMarketController

# Criar o Blueprint principal
main_routes = Blueprint('main', __name__)

# Rota inicial para testar a API
@main_routes.route('/')
def index():
    return jsonify({"message": "API funcionando!"})

# Rota para criar um novo usuário (Seller)
@main_routes.route('/api/sellers', methods=['POST'])
def create_usersmarket():
    data = request.json
    try:
        new_user = UsersMarketController.create_usermarket(data)
        return jsonify(new_user), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Rota para ativar a conta de um usuário
@main_routes.route('/api/activate', methods=['POST'])
def activate_usersmarket():
    data = request.json
    try:
        response = UsersMarketController.activate_usermarket(data)
        if 'error' in response:
            return jsonify(response), 400
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Rota para login de usuários
@main_routes.route('/api/login', methods=['POST'])
def login():
    data = request.json
    try:
        result = UsersMarketController.login(data)
        if 'error' in result:
            return jsonify(result), 400
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
