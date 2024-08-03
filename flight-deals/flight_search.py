import requests
from datetime import datetime

class FlightSearch:

    def __init__(self):
        self.endpoint = 'https://api.duffel.com/air/offer_requests'
        self.limit = 1

    def check_flights(self):
        headers = {
            'Authorization': 'Bearer duffel_test_BGYEqO0AdltttQVEiNooVKVytvCSXW67FGfuG3ptcSP',
            'Duffel-Version': 'v1',
            'Content-Type': 'application/json'
        }

        data = {
            "data": {
                "slices": [
                    {
                        "origin": "LHR",
                        "destination": "JFK",
                        "departure_date": "2024-05-24",
                        "arrival_time": {
                            "to": "17:00",
                            "from": "09:45"
                        }
                    }
                ],
                "private_fares": {
                    "QF": [
                        {
                            "corporate_code": "FLX53",
                            "tracking_reference": "ABN:2345678"
                        }
                    ],
                    "UA": [
                        {
                            "corporate_code": "1234",
                            "tour_code": "578DFL"
                        }
                    ]
                },
                "passengers": [
                    {
                        "family_name": "Last",
                        "given_name": "Name",
                        "loyalty_programme_accounts": [
                            {
                                "account_number": "12901014",
                                "airline_iata_code": "BA"
                            }
                        ],
                        "type": "adult"
                    },
                    {
                        "fare_type": "student"
                    },
                ],
                "max_connections": 0,
                "return_offers": False,
                "cabin_class": "economy",
                "supplier_timeout": 500
            }
        }

        response = requests.post(f"{self.endpoint}?limit={self.limit}", json=data, headers=headers)
        self.flight_data = response.json()

        self.price = self.flight_data["data"]["offers"][0]["total_amount"]

        self.destination_city = self.flight_data["data"]["slices"][0]["destination"]["city_name"]
        self.destination_airport = self.flight_data["data"]["slices"][0]["destination"]["iata_code"]

        self.origin_city = self.flight_data["data"]["slices"][0]["origin"]["city_name"]
        self.origin_airport = self.flight_data["data"]["slices"][0]["origin"]["iata_code"]

        self.date = self.flight_data["data"]["offers"][0]["slices"][0]["segments"][0]["departing_at"]
        self.date_time = datetime.strptime(self.date, "%Y-%m-%dT%H:%M:%S")
        self.departure = self.date_time.strftime("%d %B %Y at %H:%M:%S")



