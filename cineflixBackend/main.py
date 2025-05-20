from flask import Flask, request, jsonify
from flask_cors import CORS

from Controllers.usuarioController import usuarioController
from Controllers.assinaturaController import assinaturaController
UsuarioController = usuarioController()
Assinaturas = assinaturaController()

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

@api.route('/assinaturas', methods=['GET'])
def getAssinaturas():
    return Assinaturas.getAll()

@api.route('/assinaturas/<int:id>', methods=['GET'])
def getassinaturaById(id):
    return Assinaturas.getById(id)

@api.route('/assinaturas/create', methods=['POST'])
def createAssinatura():
    return Assinaturas.create()

@api.route('/assinaturas/update<int:id>', methods=['PUT'])
def updateAssinaturas(id):
    return Assinaturas.update(id)

@api.route('/assinaturas/delete<int:id>', methods=['DELETE'])
def deleteAssinaturas(id):
    return Assinaturas.delete(id)
