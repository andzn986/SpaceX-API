# 24.04.2021 - SpaceX
# Andrzej Gawlowski
import requests
import csv


class Flight:
    def __init__(self, flight_number, mission_name, rocket_id, rocket_name, launch_date_utc, video_link):
        self.rocket_id = rocket_id
        self.rocket_name = rocket_name
        self.launch_date_utc = launch_date_utc
        self.video_link = video_link
        self.mission_name = mission_name
        self.flight_number = flight_number


flights = []

try:
    r = requests.get('https://api.spacexdata.com/v3/launches').json()
except:
    raise Exception("Couldn't connect to SpaceX api.")

for flight in r:
    flights.append(Flight(flight['rocket']['rocket_id'], flight['mission_name'], flight['rocket']['rocket_id'],
                          flight['rocket']['rocket_name'], flight['launch_date_utc'], flight['links']['video_link']))

with open("Flights.csv", "a+") as f:
    writer = csv.writer(f)

    for flight in flights:
        writer.writerow(
            [flight.flight_number, flight.mission_name, flight.rocket_id, flight.rocket_name, flight.launch_date_utc,
             flight.video_link])
