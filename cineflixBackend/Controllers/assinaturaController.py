from flask import jsonify, request
from Workers.assinaturaWorker import assinaturaWorker

class assinaturaController:
  def __init__(self):
    self.worker = assinaturaWorker()

  def getAll(self):
    try:
      return jsonify(return self.worker.getAll()), 200
    except Exception as e:
      return jsonify({"error": str(e)}), 500

  def getById(self, id):
    try:
      assinatura = self.worker.getById(id)
      if not assinatura:
        return jsonify({"error":"Assinatura não encontrada."}), 404
      return jsonify(assinatura), 200
    except Exception as e:
      return jsonify({"error": str(e)}), 500

  def create(self):
    data = request.get_json()
    if not data:
      return jsonify({"error":"Dados incompletos ."}), 400
    try:
      self.worker.create(data)
      return jsonify({"message":"assinatura cadastrada com sucesso!"}), 201
    except ValueError as e:
      return jsonify({"error": str(e)}), 400
    except Exception as e:
      return jsonify("error": str(e)), 500

  def update(self, id):
    data = request.get_json()
    if not data:
      return jsonify({"error":"Dados incompletos ."}), 400
    try:
      self.worker.update(data, id)
      return jsonify({"message":"assinatura atualizada com sucesso!"}), 201
    except ValueError as e:
      return jsonify({"error": str(e)}), 400
    except Exception as e:
      return jsonify("error": str(e)), 500

  def delete(self, id):
        try:
            self.worker.delete(id)
            return jsonify({"message": "Assinatura cancelada com sucesso!"}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
