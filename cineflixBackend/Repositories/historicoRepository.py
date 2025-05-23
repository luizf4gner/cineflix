from Repositories.BaseRepository import BaseRepository

class historicoRepository:
    def __init__(self):
        self.baserepository = BaseRepository()

    def getAll(self):
        query = """
            SELECT 
                historico.id,
                usuarios.username,
                series_filmes.titulo,
                historico.data_visualizacao,
                historico.progresso
            FROM historico
            JOIN usuarios ON usuarios.id = historico.id_usuario
            JOIN series_filmes ON series_filmes.id = historico.id_filme
        """
        return self.baserepository.fetch(query)

    def getById(self, id):
        query = "SELECT * FROM historico WHERE id = %s"
        return self.baserepository.fetch(query, (id,))

    def create(self, data):
        query = """
            INSERT INTO historico (id_usuario, id_filme, progresso)
            VALUES (%s, %s, %s)
        """
        params = (
            data["id_usuario"],
            data["id_filme"],
            data["progresso"]
        )
        return self.baserepository.execute(query, params)

    def update(self, id, data):
        query = """
            UPDATE historico
            SET id_usuario = %s, id_filme = %s, progresso = %s
            WHERE id = %s
        """
        params = (
            data["id_usuario"],
            data["id_filme"],
            data["progresso"],
            id
        )
        return self.baserepository.execute(query, params)

    def delete(self, id):
        query = "DELETE FROM historico WHERE id = %s"
        return self.baserepository.execute(query, (id,))