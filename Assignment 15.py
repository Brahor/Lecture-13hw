import requests


API_KEY = "fc80663f5295a9ba960d85ccafc643f4"

BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"

def get_forecast(city_name):
    """ Get weather forecast information for the given city name. """
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'  
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        
        data = response.json()
        
        first_forecast = data['list'][0]
        temp = first_forecast['main']['temp']
        weather_description = first_forecast['weather'][0]['description']
        return temp, weather_description
    else:
        print("Error:", response.status_code, response.text)
        return None, None

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    temperature, weather_description = get_forecast(city_name)
    
    if temperature is not None and weather_description is not None:
        print(f"Forecast for {city_name}: {temperature}°C, {weather_description}")
    else:
        print("Failed to get the weather forecast data")
