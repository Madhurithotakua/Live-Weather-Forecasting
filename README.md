# Weather Forecasting Application

A web-based weather forecasting application built with Flask, Python, and MongoDB that allows users to check the weather forecast for a specific location over the next 1 to 5 days. The app fetches real-time weather data using the OpenWeatherMap API and displays it in a user-friendly format.

## Features

- Fetches real-time weather data for a specified location.
- Provides weather forecasts for 1 to 5 days with 3-hour intervals.
- Allows users to choose the measurement units (Metric or Imperial).
- Stores and retrieves weather forecasts in/from MongoDB.

## Prerequisites

To run this application, you'll need:

- Python 3.7 or higher
- Flask (`pip install flask`)
- Requests library (`pip install requests`)
- MongoDB server running locally
- PyMongo (`pip install pymongo`)

## Setup Instructions

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/weather-forecasting-app.git
    cd weather-forecasting-app
    ```

2. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run MongoDB locally**:

   Make sure your MongoDB server is running locally on port 27017. You can start MongoDB using:

    ```bash
    mongod
    ```

4. **Set up the API key**:

   Sign up at [OpenWeatherMap](https://openweathermap.org/) to get your API key. Replace the placeholder `api_key` in `app.py` with your actual API key:

    ```python
    api_key = "your_api_key_here"
    ```

5. **Run the Flask application**:

    ```bash
    python app.py
    ```

6. **Access the application**:

   Open your browser and go to `http://127.0.0.1:5000/` to use the weather forecasting app.

## Application Usage

1. Enter the location for which you want to check the weather forecast.
2. Select the number of days (1-5) for the forecast.
3. Choose the units of measurement (Metric or Imperial).
4. Click the "Get Forecast" button to fetch and display the weather data.

## File Structure

- **app.py**: Main Flask application file that handles routing, API calls, and MongoDB operations.
- **templates/**:
  - `index.html`: Main page for input and weather forecast display.
  - `forecast.html`: Page to display the weather forecast results.
- **static/**:
  - `style.css`: Contains styling for the application.

## Example

To fetch the weather forecast for "New York" over the next 3 days:

1. Enter "New York" in the location field.
2. Select "3" for the number of days.
3. Choose "Metric (°C, m/s)".
4. Click "Get Forecast".

The application will display the weather data for every 3 hours over the next (1-5) days.

## Screenshots
Enter the input required:
![Screenshot 2024-09-13 203543](https://github.com/user-attachments/assets/1a3a26f1-6ca9-4d7d-9375-5aca2b517438)

The forecsting weather temp for every 3 hours over the next 3 days.
![Screenshot 2024-09-13 203600](https://github.com/user-attachments/assets/04febde0-a13e-4dcc-9652-c0fd8bb761f6)


## Technologies Used

- **Python**: Core programming language.
- **Flask**: Web framework used to create the application.
- **MongoDB**: Database used to store and retrieve weather forecasts.
- **OpenWeatherMap API**: Source of real-time weather data.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any changes or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please contact [your_email@example.com].

