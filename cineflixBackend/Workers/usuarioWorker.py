from Repositories.usuarioRepository import usuarioRepository

class usuarioWorker():
    def __init__(self):
        self.repository = usuarioRepository()

    def getAll(self):
        return self.repository.getAll()
    
    def getById(self, id):
        return self.repository.getById(id)
    
    def create(self, data):
        required_fields = ("username", "senha", "email", "tipo")
        for field in required_fields:
            if field not in data or not data[field]:
                raise ValueError(f"O campo '{field}' é obrigatório.")
        return self.repository.create(data)
    
    def update(self, data, id):
        required_fields = ("username", "senha", "email", "tipo")
        for field in required_fields:
            if field not in data or not data[field]:
                raise ValueError(f"O campo '{field}' é obrigatório.")
        return self.repository.update(id, data)
    
    def delete(self, id):
        return self.repository.delete(id)