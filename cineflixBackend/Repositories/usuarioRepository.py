from Repositories.BaseRepository import BaseRepository

class usuarioRepository:
    def __init__(self):
        self.baserepository = BaseRepository()

    def getAll(self):
        query = "select * from usuarios"
        return self.baserepository.execute(query)
    
    def getById(self, id):
        query = "select * from usuarios where id = %s"
        return self.baserepository.execute(query, (id,))
    
    def create(self, data):
        commad = """
            insert  into usuarios (username, senha, email, tipo)
            values (%s, %s, %s, %s)
        """
        params = (
            data['username'],
            data['senha'],
            data['email'],
            data['tipo']
        )
        return self.baserepository.execute(commad, params)
    
    def update(self, id:int, data):
        commad = """
            update usuarios set 
                username = %s, 
                senha = %s,
                email = %s,
                tipo = %s
            where id = %s
        """
        params = (
            data["username"],
            data["senha"],
            data["email"],
            data["tipo"],
            id
        )
        return self.baserepository.execute(commad, params)
    
    def delete(self, id:int):
        command = "delete from usuarios where id = %s"
        return self.baserepository.execute(command, (id,))