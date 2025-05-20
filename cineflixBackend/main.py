from flask import Flask, request, jsonify
from flask_cors import CORS

from Controllers.usuarioController import usuarioController
UsuarioController = usuarioController()

api = Flask(__name__)
CORS(api)

@api.route('/usuarios', methods=['GET'])
def getUsuarios():
    return UsuarioController.getAll()

@api.route('/usuarios/<int:id>', methods=['GET'])
def getUsuariosById(id):
    return UsuarioController.getById(id)

@api.route('/usuarios/create', methods=['POST'])
def createUsuario():
    return UsuarioController.create()

@api.route('/usuarios/update<int:id>', methods=['PUT'])
def updateUsuario(id):
    return UsuarioController.update(id)

@api.route('/usuarios/delete<int:id>', methods=['DELETE'])
def deleteUsuario(id):
    return UsuarioController.delete(id)