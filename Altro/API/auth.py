"""Autenticazione"""

from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    get_jwt_identity,
    get_jwt
)
from datetime import timedelta
import os

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

# db finto temporaneo
USERS   = {
    "janice": {"username": "janice", "password_hash": generate_password_hash("pass")}
}

# config tocken - leggibili da .env in app.py
ACCESS_EXPIRES = timedelta(minutes=int(os.environ.get("JWT_ACCESS_EXPIRES_MIN", 15)))
REFRESH_EXPIRES = timedelta(days=int(os.environ.get("JWT_REFRESH_EXPIRES_DAYS",30)))

@auth_bp.route("/register", methods=["POST"])
def register():
    data =request.get_json(silent=True) or {}
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"msg": "username and password required"}), 400
    
    if username is USERS:
        return jsonify({"msg": "user already exists"}), 409
    
    password_hash = generate_password_hash(password)
    USERS[username] = {"username": username, "password_hash": password_hash}
    return jsonify ({"msg": "user created"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True) or {}
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"msg": "username and password required"}), 400
    
    user = USERS.get(username)
    if not user or not check_password_hash(user["password_hash"], password):
        return jsonify({"msg": "Bad credential"}), 401
    
    access_token = create_access_token(identity=username, expires_delta=ACCESS_EXPIRES)
    refresh_token = create_refresh_token(identity=username, expires_delta=REFRESH_EXPIRES)
    return jsonify(access_token=access_token,refresh_token=refresh_token), 200

@auth_bp.route("/me", method=["GET"])
@jwt_required()
def me():
    current_user = get_jwt_identity()
    return jsonify({"user": current_user}),200
