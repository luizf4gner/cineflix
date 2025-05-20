from Repositories.BaseRepository import BaseRepository

class assinaturaReposiory():
  def __init__(self):
    self.baseRepository = BaseRepository()

  def getAll(self):
    query = "select * from assinaturas"
    return self.baseRepository.fetch(query)

  def getById(self, id):
    query = "select * from assinaturas where id = %s"
    return self.baseRepository.fetch(query, (id))
