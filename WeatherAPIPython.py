import requests
def get_city_weather(city, api_key):
    city_name = city.lower()
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city_name}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        description = data['current']['condition']['text']
        temp = data['current']['temp_c']
        wind = data['current']['wind_kph']

        print(f"\nWeather in {city.capitalize()}:")
        print(f"Temperature: {temp}°C")
        print(f"Wind Speed: {wind} Km/hr")
        print(f"Condition: {description.capitalize()}")

    else:
        print(f"{city_name} not found.")

def main():
    city = input("Enter Your City: ")
    API_KEY = "43a4e56e79f94d4e99b151141251607"

    get_city_weather(city, API_KEY)

if __name__ == "__main__":
    main()