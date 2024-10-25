from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

from .jobs import start_scheduler, shutdown_scheduler  # Import the functions from jobs.py

# Inicializando as extensões
db = SQLAlchemy()

def create_app(config_class=Config):
    # Criando a instância da aplicação Flask
    app = Flask(__name__)
    
    # Configurando a aplicação
    app.config.from_object(config_class)
    
    # Inicializando as extensões
    db.init_app(app)
    
    # Registrando o blueprint
    from app.routes import main as main_blueprint  # Importando blueprint aqui para evitar importação circular
    app.register_blueprint(main_blueprint)
    
    return app

# Criando a instância da aplicação Flask
app = create_app()
