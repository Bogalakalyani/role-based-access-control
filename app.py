from flask import Flask
from config import Config
from models import db
from auth_route import user_bp
from resources_route import resources_bp
from db import init_db
from flask_cors import CORS
from flask_jwt_extended import JWTManager  

app = Flask(__name__)
app.config.from_object(Config)

db = init_db(app)

jwt = JWTManager(app)
CORS(app)

app.register_blueprint(user_bp)
app.register_blueprint(resources_bp)

if __name__ == "__main__":
    app.run(debug=True)
