import requests
from datetime import datetime

MY_LAT = 28.689619
MY_LNG = 77.134216

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,
}

response = requests.get(url=" https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
sunrise = sunrise.split("T")[1].split("+")[0]
sunset = sunset.split("T")[1].split("+")[0]

current_time = str(datetime.now())
current_time = current_time.split(" ")[1].split(".")[0]

print(f"Sunrise time in delhi is {sunrise}")
print(f"Sunset time in delhi is {sunset}")
print(f"Current time in delhi is {current_time}")

# Output
# Sunrise time in delhi is 00:02:31
# Sunset time in delhi is 13:33:08
# Current time in delhi is 23:30:49
