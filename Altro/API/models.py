"""MODELS"""

#Modelli e helper per persistenza usando Flask.SQLAlchemy

from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

#-------------
#istanza db da inizializzare in app.py
#------------------
#

db = SQLAlchemy()

#modello user

class User(db.Model):
    __tablename__ = "users"

    #colonne db
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(150), unique=True, nullable= False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # Metodo helper per importare psw hash
    def set_password(self, password: str):
        #generate_password_hash usa un salt e un algoritmo sicuro
        self.password_hash = generate_password_hash(password)

    # Metodo helper per verificare la password
    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)
    
    # Rappresentazione utile per debug
    def __repr__(self):
        return f"<User id={self.id} username={self.username}"
    
    #Repository / helper function

    def get_user_by_username(username: str):
        """Restituisce l'istanza User o None.
           Usare questa funzione invece di User.query direttamente per isolare l'accesso ai dati.
        """
        return User.query.filter_by(username=username).first()
    
    def create_uses(username: str, password: str):
        """
         Crea e persiste un nuovo utente.
         Solleva eccezione se l'username esiste già (gestire l'errore nel caller).
        """
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user
    
    #utility per inizializzare db in sviluppo

    def init_db(app):
        """
        Crea le tabelle nel DB. Usare solo in sviluppo o test.
        In produzione usare migrazioni (Flask-Migrate / Alembic).
        """    
        with app.app.context():
            db.create_all()
    