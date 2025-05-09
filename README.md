import requests
from datetime import datetime, timedelta

api = "89d73868a3f78ff1e0c25096816234f8"
weather_history = {}

def celcius_to_kelvin(celsius):
    return celsius + 273.15

def get_weather(lat, lon):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    url = f"{base_url}?lat={lat}&lon={lon}&appid={api}&units=metric"
    
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        try:
            daily_temp = data["main"]["temp"]
            at_kelvin = celcius_to_kelvin(daily_temp)
            feels_like_temp = data["main"]["feels_like"]
            pressure = data["main"]["pressure"]
            humidity = data["main"]["humidity"]
            condition = data["weather"][0]["description"]
            city_name = data.get("name", "Unknown")
            entry = {
                "city": city_name,
                "temp_c": daily_temp,
                "temp_k": at_kelvin,
                "feels_like": feels_like_temp,
                "pressure": pressure,
                "humidity": humidity,
                "condition": condition,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            # Use timestamp as a unique key for saving the entry

            print(f"\nWeather in {city_name}:")
            print(f"Temperature: {daily_temp}°C")
            print(f"Temperature in Kelvin: {at_kelvin:.2f} K")
            print(f"Feels Like: {feels_like_temp}°C")
            print(f"Pressure: {pressure} hPa")
            print(f"Humidity: {humidity}%")
            print(f"Condition: {condition}")

            # Ask for sunrise/sunset
            choice = input("\nDo you want to see sunrise and sunset info? (yes/no): ").strip().lower()
            if choice == "yes":
                timezone_offset = data["timezone"]  # seconds
                sunrise_utc = datetime.utcfromtimestamp(data["sys"]["sunrise"])
                sunset_utc = datetime.utcfromtimestamp(data["sys"]["sunset"])
                sunrise_local = sunrise_utc + timedelta(seconds=timezone_offset)
                sunset_local = sunset_utc + timedelta(seconds=timezone_offset)

                print(f"Sunrise: {sunrise_local.strftime('%H:%M:%S')}")
                print(f"Sunset: {sunset_local.strftime('%H:%M:%S')}")

            save_choice = input("Do you want to save this weather data? (yes/no): ").strip().lower()
            
            if save_choice == "yes":
                s = input("input a key to see old data: ")

                weather_history[s] = entry

                print(f"Weather data saved with key: {s}")

        except KeyError:
            print("Error: Missing expected data in response.")
    else:
        print("\nInvalid coordinates or API key error.")
        print("Status code:", response.status_code)

def retrieve_weather_by_key():
    key = input("Enter the  key to retrieve the saved weather data: ").strip()
    # Retrieve the data from history using the key
    if key in weather_history:
        entry = weather_history[key]
        print(f"\nWeather Data for '{key}':")
        print(f"Timestamp: {entry['timestamp']}")
        print(f"City: {entry['city']}")
        print(f"Temperature: {entry['temp_c']}°C")
        print(f"Condition: {entry['condition']}")
    else:
        print("No data found for the provided key.")
def weather_forcast_update(lat,lon):
    base_url = "https://api.openweathermap.org/data/2.5/forecast"
    url = f"{base_url}?lat={lat}&lon={lon}&appid={api}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
         print("\n5-Day Forecast (Daily at 12:00 PM):")
         for forecast in data["list"]: 
            if "12:00:00" in forecast["dt_txt"]:
             date= forecast["dt_txt"].split()[0]
             temp = forecast["main"]["temp"]
             desp = forecast["weather"][0]["description"]
             print (f"{date}: {temp}:{desp}")
    else:
        print("not found")

while True:
    print("\nWelcome to Realtime Weather by Coordinates and City Name")
    user_command = input("Type 'history' to see previous data, 'get' to fetch new weather, 'retrieve' to get saved data by key, or 'exit' to quit: ").strip().lower()

    if user_command == "exit":
        break

    elif user_command == "history":
        if not weather_history:
            print("No weather history available yet.")
        else:
            for key, entry in weather_history.items():
                print(f"{key}: {entry['timestamp']} - {entry['city']} - {entry['temp_c']}°C - {entry['condition']}")

    elif user_command == "retrieve":
        retrieve_weather_by_key()

    elif user_command == "get":
        take = input("Do you want to get weather by (1) coordinates or (2) city name? Enter 1 or 2: ").strip()
        
        if take == "1":
            lat_input = input("Enter latitude: ").strip()
            lon_input = input("Enter longitude: ").strip()

            try:
                lat = float(lat_input)
                lon = float(lon_input)
                get_weather(lat, lon)
            except ValueError:
                print("Please enter valid numbers for coordinates.")
        
        elif take == "2":
            city_name = input("Enter city name: ").strip()
            base_url = "https://api.openweathermap.org/data/2.5/weather"
            url = f"{base_url}?q={city_name}&appid={api}&units=metric"
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                lat =data['coord']['lat']
                lon =data['coord']['lon']
                get_weather(lat,lon)
                

                weather_forcast = input("do you want to weather forecast for 5 days? yes or no: ")
                if weather_forcast == "yes":
                    weather_forcast_update(lat,lon)
                else:
                    print ("thanks")
            else:
                print("City not found.")
        else:
            print("Invalid input. Please enter 1 or 2.")


    else:
        print("Unknown command. Please type 'get', 'history', 'retrieve', or 'exit'.")
