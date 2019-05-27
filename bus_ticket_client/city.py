import requests 

class City(object):
  def __init__(self, id, name):
    self.id = id
    self.name = name

  def getID():
    return self.ID

  def getName():
    return self.name


def exists(city):
    cities = get()
    for c in cities:
      if c["name"].lower() == city.lower():
        return c
    
    raise ValueError('city {city} does not exist'.format(city=city))

def get():
  r = requests.get('https://www.rede-expressos.pt/api/locations/origins?national=true')
  return r.json()