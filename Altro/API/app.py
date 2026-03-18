""" API """

from flask import Flask, jsonify, request
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from auth import auth_bp
import os

app = Flask(__name__)

#serve a caicare variabili da .env ma solo in develop
load_dotenv()

app.register_blueprint(auth_bp)

#configuro JWT
app.config["JWT_SECRET_KEY"] = os.environ.get("JWT_SECRET_KEY")
if not app.config["JWT_SECRET_KEY"]:
    raise RuntimeError("JWT_SECRET_KEY non impostata. Aggiungila nel file .env")

jwt = JWTManager(app)

#finto db

USERS = {
    "janice": {"username": "janice", "password": "pass"}
}

@app.post("/auth/login")
def login():
    data = request.get_json(silent = True)
    if not data:
        return jsonify({"msg": "Missing JSON body"}), 400
    
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"msg": "username and password required"}), 400
    
    user = USERS.get(username)
    if not user or user["password"] != password:
        return jsonify({"msg": "Bad credential"}), 401
    
    token = create_access_token(identity=username)
    return jsonify(access_token = token), 200

@app.get("/me")
@jwt_required()
def me():
    current_user = get_jwt_identity()
    return jsonify({"user": current_user}), 200

@app.get("/ping")
def ping():
    return jsonify({"msg": "pong"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)