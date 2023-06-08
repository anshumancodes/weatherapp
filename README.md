
# WeatherApp

WeatherApp is a simple web application that provides current weather information based on user input. It utilizes the OpenWeather API to fetch weather data and is built using the Django framework.

## Features

- Allow users to search for the current weather of a specific location.
- Display the temperature, weather condition, humidity, and wind speed for the searched location.

 To be added:
- Support for  Celsius and Fahrenheit temperature units.
- Display relevant weather icons based on the weather condition.

## Prerequisites

Before running the WeatherApp, ensure that you have the following prerequisites installed:

refer: requirements.txt

## Installation

1. Clone the repository or download the source code:

   ```bash
   git clone https://github.com/anshumancodes/weatherapp.git
   ```

2. Navigate to the project directory:

   ```bash
   cd weatherapp
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Obtain an API key from [OpenWeather](https://openweathermap.org/). Create a free account if you don't have one.

5. In the app's (home) `views.py` file, update the `apikeys.weatherapikey` variable with your OpenWeather API key

   

## Usage

1. Start the development server:

   ```bash
   python manage.py runserver
   ```

2. Access the WeatherApp in your web browser at `http://localhost:8000/`.

3. Enter the desired location in the search bar and click on the "Search" button.

4. The current weather information for the specified location will be displayed, including temperature, weather condition, humidity, and wind speed.

5. To switch between Celsius and Fahrenheit temperature units, click on the respective buttons.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please create a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

## Acknowledgments

- Weather data provided by [OpenWeather](https://openweathermap.org/).
- Built with [Django](https://www.djangoproject.com/).


