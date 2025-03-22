from src.Application.Services import usersmarket_services
from src.database import db

class UsersMarketController:
    @staticmethod
    def create_usermarket(data):
        try:
            new_user = usersmarket_services.UsersMarketService.create_usermarket(
                session=db.session,
                name=data['name'],
                cnpj=data['cnpj'],
                phone=data['phone'],
                email=data['email'],
                password=data['password']
            )
            return {
                'id': new_user.id,
                'name': new_user.name,
                'cnpj': new_user.cnpj,
                'phone': new_user.phone,
                'email': new_user.email,
                'activation_code': new_user.code
            }
        except Exception as e:
            return {'error': str(e)}

    @staticmethod
    def activate_usermarket(data):
        try:
            user = usersmarket_services.UsersMarketService.activate_usermarket(
                session=db.session,
                activation_code=data['activation_code']
            )
            return {
                'message': 'Conta ativada com sucesso!',
                'user': {
                    'id': user.id,
                    'name': user.name,
                    'email': user.email
                }
            }
        except Exception as e:
            return {'error': str(e)}

    @staticmethod
    def login(data):
        try:
            token = usersmarket_services.UsersMarketService.login(
                session=db.session,
                email=data["email"],
                password=data["password"]
            )
            return token
        except Exception as e:
            return {"error": str(e)}
