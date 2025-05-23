from flask import jsonify, request
from Workers.recomendacaoWorker import recomendacaoWorker

class recomendacaoController:
    def __init__(self):
        self.worker = recomendacaoWorker()

    def getAll(self):
        try:
            return jsonify(self.worker.getAll()), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def getById(self, id):
        try:
            recomendacao = self.worker.getById(id)
            if not recomendacao:
                return jsonify({"error": "Recomendação não encontrada"}), 404
            return jsonify(recomendacao), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def create(self):
        data = request.get_json()
        if not data:
            return jsonify({"error": "Dados incompletos"}), 400
        try:
            self.worker.create(data)
            return jsonify({"message": "Recomendação registrada com sucesso!"}), 201
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
            return jsonify({"message": "Recomendação atualizada com sucesso!"}), 200
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    def delete(self, id):
        try:
            self.worker.delete(id)
            return jsonify({"message": "Recomendação deletada com sucesso!"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500