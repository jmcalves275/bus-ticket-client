import requests

class Passenger(object):
  def __init__(self, name, email, age, address, phone, nif, docID):
    self.name = name
    self.email = email
    self.age = age
    self.address = address
    self.phone = phone
    self.nif = nif
    self.docID = docID
    self.type = get_passenger_type(age)
    

def get_passenger_type(age):
  if age <= 3: 
    return 45
  elif age <= 12:
    return 2
  elif age <= 29:
    return 4
  elif age <= 64:
    return 1
  else:
    return 5