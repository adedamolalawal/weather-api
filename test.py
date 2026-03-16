
from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
WEATHER_API_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City parameter is required"}), 400

    params = {
        'q': city,
        'appid': WEATHER_API_KEY,
        'units': 'metric'
    }

    response = requests.get(WEATHER_API_URL, params=params)
    print (response)
    
    if response.status_code == 404:
        return jsonify({"error": "City not found"}), 404
    elif response.status_code != 200:
        return jsonify({"error": "Failed to fetch weather data"}), 500

    data = response.json()

    result = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    }

    return jsonify(result)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5001))
    app.run(host='0.0.0.0', port=port)
