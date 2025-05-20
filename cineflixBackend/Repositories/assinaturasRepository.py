from Repositories.BaseRepository import BaseRepository

class assinaturaReposiory():
  def __init__(self):
    self.baseRepository = BaseRepository()

  def getAll(self):
    query = "select * from assinaturas"
    return self.baseRepository.fetch(query)

  def getById(self, id):
    query = "select * from assinaturas where id = %s"
    return self.baseRepository.fetch(query, (id,))

  def create(self):
    query = """
        insert into assinaturas 
        set usuario_id = %s, data_inicial = %s, data_final = %s
        where id = %s
    """
    params = (
      data["usuario_id"],
      data["data_inicial"],
      data["data_final"],
      id
    )
    return self.baseRepository.execute(query, params)

  def update(self, data, id):
    query = """
        update assinaturas (usuario_id, data_inicial, data_final)
        values (%s, %s, %s)
    """
    params = (
      data["usuario_id"],
      data["data_inicial"],
      data["data_final"]
    )
    return self.baseRepository.execute(query, params)

  def delete(self, id):
    query = "delete from assinaturas where id = %s"
    return self.baseRepository.execute(query, (id,))
