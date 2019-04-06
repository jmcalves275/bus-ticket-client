import requests, city


class App(object):

  def __init__(self, passenger, seat_type):
    self.passenger = passenger
    self.cities = city.get_cities()
    self.seat_type = seat_type

  def city_exists(self, city):
    for c in self.cities:
      if c["name"].lower() == city.lower():
        return c
    
    raise ValueError('city {city} does not exist'.format(city=city))

  def buy_tickets(self, from_city, to_city, date, hour):
    try:
      from_city = self.city_exists(from_city)
      to_city = self.city_exists(to_city)

      #pickup_itenerary(from_city, to_city, date, hour)
        #get_iteneraries(from_city, to_city, date)  
        #itenerary exists?


      print(from_city)

    except Exception as error:
        print('err: ' + repr(error))

    
