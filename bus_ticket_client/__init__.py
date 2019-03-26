class Client(object):

  def __init__(self, name, city):
    self.name = name
    self.city = city
  
  def getName(self):
    return self.name

  def printCityName(self):
    print (self.city)