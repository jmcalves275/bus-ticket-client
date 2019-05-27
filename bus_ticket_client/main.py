import passenger, app, datetime, json

# test function
def main():
  psg = passenger.Passenger("name", "email", 26, "address", "phone", "nif", "docID")

  client = app.App(psg)
  
  date = datetime.datetime.now()

  response = client.buy_tickets("from_city", "to_city", date, "HH:MM")

  print(json.dumps(response, indent=2))


if __name__ == "__main__":
    main()

