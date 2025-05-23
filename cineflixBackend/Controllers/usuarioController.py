from flask import jsonify, request
from Workers.usuarioWorker import usuarioWorker

class usuarioController():
    def __init__(self):
        self.usuarioworker = usuarioWorker()

    def getAll(self):
        return jsonify(self.usuarioworker.getAll()), 200

    def getById(self, id):
        usuario = self.usuarioworker.getById(id)
        if not usuario:
            return jsonify({"erro":"usuário não encontrado"}), 404
        return jsonify(usuario), 200

    def create(self):
        data = request.get_json()
        if not data:
            return jsonify({"error":"Dados incompletos"}), 400
        try:
            self.usuarioworker.create(data)
            return jsonify({"message":"usuario criado com sucesso!"}), 201
        except Exception as e:
            return jsonify({"error":str(e)}), 500

    def update(self, id):
        data = request.get_json()
        if not data:
            return jsonify({"error":"Dados incompletos"}), 400
        try:
            self.usuarioworker.update(data, id)
            return jsonify({"message":"usuario atualizado com sucesso!"}), 200
        except Exception as e:
            return jsonify({"error":str(e)}), 500

    def delete(self, id):
        try:
            self.usuarioworker.delete(id)
            return jsonify({"message":"usuario deletado com sucesso!"}), 200
        except Exception as e:
            return jsonify({"error":str(e)}), 500