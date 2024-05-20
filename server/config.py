from datetime import timedelta
from dotenv import load_dotenv
from models.databaseconfig import db
load_dotenv()

class ApplicationConfig:
    SECRET_KEY = 'dfsadfdtddasxfta'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_ECHO = True
    # postgresql://postgres:DWJNNRBfzxviIeroiZkubofqvDueDhUy@viaduct.proxy.rlwy.net:21766/railway
    SQLALCHEMY_DATABASE_URI = r"sqlite:///./app.sqlite" #'postgresql://postgres:DWJNNRBfzxviIeroiZkubofqvDueDhUy@viaduct.proxy.rlwy.net:21766/railway' #

    SESSION_TYPE = "sqlalchemy"
    SESSION_SQLALCHEMY = db
    SESSION_PERMANENT = True
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=60)
    SESSION_USE_SIGNER = True