import passenger, app, datetime

# test function
def main():
  psg = passenger.Passenger("Jose", "email", 26, "Rua", "991", 214, "dasd")
  client = app.App(psg)
  date = datetime.datetime.now()
  client.buy_tickets("Nazare", "Lisboa Sete Rios", date)


if __name__ == "__main__":
    main()

