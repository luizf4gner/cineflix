from Repositories.BaseRepository import BaseRepository

class AssinaturaRepository:
    def __init__(self):
        self.baserepository = BaseRepository()

    def getAll(self):
        query = """
            SELECT 
                assinaturas.id,
                usuarios.username,
                assinaturas.data_inicial,
                assinaturas.data_final
            FROM assinaturas
            JOIN usuarios ON usuarios.id = assinaturas.id_usuario
        """
        return self.baserepository.fetch(query)

    def getById(self, id):
        query = "SELECT * FROM assinaturas WHERE id = %s"
        return self.baserepository.fetch(query, (id,))

    def create(self, data):
        query = """
            INSERT INTO assinaturas (id_usuario, data_inicial, data_final)
            VALUES (%s, %s, %s)
        """
        params = (
            data["id_usuario"],
            data["data_inicial"],
            data["data_final"]
        )
        return self.baserepository.execute(query, params)

    def update(self, id, data):
        query = """
            UPDATE assinaturas
            SET id_usuario = %s, data_inicial = %s, data_final = %s
            WHERE id = %s
        """
        params = (
            data["id_usuario"],
            data["data_inicial"],
            data["data_final"],
            id
        )
        return self.baserepository.execute(query, params)

    def delete(self, id):
        query = "DELETE FROM assinaturas WHERE id = %s"
        return self.baserepository.execute(query, (id,))