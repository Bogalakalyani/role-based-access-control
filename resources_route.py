from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import db, User

resources_bp = Blueprint('admin', __name__)

@resources_bp.route('/api/admin/resources', methods=['GET'])
@jwt_required()
def get_admin_resources():
    identity = get_jwt_identity()
    user_email = identity.get("email")

    user = User.query.filter_by(email=user_email).first()
    if not user:
        return jsonify({"message": "User not found!"}), 404
    if user.role != "admin":
        return jsonify({"message": "Access denied. Admins only!"}), 403
    admin_resources = [
        {"id": 1, "name": "Admin Report 1"},
        {"id": 2, "name": "Admin Settings"},
    ]
    return jsonify({
        "message": "Admin Resources",
        "resources": admin_resources,
        "user": {"email": user.email, "role": user.role}
    })

@resources_bp.route('/api/user/resources', methods=['GET'])
@jwt_required()
def get_user_resources():
    identity = get_jwt_identity()
    user_email = identity.get("email")
    user = User.query.filter_by(email=user_email).first()
    if not user:
        return jsonify({"message": "User not found!"}), 404
    if user.role != "user":
        return jsonify({"message": "Access denied. Users only!"}), 403
    user_resources = [
        {"id": 1, "name": "User Dashboard"},
        {"id": 2, "name": "Profile Settings"},
    ]
    return jsonify({
        "message": "User Resources",
        "resources": user_resources,
        "user": {"email": user.email, "role": user.role}
    })
