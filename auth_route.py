# routes/user_routes.py

from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models import db, User
import bcrypt

user_bp = Blueprint('user', __name__)

@user_bp.route('/api/register', methods=['POST'])
def register_user():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    existing_user = User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"message": "Email is already registered"}), 409

    new_user = User(email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Registration successful!"}), 201

@user_bp.route('/api/login', methods=['POST'])
def login_user():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400

    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"message": "User not found"}), 404

    if not bcrypt.checkpw(password.encode('utf-8'), user.password):
        return jsonify({"message": "Incorrect password"}), 401

    access_token = create_access_token(identity={"email": user.email, "role": user.role})
    return jsonify({
        "message": "Login successful!",
        "access_token": access_token
    })
