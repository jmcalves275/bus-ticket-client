import requests 

class City(object):

  def __init__(self, id, name):
    self.id = id
    self.name = name

  def getID():
    return self.ID

  def getName():
    return self.name


def get_cities():
  r = requests.get('https://www.rede-expressos.pt/api/locations/origins?national=true')
  return r.json()