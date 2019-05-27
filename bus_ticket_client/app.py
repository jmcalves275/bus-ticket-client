import requests, city, json


class App(object):
  def __init__(self, passenger):
    self.passenger = passenger

  def buy_tickets(self, from_city, to_city, date, time):
    try:
      from_city = city.exists(from_city)
      to_city = city.exists(to_city)

      ticket = self.get_ticket(from_city, to_city, date, time)
      reservation_token = self.create_reservation(date, ticket)
      
      #pick_seat()
      
      self.fill_passenger_info(reservation_token)
      details = self.get_reservation_details(reservation_token)

      finalize_response = self.finalize(details["reservationId"])

      transaction_id = get_transaction_id(finalize_response)
      
      response = self.get_payment_details(transaction_id)

      return response

    except Exception as error:
        print('err: ' + repr(error))

  def get_ticket(self, source, destination, date, dep_time):
    payload={
      "Destination": destination["id"],
      "HasReturn": False, 
      "Ida": str(date),
      "Passenger": [{
        "Code": "",
        "DocId": "",
        "Email": "",
        "Name": "",
        "Type": self.passenger.type
      }],
      "Source": source["id"]
    }

    url = 'https://www.rede-expressos.pt/api/ticketing/getTickets/'
    
    r = requests.post(url, json=payload)

    for response in r.json():
      for outgoing in response["outgoing_schedules"]:
        if outgoing["departure_time"] == dep_time:
          return outgoing

    raise ValueError('departure time {dep_time} not found'.format(dep_time=dep_time))

  def create_reservation(self, date, ticket):
    payload = {
      "dateIda": str(date),
      "dateVolta": None,
      "document": None,
      "idIda": ticket["schedule_id"],
      "idVolta": None,
      "isRecover": False,
      "passengers": [
        {
          "Code": "",
          "Type": self.passenger.type,
          "DocId": "",
          "Email": "",
          "Name": "",
          "price_type_id": "A"
        }
      ],
      "recovery": None
    }  

    url = 'https://www.rede-expressos.pt/api/reservation/create'
    
    r = requests.post(url, json=payload)
    response = r.json()
    
    return response  

  def fill_passenger_info(self, reservation_token):
    payload = {
      "Id": reservation_token,
      "passengers": [{
        "Code": "",
        "Type": self.passenger.type,
        "DocId": self.passenger.docID,
        "Email": self.passenger.email,
        "Name": self.passenger.name,
        "price_type_id": "A"
      }]
    }

    url = "https://www.rede-expressos.pt/api/passengers/setList/"
    
    r = requests.post(url, json=payload)
    response = r.json()

    return response
  
  def get_reservation_details(self, reservation_token):
    payload = {
      "Id": reservation_token
    }
    url = "https://www.rede-expressos.pt/api/reservation/details"
    
    r = requests.post(url, json=payload)
    response = r.json()

    return response

  def finalize(self, reservation_number):
    payload = {
      "clientInfo": {
        "activateReferenceTransaction": False, 
        "email": self.passenger.email,
        "nCard": None, 
        "nClient": None,
        "nDocId": self.passenger.docID,
        "paymentType": "MBWAY",
        "paymentTypeSpecified": True,
        "phoneMBWay": self.passenger.phone,
        "clientName": self.passenger.name,
        "clientPerfil": None,
      },
      "clientTaxInfo": {
        "clientTaxCountry": "PT", 
        "clientTaxCountrySpecified": True,
        "clientTaxID": self.passenger.nif,
        "clientTaxName": self.passenger.name,
        "taxAddress": {
          "country": "PT"
          }
        },
      "language": "PT",
      "passangers": [{
        "Name": self.passenger.name, 
        "Email": self.passenger.email, 
        "DocId": self.passenger.docID,
        "Code": "", 
        "Type": self.passenger.type,
        "price_type_id": "A"
      }],
      "recover": None,
      "reservationNumber": reservation_number,
      "sessionID": "123456"
    }

    url = "https://www.rede-expressos.pt/api/payments/paymentFinalize"
    
    r = requests.post(url, json=payload)
    response = r.json()

    return response



  def get_payment_details(self, transaction_id):
    payload = {
      "transId": transaction_id,
      "hook": True
    }

    url = "https://www.rede-expressos.pt/api/payments/paymentDetails/"

    r = requests.post(url, json=payload)
    response = r.json()

    return response

def get_transaction_id(url):
  to_find = "TransID"
  index = url.find(to_find)
  return url[index+len(to_find)+1:]