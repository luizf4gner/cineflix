from Repositories.BaseRepository import BaseRepository

class recomendacaoRepository:
    def __init__(self):
        self.baserepository = BaseRepository()

    def getAll(self):
        query = """
            SELECT 
                recomendacao.id,
                usuarios.username,
                series_filmes.titulo,
                recomendacao.nota
            FROM recomendacao
            JOIN usuarios ON usuarios.id = recomendacao.id_usuario
            JOIN series_filmes ON series_filmes.id = recomendacao.id_filme
        """
        return self.baserepository.fetch(query)

    def getById(self, id):
        query = "SELECT * FROM recomendacao WHERE id = %s"
        return self.baserepository.fetch(query, (id,))

    def create(self, data):
        query = """
            INSERT INTO recomendacao (id_usuario, id_filme, nota)
            VALUES (%s, %s, %s)
        """
        params = (
            data["id_usuario"],
            data["id_filme"],
            data["nota"]
        )
        return self.baserepository.execute(query, params)

    def update(self, id, data):
        query = """
            UPDATE recomendacao
            SET id_usuario = %s, id_filme = %s, nota = %s
            WHERE id = %s
        """
        params = (
            data["id_usuario"],
            data["id_filme"],
            data["nota"],
            id
        )
        return self.baserepository.execute(query, params)

    def delete(self, id):
        query = "DELETE FROM recomendacao WHERE id = %s"
        return self.baserepository.execute(query, (id,))