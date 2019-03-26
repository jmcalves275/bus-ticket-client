import requests

class Client(object):

  def __init__(self, name, city):
    self.name = name
    self.city = city
  
  def getName(self):
    return self.name

  def getCities(self):
    return requests.get('https://www.rede-expressos.pt/api/locations/origins?international=true')