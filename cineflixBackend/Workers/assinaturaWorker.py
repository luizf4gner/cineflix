from Repositories.assinaturaRepository import assinaturaRepository

class assinaturaWorker:
  def __init__(self):
    self.repository = assinaturaRepository()

  def getAll(self):
    return self.repository.getAll()

  def getById(self, id):
    return self.repository.getById(id)

  def create(self, data):
    required_files = ("usuario_id", "data_inicial", "data_final")
    for field in required_files:
      if field not in data or not data[field]:
        raise ValueError(f"O campo {field} é obrigatório.")
    return self.repository.create(data)

  def update(self, data, id):
    required_files = ("usuario_id", "data_inicial", "data_final")
    for field in required_files:
      if field not in data or not data[field]:
        raise ValueError(f"O campo {field} é obrigatório.")
    return self.repository.update(data, id)

  def delete(self, id):
    return self.repository.delete(id)
