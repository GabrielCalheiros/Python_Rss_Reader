from dotenv import dotenv_values
from datetime import timedelta

# Obtem o arquivo .env e armazena suas variáveis em um dicionário
config = dotenv_values(".env")

# Classe usada para armazenar os parâmetros de configuração da aplicação.
class Config:
    """
    Classe usada para armazenar os parâmetros de configuração da aplicação.
    
    - SECRET_KEY: Usada para proteger os dados da sessão e deve ser mantida em segredo.
    - SQLALCHEMY_DATABASE_URI: Especifica a string de conexão do banco de dados. 
    - SQLALCHEMY_TRACK_MODIFICATIONS: Usada para habilitar/desabilitar o rastreamento 
      automático de alterações em objetos ORM do SQLAlchemy. Esta opção é definida 
      como `False` por padrão para melhorar o desempenho.
    """

    SECRET_KEY = config['SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = config['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
