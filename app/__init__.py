"""
    Cria a instância da aplicação Flask e configura as extensões.
"""

from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Inicializando as extensões
db = SQLAlchemy()

def create_app(config_class=Config):
    # Criando a instância da aplicação Flask
    """
    Cria a instância da aplicação Flask e configura as extensões.

    Se não for especificado, o parâmetro config_class é setado como a classe de configuração padrão.

    :param config_class: A classe que contém as configurações da aplicação
    :type config_class: class
    :return: A instância da aplicação Flask configurada
    :rtype: Flask
    """

    app = Flask(__name__)

    # Configurando a aplicação
    app.config.from_object(config_class)

    # Inicializando as extensões
    from app.routes import main as main_blueprint # pylint: disable=import-outside-toplevel
    db.init_app(app)

    # Registrando o blueprint
    app.register_blueprint(main_blueprint)

    return app

# Criando a instância da aplicação Flask
application = create_app()  # Renamed from 'app' to 'application'
