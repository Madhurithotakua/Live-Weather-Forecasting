from flask import Flask, render_template, request, redirect, url_for
import requests
from datetime import datetime
from pymongo import MongoClient

app = Flask(__name__)

# Define your API key
api_key = "98632acd03acc535ab8423f6792f24d3"

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['weather_forecast']
collection = db['forecasts']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        location = request.form['location']
        days = int(request.form['days'])  # Get the number of days for the forecast
        units = request.form['units']

        # Ensure days is within the free API limit (1-5)
        if days < 1 or days > 5:
            return render_template('index.html', error_message="Please enter a number of days between 1 and 5.")

        # Fetch the forecast data for the location
        url = f'https://api.openweathermap.org/data/2.5/forecast?q={location}&appid={api_key}&units={units}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            forecast = f"Forecast data for the next {days} days for every 3 hours:\n"
            
            # Filter and display only the required number of days
            forecast_data = data['list'][:days * 8]  # 8 data points per day
            for item in forecast_data:
                dt = datetime.strptime(item['dt_txt'], "%Y-%m-%d %H:%M:%S")
                temp = item['main']['temp']
                weather = item['weather'][0]['description']
                forecast += f"Date: {dt}, Temp: {temp}°C, Weather: {weather}\n"

            # Store forecast in MongoDB
            collection.insert_one({'location': location, 'forecast': forecast})

            return render_template('forecast.html', location=location, forecast=forecast)
        else:
            forecast = 'Unable to retrieve weather forecast. Please enter a valid location...'
            return render_template('index.html', forecast=forecast)
    else:
        return render_template('index.html')

@app.route('/forecast/<location>')
def forecast(location):
    # Retrieve forecast from MongoDB
    forecast_data = collection.find_one({'location': location})
    if forecast_data:
        forecast = forecast_data['forecast']
        return render_template('forecast.html', location=location, forecast=forecast)
    else:
        return "Forecast not found for this location."

if __name__ == '__main__':
    app.run(debug=True)
