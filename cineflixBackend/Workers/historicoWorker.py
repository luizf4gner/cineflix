from Repositories.historicoRepository import historicoRepository
from Repositories.usuarioRepository import usuarioRepository

class historicoWorker:
    def __init__(self):
        self.repository = historicoRepository()
        self.usuarioRepo = usuarioRepository()

    def getAll(self):
        return self.repository.getAll()

    def getById(self, id):
        return self.repository.getById(id)

    def create(self, data):
        required = ("username", "id_filme", "progresso")
        for campo in required:
            if campo not in data or not data[campo]:
                raise ValueError(f"O campo '{campo}' é obrigatório.")

        usuario = self.usuarioRepo.getByUsername(data["username"])
        if not usuario:
            raise ValueError("Usuário não encontrado.")

        id_usuario = usuario[0]["id"]
        dados = {
            "id_usuario": id_usuario,
            "id_filme": data["id_filme"],
            "progresso": data["progresso"]
        }
        return self.repository.create(dados)

    def update(self, id, data):
        return self.create({**data, "id": id}) if "username" in data else self.repository.update(id, data)

    def delete(self, id):
        return self.repository.delete(id)