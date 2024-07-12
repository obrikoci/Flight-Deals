from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()

today = datetime.now() + timedelta(days=1)
tomorrow = today.date()
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))
six_months_from_tomorrow = six_month_from_today.date()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.check_flights()
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()


flight = flight_search.check_flights()
notification_manager.send_sms(
     message=f"Low price alert! Only ${flight_search.price} to fly from {flight_search.origin_city}-"
             f"{flight_search.origin_airport} to {flight_search.destination_city}-{flight_search.destination_airport}, "
             f"on {flight_search.departure}."
    )

