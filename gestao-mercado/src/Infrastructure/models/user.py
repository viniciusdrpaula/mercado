from src.database import db

class UsersMarketModel(db.Model):
    __tablename__ = "sellers"  # Nome da tabela no banco de dados

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(20), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    code = db.Column(db.String(6), nullable=False)  # Código de ativação
    is_active = db.Column(db.Boolean, default=False)

    def __init__(self, name, cnpj, phone, email, password, code, is_active=False):
        self.name = name
        self.cnpj = cnpj
        self.phone = phone
        self.email = email
        self.password = password
        self.code = code
        self.is_active = is_active

    def to_json(self):
        """
        Converte o modelo para um dicionário JSON, omitindo informações sensíveis.
        """
        return {
            "id": self.id,
            "name": self.name,
            "cnpj": self.cnpj,
            "phone": self.phone,
            "email": self.email,
            "is_active": self.is_active
        }