import jwt
import datetime
import os
from src.Infrastructure.http.whats_app import generateNumber, sendMessage
from src.Infrastructure.Models.user import UsersMarketModel
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

class UsersMarketService:
    @staticmethod
    def create_usermarket(session, name, cnpj, phone, email, password):
        try:
            numberMessage = generateNumber()
            sendMessage(numberMessage)
            hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=16)
            users_market_model = UsersMarketModel(
                name=name,
                cnpj=cnpj,
                phone=phone,
                email=email,
                password=hashed_password,
                code=numberMessage
            )

            session.add(users_market_model)
            session.commit()

            return users_market_model
        except Exception as e:
            session.rollback()
            raise e

    @staticmethod
    def activate_usermarket(session, activation_code):
        user = session.query(UsersMarketModel).filter_by(code=activation_code).first()
        
        if user is None:
            raise ValueError("Código de ativação inválido.")
        
        user.is_active = True
        session.commit()
        
        return user

    @staticmethod
    def login(session, email, password):
        user = session.query(UsersMarketModel).filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):
            raise ValueError("Email ou senha incorretos")

