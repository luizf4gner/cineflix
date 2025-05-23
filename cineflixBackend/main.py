from flask import Flask, request, jsonify
from flask_cors import CORS

from Controllers.usuarioController import usuarioController
from Controllers.assinaturaController import AssinaturaController
from Controllers.historicoController import historicoController
from Controllers.recomendacaoController import recomendacaoController
UsuarioController = usuarioController()
Assinaturas = AssinaturaController()
historico = historicoController()
recomendacao = recomendacaoController()

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

@api.route('/historico', methods=['GET'])
def getHistorico():
    return Assinaturas.getAll()

@api.route('/historico/<int:id>', methods=['GET'])
def gethistoricoById(id):
    return historico.getById(id)

@api.route('/historico/create', methods=['POST'])
def createhistorico():
    return historico.create()

@api.route('/historico/update<int:id>', methods=['PUT'])
def updatehistorico(id):
    return historico.update(id)

@api.route('/historico/delete<int:id>', methods=['DELETE'])
def deletehistorico(id):
    return historico.delete(id)

@api.route('/recomendacao', methods=['GET'])
def getRecomendacao():
    return recomendacao.getAll()

@api.route('/recomendacao/<int:id>', methods=['GET'])
def getRecomendacaoById(id):
    return recomendacao.getById(id)

@api.route('/recomendacao/create', methods=['POST'])
def createRecomendacao():
    return recomendacao.create()

@api.route('/recomendacao/update<int:id>', methods=['PUT'])
def updateRecomendacao(id):
    return recomendacao.update(id)

@api.route('/recomendacao/delete<int:id>', methods=['DELETE'])
def deleteRecomendacao(id):
    return recomendacao.delete(id)