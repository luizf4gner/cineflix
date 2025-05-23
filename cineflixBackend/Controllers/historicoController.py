from flask import jsonify, request
from Workers.historicoWorker import historicoWorker

class historicoController:
    def __init__(self):
        self.worker = historicoWorker()

    def getAll(self):
        try:
            return jsonify(self.worker.getAll()), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def getById(self, id):
        try:
            historico = self.worker.getById(id)
            if not historico:
                return jsonify({"error": "Histórico não encontrado"}), 404
            return jsonify(historico), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def create(self):
        data = request.get_json()
        if not data:
            return jsonify({"error": "Dados incompletos"}), 400
        try:
            self.worker.create(data)
            return jsonify({"message": "Histórico registrado com sucesso!"}), 201
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def update(self, id):
        data = request.get_json()
        if not data:
            return jsonify({"error": "Dados incompletos"}), 400
        try:
            self.worker.update(id, data)
            return jsonify({"message": "Histórico atualizado com sucesso!"}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def delete(self, id):
        try:
            self.worker.delete(id)
            return jsonify({"message": "Histórico deletado com sucesso!"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500