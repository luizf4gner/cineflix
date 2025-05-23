from Repositories.assinaturaRepository import AssinaturaRepository
from Repositories.usuarioRepository import usuarioRepository

class assinaturaWorker:
    def __init__(self):
        self.repository = AssinaturaRepository()
        self.usuarioRepo = usuarioRepository()

    def getAll(self):
        return self.repository.getAll()

    def getById(self, id):
        return self.repository.getById(id)

    def create(self, data):
        required_fields = ("username", "data_inicial", "data_final")
        for field in required_fields:
            if field not in data or not data[field]:
                raise ValueError(f"O campo '{field}' é obrigatório.")
            
        usuarios = self.usuarioRepo.getByUsername(data["username"])
        if not usuarios:
            raise ValueError("Usuário não encontrado.")

        usuario_id = usuarios[0]["id"]
        assinatura_data = {
            "usuario_id": usuario_id,
            "data_inicial": data["data_inicial"],
            "data_final": data["data_final"]
        }

        return self.repository.create(assinatura_data)

    def update(self, id, data):
        required_fields = ("usuario_id", "data_inicial", "data_final")
        for field in required_fields:
            if field not in data or not data[field]:
                raise ValueError(f"O campo '{field}' é obrigatório.")

        usuarios = self.usuarioRepo.getByUsername(data["username"])
        if not usuarios:
            raise ValueError("Usuário não encontrado.")

        usuario_id = usuarios[0]["id"]
        assinatura_data = {
            "id_usuario": usuario_id,
            "data_inicial": data["data_inicial"],
            "data_final": data["data_final"]
        }
        return self.repository.update(id, assinatura_data)

    def delete(self, id):
        return self.repository.delete(id)